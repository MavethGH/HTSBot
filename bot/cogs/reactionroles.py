import discord.ext.commands as commands
import config
import os

class ReactionRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # Store active messages by guild
        self.active_messages = dict()
        # Store emoji-role pairs by message
        self.rrmappings = dict()


    @commands.group(aliases=["rr"])
    @commands.has_permissions(manage_messages=True)
    async def reactionroles(self, ctx):
        """The group for reaction role commands"""


    @reactionroles.command()
    @commands.guild_only()
    async def message(self, ctx, message: commands.MessageConverter):
        """Sets the active message for the caller's guild
           Requires a message ID obtained by shift-clicking Copy ID"""
        self.active_messages[ctx.guild] = message


    @reactionroles.command()
    @commands.guild_only()
    async def add(self, ctx, emoji: commands.EmojiConverter, role: commands.RoleConverter):
        """Adds a mapping of emoji to role. The bot will listen for users reacting
           with that emoji and give them the corresponding role"""

        # message command must be used first
        if ctx.guild in self.active_messages:
            msg_id = self.active_messages[ctx.guild].id
        else:
            await ctx.send("Please select a message first, using `rr message <message_id>`.")
            return

        # Stores mappings of emojis to roles
        if msg_id not in self.rrmappings:
            self.rrmappings[msg_id] = dict()

        # Storing emoji by hash so that custom and unicode emojis behave the same
        self.rrmappings[msg_id][hash(emoji)] = role

        await ctx.send("Listener successfully added!")


    @commands.Cog.listener('on_raw_reaction_add')
    async def handle_reaction(self, payload):
        """ For each reaction, check if a new role needs to be assigned"""

        if payload.message_id in self.rrmappings:
            role = self.rrmappings[payload.message_id][hash(payload.emoji)]
            await payload.member.add_roles(role)

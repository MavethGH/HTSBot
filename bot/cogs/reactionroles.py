import discord.ext.commands as commands
import emoji


class UnicodeEmojiConverter(commands.EmojiConverter):
    """For some reason, normal EmojiConverter does not work with Unicode
       emojis. This should prevent it from raising an error every time."""
    async def convert(self, ctx, argument):
        if emoji.emoji_count(argument):
            return argument
        else:
            custom_emoji = await super().convert(ctx, argument)
            return custom_emoji


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
    async def add(self, ctx, emoji: UnicodeEmojiConverter, role: commands.RoleConverter):
        """Adds a mapping of emoji to role. The bot will listen for users reacting
           with that emoji and give them the corresponding role"""

        # message command must be used first
        if ctx.guild in self.active_messages:
            msg_id = self.active_messages[ctx.guild].id
            channel = self.active_messages[ctx.guild].channel
        else:
            await ctx.send("Please select a message first, using `rr message <message_id>`.")
            return

        # Stores mappings of emojis to roles
        if msg_id not in self.rrmappings:
            self.rrmappings[msg_id] = dict()

        # Storing emoji by hash for efficiency
        self.rrmappings[msg_id][hash(emoji)] = role

        # Add the initial reaction for users to click on
        message = await channel.fetch_message(msg_id)
        await message.add_reaction(emoji)
        # Success!
        await ctx.send("Listener successfully added!")

    @commands.Cog.listener('on_raw_reaction_add')
    async def handle_reaction(self, payload):
        """ For each reaction, check if a new role needs to be assigned"""

        # Ignore bot users
        if payload.member.bot:
            return

        if payload.message_id in self.rrmappings:

            if payload.emoji.is_custom_emoji():
                # emoji object will be what got stored earlier
                emoji_hash = hash(payload.emoji)
            else:
                # emoji.name will be the actual unicode emoji that got stored earlier
                emoji_hash = hash(payload.emoji.name)

            role = self.rrmappings[payload.message_id][emoji_hash]
            await payload.member.add_roles(role)

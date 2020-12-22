import discord.ext.commands as commands
import config
import os

class BlockExts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Block bad file extensions, such as .exe
    @commands.Cog.listener()
    async def on_message(message):
        if not message.attachments:
            pass

        for att in message.attachments:
            fname, fext = os.splitext(att.name)
            if fext not in config.GOOD_FILE_TYPES:
                if message.channel.permissions_for(message.author).manage_messages:
                    await message.delete()
                    
                    print(f"""Deleted a message with a .{fext} file attached,
                    sent by user {message.author.name} in channel {message.channel.name}.""")
                    break
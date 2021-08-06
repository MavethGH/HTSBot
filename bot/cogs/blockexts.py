from discord.ext import commands
import os.path


class BlockExts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Block bad file extensions, such as .exe
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.attachments:
            pass

        for att in message.attachments:
            fext = os.path.splitext(att.name)[1]  # [0] is the filename
            if fext not in self.bot.config["GOOD_FILE_TYPES"]:
                if message.channel.permissions_for(message.author).manage_messages:
                    await message.delete()

                    print(f"""Deleted a message with a .{fext} file attached,
                    sent by user {message.author.name} in channel {message.channel.name}.""")
                    break

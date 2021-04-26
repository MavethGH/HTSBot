from discord.ext import commands
from operator import itemgetter # Faster than lambda for sorting, I think
from datetime import datetime, timedelta
from is_bot import is_bot

class TimedeltaConverter(commands.Converter):
    async def convert(self, ctx, argument):
        return timedelta(seconds=argument)

class RemoveBots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def botremoval(self, ctx):
        """Command group relating to mass banning spam/scam bots"""

    @botremoval.command()
    async def remove_recent(self, ctx, seconds: TimedeltaConverter):
        """Remove all potential bots that joined recently"""

        time = datetime.utcnow() - seconds

        # I'm like 70% sure this gets members who joined later than after
        recent_members = await guild.fetch_members(after=time)
        
        # Eventually this function will be able to filter out legit users
        for member in recent_members:
            if self.bot.config["DEBUG_MODE"]:
                await member.send("If this wasn't a drill, you would be banned")
            elif is_bot(member):
                await member.ban(
                # Reason for banning subject to change
                reason="Automatic bot removal. If you are not a bot, let us know who to unban in IRC.",
                delete_message_days=1)
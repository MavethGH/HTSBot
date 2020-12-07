from discord.ext import commands

from reactionroles import ReactionRoles
from blockexts import BlockExts

bot = commands.Bot(command_prefix='~')

bot.add_cog(BlockExts(bot))
bot.add_cog(ReactionRoles(bot))

bot.run('PLACEHOLDER_TOKEN')
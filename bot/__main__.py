from discord.ext import commands

import config

from reactionroles import ReactionRoles
from blockexts import BlockExts

bot = commands.Bot(command_prefix=config.PREFIX)

bot.add_cog(BlockExts(bot))
bot.add_cog(ReactionRoles(bot))

bot.run(config.TOKEN)
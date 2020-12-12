from bot import HTSBot

from cogs.reactionroles import ReactionRoles
from cogs.blockexts import BlockExts

bot = HTSBot()

bot.add_cog(BlockExts(bot))
bot.add_cog(ReactionRoles(bot))

bot.run(bot.config["TOKEN"])
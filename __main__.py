from discord.ext import commands
from discord import Intents

from bot.bot import HTSBot
from bot.cogs.reactionroles import ReactionRoles
from bot.cogs.blockexts import BlockExts

intents = Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

bot = HTSBot(command_prefix="~", intents=intents)

bot.add_cog(BlockExts(bot))
bot.add_cog(ReactionRoles(bot))

bot.run(bot.config["TOKEN"])
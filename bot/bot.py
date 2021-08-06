from discord.ext import commands
import json


# Subclassing Bot to add config data that can be viewed by cogs without hassle
class HTSBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open('bot/config.json', 'r') as config:
            self.config = json.load(config)

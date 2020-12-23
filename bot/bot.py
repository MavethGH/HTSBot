from discord.ext import commands
import json


# Subclassing Bot to add config data that can be viewed by cogs without hassle
class HTSBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        with open('config.json') as config:
            self.config = json.load(config)
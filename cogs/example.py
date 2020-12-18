from discord.ext import commands
import importlib
from os.path import basename, dirname

botpy = importlib.import_module("bot", "../")

class exampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def example(self, ctx):
        await ctx.send(self)

def setup(bot):
    botpy.cmds["example"] = "Debug command"

    bot.add_cog(exampleCog(bot))

def teardown(bot):
    del botpy.cmds["example"]

    bot.remove_cog(exampleCog(bot))

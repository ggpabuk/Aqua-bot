import discord
from discord.ext import commands
import importlib
import sys

botpy = importlib.import_module("bot", "../")

class exampleCog(commands.Cog):
    def __init__(self, bot):
        botpy.cmds["test"] = "Debug command"
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send(self)

def setup(bot):
    bot.add_cog(exampleCog(bot))

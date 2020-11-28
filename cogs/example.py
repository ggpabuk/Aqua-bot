import discord
from discord.ext import commands

class exampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send(self)

def setup(bot):
    bot.add_cog(exampleCog(bot))

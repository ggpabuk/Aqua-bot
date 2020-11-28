import discord
from discord.ext import commands
import json
import os

config = json.load(open("config.json"))

bot = commands.Bot(
    command_prefix=config["prefix"],
    owner_ids=config["ownerIds"]
)

#COG Auto Loader
for filename in os.listdir("./cogs"):
    if not filename.endswith('.py'): continue
    try:
        bot.load_extension(f"cogs.{filename[:-3]}")
    except Exception as e:
        print(f"Failed to load {filename} ({e})")
    else:
        print(f"{filename} loaded")

@bot.command()
async def ping(ctx):
    await ctx.send(f"pong in {bot.latency}!")

bot.run(config["token"])

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
if (config["cogloader_enabled"]):
    for filename in os.listdir("./cogs"):
        if not filename.endswith('.py'): continue
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
            print(f"Failed to load {filename} ({e})")
        else:
            print(f"{filename} loaded")

# COG management
@bot.command()
async def pyload(ctx, extension):
    if not await bot.is_owner(ctx.message.author):
        await ctx.send(f"Failed to load some extension (You dont have enough rights.)")
        return
    elif not config["cogsmanagement_enabled"]:
        await ctx.send(f"Failed to unload some extension (Cogs management disabled.)")
        return

    try:
        bot.load_extension(f"cogs.{extension}")
    except Exception as e:
        await ctx.send(f"Failed to load {extension}.py ({e})")
    else:
        await ctx.send(f"{extension}.py loaded")

@bot.command()
async def pyunload(ctx, extension):
    if not await bot.is_owner(ctx.message.author):
        await ctx.send(f"Failed to unload some extension (You dont have enough rights.)")
        return
    elif not config["cogsmanagement_enabled"]:
        await ctx.send(f"Failed to unload some extension (Cogs management disabled.)")
        return

    try:
        bot.unload_extension(f"cogs.{extension}")
    except Exception as e:
        await ctx.send(f"Failed to unload {extension}.py ({e})")
    else:
        await ctx.send(f"{extension}.py unloaded")


@bot.command()
async def ping(ctx):
    await ctx.send(f"pong in {bot.latency}!")

bot.run(config["token"])

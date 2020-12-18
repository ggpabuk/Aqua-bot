#from modules import *
from clrprint import *
import discord
from discord.ext import commands
import json
import os

config = json.load(open("config.json"))

bot = commands.Bot(
    command_prefix=config["prefix"],
    help_command=None,
    owner_ids=config["ownerIds"]
)

# Help command
cmds = { "help": "Bot commands (shows this window)" }

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        description="Bot commands and their description",
        url="https://discord.gg/TQtjbMn",
        colour=discord.Color.from_rgb(19, 184, 204)
    )

    for cmd in cmds.keys():
        embed.add_field(name=cmd, value=cmds[cmd])

    await ctx.send(embed=embed)

# EventHandlers
@bot.event
async def on_ready():
    prefix = config["prefix"]
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"music ({prefix}help)"))
    clrprint("Bot ready! (", bot, ")", clr=["blue", "default", "blue"])

@bot.event
async def on_command_error(ctx, error):
    clrprint("Command error duty to", ctx.message.author, "(", ctx.message.author.id, ") message content:", ctx.message.content, ";\n", error,
        clr=["default", "red", "default", "red", "default", "red", "default", "red"])
    errTxt = str(error).replace("\n", " ")
    await ctx.send(f"Failed to handle \"{ctx.message.content}\" command.\n\n`{errTxt}`")

@bot.event
async def on_command_completion(ctx):
    clrprint(ctx.message.author, "(", ctx.message.author.id, ") used command \"", ctx.message.content, "\"",
        clr=["blue", "default", "blue", "default", "blue", "default"])

#COG Auto Loader
if (config["cogloader_enabled"]):
    for filename in os.listdir("./cogs"):
        if not filename.endswith('.py'): continue
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
            clrprint(f"Failed to load" , filename, "(", e, ")",
                clr=["default", "red", "default", "red", "default"])
        else:
            clrprint(filename, "loaded.", clr=["blue", "default"])

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
        await ctx.send(f"Failed to load {extension}.py. ({e})")
    else:
        await ctx.send(f"{extension}.py loaded.")

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
        await ctx.send(f"Failed to unload {extension}.py. ({e})")
    else:
        await ctx.send(f"{extension}.py unloaded.")

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f"pong in {bot.latency}!")

bot.run(config["token"])

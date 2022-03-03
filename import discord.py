import discord
from discord.ext import commands
from PIL import Image,ImageFont,ImageDraw
import os

client = commands.Bot(command_prefix = '!')
client.remove_command("help")
TOKEN = "OTQ4ODE1ODQxOTIxNzUzMTM4.YiBTnA.7FxMDm8JLuwo-Zq4HyemiX30ncM"

@client.command()
async def mic(ctx):
    vc = 0
    for member in ctx.guild.members:
        voice_state = member.voice
        if voice_state is None:
            continue
        else:
            vc += 1
    img = Image.open("docimic.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("aroal.ttf", 18)
    draw.text((210,300), str(vc), (0,0,0), font=font)
    img.save(f"{vc}.png")
    await ctx.send(file = discord.File(f"{vc}.png"))
    os.remove(f"{vc}.png")

    client.run(TOKEN)
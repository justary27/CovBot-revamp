import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


from discord.ext.commands.core import command

client = commands.Bot(command_prefix="'")
client.remove_command("help")

@client.event
async def on_ready():
    print(" I'm on !")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Covid-19 Guidelines !"))

@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title= "Getting Help",description="Use `-<command name>` to activate !",color=ctx.author.color)
    embed.set_thumbnail(
        url="https://i.pinimg.com/originals/09/b0/08/09b008ceb45878eb34180d23506e4212.gif")

    embed.add_field(name='cinfo',value="Gives the Covid-19 information.",inline=False)
    embed.add_field(name="cc <country name>",value="Use this command to get Covid-19 stats in a country (default:India)\nFor eg: cc usa to get Covid stats of United States",inline=False)
    embed.add_field(name="cmed",value="Get general purpose Medicines name and their Dosage",inline=False)
    embed.add_field(name="cvac",value="Get information and important url related to Vaccination in India",inline=False)


    await ctx.send(embed=embed)

@client.command()
async def load(ctx,extension):
    client.load_extension(f'src.cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'src.cogs.{extension}')

for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'src.cogs.{filename[:-3]}')

client.run(os.getenv('DC_TOKEN'))

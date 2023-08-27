import discord
from discord import app_commands
import calendar
import time
ts = calendar.timegm(time.gmtime())
from discord.ext import commands
import os

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="$", intents=intents)
intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
channelId = os.getenv('channelId')
@bot.event 
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    
    except Exception as e:
        print(e)

@bot.tree.command(name = "name", description= "reminder")
async def name_slash(interaction: discord.Interaction):
    await interaction.response.send_message('you will remind in <time you want>')
    channel = client.get_channel(str(channelId))
    time.sleep(<time you want in seconds>)
    await interaction.channel.send(f"your reminder <@" + str(interaction.user.id) + ">")
    
#create a custom reminder
@bot.tree.command(name = "reminder", description= "custom reminder")
async def rmd_slash(interaction: discord.Interaction, hours: int = None, minutes: int = None, seconds: int = None):
    x = int(3600)*hours + int(60)* minutes + seconds
    await interaction.response.send_message(f'you will remind in ', hours, 'h, ', minutes, ' m et', seconds, 's'  )
    channel = client.get_channel(str(channelId))
    time.sleep(x)
    await interaction.channel.send(f"your reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "source_cod", description = "Tout le code du bot est là, ainsi qu'une version épuré avec seulement l'essentiel")
async def sourcecod_slash(interaction : discord.interactions):
    await interaction.response.send_message("Here is the cod source <link of the github>" )

@bot.tree.command(name = "ping", description = "get the ping")
async def ping_slash(interaction : discord.interactions):
    await interaction.response.send_message(f":ping_pong: pong {int(bot.latency * 1000)} ms !" )



bot.run("token of your bot")

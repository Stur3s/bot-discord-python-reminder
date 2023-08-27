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

@bot.tree.command(name = "yo", description= "p'tit reminder")
async def yo_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 10m')
    channel = client.get_channel(str(channelId))
    time.sleep(9*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")
    
@bot.tree.command(name = "effrayé", description= "p'tit reminder")
async def effrayé_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 20m :scream:')
    channel = client.get_channel(str(channelId))
    time.sleep(19*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "confus", description= "p'tit reminder")
async def confus_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 50m :confounded:')
    channel = client.get_channel(str(channelId))
    time.sleep(49*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "gelé", description= "p'tit reminder")
async def confus_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 1h10 :cold_face:')
    channel = client.get_channel(str(channelId))
    time.sleep(69*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "affamé", description= "reminder si affamé")
async def affamé_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 1h30 :drooling_face: ')
    channel = client.get_channel(str(channelId))
    time.sleep(89*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "endormi", description= "reminder si endormi")
async def affamé_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 3h10 :sleeping:')
    channel = client.get_channel(str(channelId))
    time.sleep(189*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "ivre", description= "reminder si ivre")
async def ivre_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 4h10 :zany_face: ')
    channel = client.get_channel(str(channelId))
    time.sleep(249*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "blessé", description= "reminder si blessé")
async def blessé_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 6h10 :head_bandage:')
    channel = client.get_channel(str(channelId))
    time.sleep(369*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "malade", description= "reminder si malade")
async def blessé_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 6h10 :nauseated_face: ')
    channel = client.get_channel(str(channelId))
    time.sleep(369*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "gravement_blessé", description= "reminder si gravement blessé")
async def grvblessé_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 12h10 :dizzy_face:')
    channel = client.get_channel(str(channelId))
    time.sleep(2*369*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "prison", description= "reminder si gravement blessé")
async def prison_slash(interaction: discord.Interaction):
    await interaction.response.send_message('tu seras remind dans 24h10 :lock:')
    channel = client.get_channel(str(channelId))
    time.sleep(4*369*60+45)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "rmd", description= "ton reminder")
async def rmd_slash(interaction: discord.Interaction, heures: int = 0, minutes: int = 0, secondes: int = 0):
    x = int(3600)*heures + int(60)* minutes + secondes
    await interaction.response.send_message(f"tu seras remind dans {heures} h, {minutes} m et {secondes} s")
    channel = client.get_channel(str(channelId))
    time.sleep(x)
    await interaction.channel.send(f"ton reminder <@" + str(interaction.user.id) + ">")

@bot.tree.command(name = "code_source", description = "Tout le code du bot est là, ainsi qu'une version épuré avec seulement l'essentiel")
async def codesource_slash(interaction : discord.interactions):
    await interaction.response.send_message("Voici le code source du bot, tu trouveras également une version épurée pour avoir seulement l'essentiel : https://github.com/Stur3s/bot-discord-python-reminder" )

@bot.tree.command(name = "ping", description = "obtient la latence du bot")
async def ping_slash(interaction : discord.interactions):
    await interaction.response.send_message(f"Le bot a {int(bot.latency * 1000)} ms !" )

bot.run("token du bot")

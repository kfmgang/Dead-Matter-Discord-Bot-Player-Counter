import discord
from discord.ext import tasks
import a2s
import socket
import config


client = discord.Client()

@client.event
async def on_ready():
    update_player_count.start()

@tasks.loop(seconds=20)
async def update_player_count():
    try:
        Player = a2s.info(config.SERVER_ADDRESS).player_count
        MaxPlayers = a2s.info(config.SERVER_ADDRESS).max_players
    except socket.timeout as error:
        await client.change_presence(activity=discord.Game(name=f"Server is off"))
    else:
        await client.change_presence(activity=discord.Game(name=f"{Player}/{MaxPlayers} Players Connected"))

client.run(config.BOT_TOKEN)

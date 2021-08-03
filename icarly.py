# icarly.py
##Author: Eduard Varshavsky, David Gendelman
##File Name: icarly.py
##Program Name: icarly.py
##Creation Date: August 2nd, 2021
##Modified Date: August 3rd, 2021
##Description: Discord bot for discord

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to Discord!'
           f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    print(f'test')

client.run(TOKEN)

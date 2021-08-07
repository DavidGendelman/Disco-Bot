# main.py
## Author: Eduard Varshavsky, David Gendelman
## File Name: main.py
## Program Name: main
## Creation Date: August 2nd, 2021
## Modified Date: August 07, 2021
## Description: Discord bot for discord

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
    print(
        f'{client.user} has connected to Discord!\n'
        f'{guild.name}(id: {guild.id})'
    )
         
    member_objs = await guild.fetch_members(limit=None).flatten()
    members = '\n - '.join([member.name for member in  member_objs])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)

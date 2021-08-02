# icarly.py
##Author: Eduard Varshavsky, David Gendelman
##File Name: icarly.py
##Program Name: icarly.py
##Creation Date: August 2nd, 2021
##Modified Date: August 2nd, 2021
##Description: Discord bot for discord

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

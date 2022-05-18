import discord
import time
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
  print('Bot started and authorized as {0.user}'.format(client))

class Ping:
  def __init__(self, bot, api):
    self.bot = bot
    self.api = api

@client.command()
async def ping(ctx):
  before = time.monotonic()
  msg = await ctx.send('Pong..')
  ping = Ping(int(client.latency * 1000), int((time.monotonic() - before) * 1000))
  await msg.edit(content=f'Pong! Bot Latency {ping.bot}ms\nAPI Latency {ping.api}ms')

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)

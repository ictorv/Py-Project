import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print("Now logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Kripya spam na kare!')
client.run('MTAzMzAwMjk3MTg1Mzc2NjY4Ng.GqL7mk.FVJZYy7NOViCW5GdXLplkiHfBbxDnahG3XKBQY')
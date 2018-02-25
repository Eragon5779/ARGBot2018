import asyncio
import discord
from discord.ext.commands import bot
from discord.ext import commands

# echo
questions = { "Is it a piece of technology?" : True,
              "Does it glow pleasantly?" : True,
              "Is it brightly colored?" : False,
              "Is it personal?" : True,
              "Does it love you?" : False,
              "Is it a tube?" : True,
              "Does it have personality?" : True,
              "Is it well known?" : True,
              "Is it a piece of software?" : False,
              "Can it sing?" : True,
              "Can it respond to your voice?" : True }

Client = discord.Client()
bot = commands.Bot(command_prefix = ".")

@client.event
async def on_message(message):
	if not message.author.bot:
		m = message.content.lower()
		if m.contains("echo"):
			uid = message.author.id
			await client.send_message(message.channel,"<@%s> You got it!" % (uid))
		if m.contains("true") or m.startswith("t") or m.contains("1"):

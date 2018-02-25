# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="ARGBot by the UNCo Team", command_prefix="!", pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=268516352'.format(client.user.id))
	print('--------')
	print('You are running ARGBot v0.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by The UNCo Team')
	return await client.change_presence(game=discord.Game(name='! to play')) #This is buggy, let us know if it doesn't work.

# Questions dictionary
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

@client.event
async def on_message(message) :
	role = discord.utils.get(message.server.roles, name="twenty")
	if message.author == client.user :
		return
	if "echo" in message.content.lower() and message.channel.name != 'word-hunt':
		await client.send_message(message.channel, "You got it <@%s>!" % (message.author.id))
		await client.delete_message(message)
		await client.add_roles(message.author, role)
	if "start" in message.content.lower() and message.channel.name != 'word-hunt' :
		await client.send_message(message.channel, 'Asking questions! Answer "true" or "false"')
		for question in questions.keys() :
			await client.send_message(message.channel, "<@%s>, %s" % (message.author.id, question))
			def checkContent(msg) :
				return 'echo' in msg.content.lower() or 'true' in msg.content.lower() or 'false' in msg.content.lower() or 'yes' in msg.content.lower() or 'no' in msg.content.lower()
			msg = await client.wait_for_message(author=message.author, check=checkContent)
			alt = False
			if 'yes' in msg.content.lower() :
				alt = True
				
			if msg.content.lower() == str(questions[question]).lower() :
				await client.send_message(message.channel, "Correct <@%s>!" % msg.author.id)
			elif alt == questions[question] :
				await client.send_message(message.channel, "Correct <@%s>!" % msg.author.id)
			elif "echo" in msg.content.lower() :
				await client.send_message(message.channel, "You got it <@%s>!" % (message.author.id))
				await client.add_roles(message.author, role)
				break
			elif msg.content.lower() != str(questions[question]).lower()  :
				await client.send_message(message.channel, "Incorrect <@%s>!" % msg.author.id)
			elif alt != questions[question] :
				await client.send_message(message.channel, "Incorrect <@%s>!" % msg.author.id)
			await client.delete_message(msg)
		await client.send_message(message.channel, 'Think you have an answer <@%s>? Type it in!' % message.author.id)

# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.
client.run('')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.

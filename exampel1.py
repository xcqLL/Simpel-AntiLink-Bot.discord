import discord
from discord.ext import commands

# Set up intents 
intents = discord.Intents.all()  
intents.messages = True
bot = commands.Bot(command_prefix="/",intents=intents) 

channel_id = 1229723305917808655 # Change the channel_id to your channel id

@bot.event
async def on_ready(): #This function will be called when the bot has finished the initialization process and is ready to receive commands.
    print(f'Logged in as {bot.user.name}')  # Give us notification when the bot active in terminal

@bot.event 
async def on_message(message):  #This function will be called every time the bot receives a message on the supervised Discord server.
    if message.channel.id == channel_id: #This is often used to ensure that bots only respond to messages from specific channels or perform certain actions based on the location of those messages within the Discord server. 
        if any(url in message.content for url in ["https://", "http://"]): #check the link when we send on discord 
            await message.delete() #Delete the message because the link above is already set 
            await message.channel.send(f"{message.author.mention}, Please do not send links") #Message displayed by the bot when it has deleted the link in the Discord chat (on the channel that has been set)

    await bot.process_commands(message) #In this way, the bot will read the received message and determine the appropriate action to be taken based on the commands or keywords contained in the message.

bot.run("YOUR_TOKEN") #CHANGE TO YOUR TOKEN

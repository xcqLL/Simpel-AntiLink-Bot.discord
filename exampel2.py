import discord
from discord.ext import commands

# Set up intents 
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if any(url in message.content for url in ["http://", "https://"]):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Please do not send links")
    
    await bot.process_commands(message)

bot.run("YOUR_TOKEN") #CHANGE TO YOUR TOKEN
 

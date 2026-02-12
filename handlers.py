# Example Command Handlers

from discord.ext import commands

# Create bot instance
bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! How can I help you?')

@bot.command()
async def help(ctx):
    help_text = "Available commands:\n!ping - Responds with Pong!\n!hello - Greets the user!" 
    await ctx.send(help_text)
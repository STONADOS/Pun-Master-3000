import discord
from discord.ext import commands
import Joking
import math
import random  
import praw
import asyncpraw
from random import choice
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = discord.Intents.all()

client = commands.Bot(command_prefix='.', intents=intents)

# Error handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command does not exist.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("An error occurred while invoking the command.")
    else:
        await ctx.send("An unexpected error occurred.")
    logger.error(f"An error occurred: {error}")


@client.event
async def on_ready():
    print(f"{__name__} is now ready!")
    print("~~~~~~~~~~~~")

#RANDOM JOKES

@client.command()
async def joke(ctx):
    b = str(Joking.random_joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Random Laughter",
        description=a,
        color=discord.Color.dark_gray()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed)

@client.command()
async def jokes(ctx):
    b = str(Joking.random_joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Random Laughter",
        description=a,
        color=discord.Color.dark_gray()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

#DAD JOKES

@client.command()
async def dad(ctx):
    b = str(Joking.random_dad_joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Hey Orphan :) ",
        description=a,
        color=discord.Color.dark_blue()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

@client.command()
async def dadjoke(ctx):
    b = str(Joking.random_dad_joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Hey Orphan :) ",
        description=a,
        color=discord.Color.dark_blue()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

#KNOCK KNOCK JOKES

@client.command()
async def knock(ctx):
    b = str(Joking.Random_knock_knock_joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Knock Knock Jokes",
        description=a,
        color=discord.Color.pink()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

@client.command()
async def knockknock(ctx):
    b = str(Joking.Random_knock_knock_joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Knock Knock Jokes",
        description=a,
        color=discord.Color.pink()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

@client.command()
async def knockknockjoke(ctx):
    b = str(Joking.Random_knock_knock_joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Knock Knock Jokes",
        description=a,
        color=discord.Color.pink()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)
 
#MAMA JOKES

@client.command()
async def mama(ctx):
    b = str(Joking.yo_mama_joke_slash_insults())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Mommy Jokes ;) ",
        description=a,
        color=discord.Color.dark_magenta()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

@client.command()
async def mamajoke(ctx):
    b = str(Joking.yo_mama_joke_slash_insults())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Mommy Jokes ;) ",
        description=a,
        color=discord.Color.dark_magenta()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

@client.command()
async def momajoke(ctx):
    b = str(Joking.yo_mama_joke_slash_insults())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Mommy Jokes ;) ",
        description=a,
        color=discord.Color.dark_magenta()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

@client.command()
async def moma(ctx):
    b = str(Joking.yo_mama_joke_slash_insults())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Mommy Jokes ;) ",
        description=a,
        color=discord.Color.dark_magenta()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

#CHUCK NORRIS

@client.command()
async def cn(ctx):
    b = str(Joking.chuck_norris_jokes())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Chuck Norris Jokes (Idk Who he Even Is) ",
        description=a,
        color=discord.Color.dark_red()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

#PUNS

@client.command()
async def pun(ctx):
    b = str(Joking.Pun())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Exclusives ★",
        description=a,
        color=discord.Color.dark_theme()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

#DARK JOKES

@client.command()
async def dark(ctx):
    b = str(Joking.DarkJoke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Negro Jokes",
        description=a,
        color=discord.Color.dark_gray()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

@client.command()
async def darkjoke(ctx):
    b = str(Joking.DarkJoke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="Negro Jokes",
        description=a,
        color=discord.Color.dark_gray()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer,)
    await ctx.send(embed=embed,)

#IRONY JOKES

@client.command()
async def irony(ctx):
    b = str(Joking.Irony_Joke())
    a = b + "\n"
    
    embed = discord.Embed(
        title="What In The Irony Is This ??",
        description=a,
        color=discord.Color.dark_purple()
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

#ANIMAL JOKES

@client.command()
async def animaljoke(ctx):
    b = str(Joking.animal_joke())
    a = b + "\n"
    embed = discord.Embed(
        title="Animal Joke (Sighs...)",
        description=a,
        color=discord.Color.green()  # choose any color you like
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@client.command()
async def animal(ctx):
    b = str(Joking.animal_joke())
    a = b + "\n"
    embed = discord.Embed(
        title="Animal Joke (Sighs...)",
        description=a,
        color=discord.Color.green()  # choose any color you like
    )
    footer="\"If You Get Offended \n-English Or Spanish\""
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)


@client.command()
async def meme(ctx):
    reddit = praw.Reddit(client_id = 'CLIENT ID', 
                    client_secret = 'CLIENT SECRET', 
                    user_agent = 'USER AGENT')
    
    streams = ['SERVER1', 'SERVER2', 'SERVER3', 'SERVER4']

    stream = str(streams[random.randint(0,4)])
    
    subreddit = reddit.subreddit(stream).hot()
    post_pick = random.randint(1,100)
    for i in range(0, post_pick):
        final = next(x for x in subreddit if not x.stickied)
        logger.info(final.url)

    await ctx.send(final.url)


client.run('CLIENT')

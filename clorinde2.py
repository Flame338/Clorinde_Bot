import discord
import scraper
from dotenv import load_dotenv
from discord.ext import commands
import os

async def send_message() -> str:
    try:
        response = responses.get_response()
        return response
        
    except Exception as e:
        print(e)

def run_discord_bot():
    command_names = ['$button', '$codes', '$crystals', '$help', '$primo', '$roll', '$stellar']
    command_values = ['Pings the bot',
                      'Lists codes for premium currency in gacha games.',
                      'Lists available codes for HI3rd',
                      'List all of the commands',
                      'Lists available codes for Genshin Impact',
                      'Rolls a d6 die.',
                      'Lists available codes for Star Rail']

    games = ['Genshin Impact', 'Honkai Impact 3rd', 'Honkai Star Rail']
    #url = 'https://pbs.twimg.com/media/F0bCqS5WIAEOkzK?format=jpg&name=large'
    url = 'https://media.tenor.com/p8nqebseDYEAAAAC/clorinde-genshin-impact.gif'

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="$", intents=intents)
    bot.remove_command('help')

    @bot.event
    async def on_ready():
        print(f'{bot.user} is running')

    @bot.command()
    async def button(ctx):
        await ctx.send("Hello!")

    @bot.command()
    async def help(ctx):
        embed = discord.Embed(
            title='Bot Commands',
            description='Welcome to the help section. These are all the commands.',
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=url)
        for idx in range(0,len(command_names)):
            embed.add_field(
                name=command_names[idx],
                value=command_values[idx],
                inline=False
            )

        await ctx.send(embed=embed)

    @bot.command()
    async def primos(ctx):
        embed = discord.Embed(
            title="Available Genshin Codes",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=url)
        code_value = scraper.genshin_scrape()
        embed.add_field(
            name=games[0],
            value=code_value,
            inline=False
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def stellar(ctx):
        embed = discord.Embed(
            title="Available HSR Codes",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=url)
        code_value = scraper.star_scrape()
        embed.add_field(
            name=games[2],
            value=code_value,
            inline=False
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def crystals(ctx):
        embed = discord.Embed(
            title="Available Genshin Codes",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=url)
        code_value = scraper.HI3_scrape()
        embed.add_field(
            name=games[1],
            value=code_value,
            inline=False
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def codes(ctx):
        embed = discord.Embed(
            title='Game Codes',
            description='Shows codes for premium currency in gacha games.',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=url)

        code_value = ''
        for idx in range(0,len(games)):
            if games[idx] == 'Genshin Impact':
                code_value = scraper.genshin_scrape()
            elif games[idx] == 'Honkai Impact 3rd':
                code_value = scraper.HI3_scrape()
            else:
                code_value = scraper.star_scrape()

            embed.add_field(
                name=games[idx],
                value=code_value,
                inline=False
            )

        await ctx.send(embed=embed)

    async def roll(ctx):
        embed = discord.Embed(
            title='Dice Roll',
            description='Rolls a d6 die',
            color=discord.Color.blue()
        )

    load_dotenv('.env')
    bot.run(os.getenv('TOKEN'))


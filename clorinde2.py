import discord
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive
from random import random
from replit import db
import os


def run_discord_bot():
  command_names = [
    '$addCodes', '$button', '$codes', '$crystals', '$help', '$primos', '$roll',
    '$stellar'
  ]

  command_values = [
    'Asks user input to insert codes (GI, HSR, HI3)', 'Pings the bot',
    'Lists codes for premium currency in gacha games.',
    'Lists available codes for HI3rd', 'List all of the commands',
    'Lists available codes for Genshin Impact', 'Rolls a d6 die.',
    'Lists available codes for Star Rail'
  ]

  games = ['Genshin Impact', 'Honkai Impact 3rd', 'Honkai Star Rail']

  url = [
    'https://i.pinimg.com/originals/99/d4/3b/99d43befb3df2d6293974cfc7313d7e0.gif',
    'https://cdn.discordapp.com/attachments/551083776479068170/1147829701126127626/download.gif',
    'https://cdn.discordapp.com/attachments/551083776479068170/1147830028407672892/ganyu_wallpaper_by_snkochan_deeeeaf-fullview.png',
    'https://cdn.discordapp.com/attachments/551083776479068170/1147831268218781776/ganyu-genshin-impact.gif',
    'https://cdn.discordapp.com/attachments/551083776479068170/1147831412326678578/ganyu.gif'
  ]

  primo_codes = set()
  crystal_codes = set()
  stellar_codes = set()

  intents = discord.Intents.default()
  intents.message_content = True

  bot = commands.Bot(command_prefix="$", intents=intents)
  bot.remove_command('help')

  @bot.event
  async def on_ready():
    print(f'{bot.user} is running')

  @bot.command()
  async def addCode(ctx, what='default', *why):
    what = str(what)
    why = str(why)
    match what:
      case 'HI3':
        if what in db.keys():
          if why in db.get('HI3'):
            await ctx.send(f'{why} already exists in the databse')
          else:
            data = db[what]
            data.append(why)
            db[what] = data
        else:
          db[what] = [why]

      case 'GI':
        if what in db.keys():
          if why in db.get(what):
            await ctx.send(f'{why} already exists in the databse')
          else:
            data = db[what]
            data.append(why)
            db[what] = data
        else:
          db[what] = [why]

      case 'HSR':
        if what in db.keys():
          if why in db.get('HSR'):
            await ctx.send(f'{why} already exists in the databse')
          else:
            data = db[what]
            data.append(why)
            db[what] = data
        else:
          db[what] = [why]

      case 'default':
        await ctx.send('Invalid or missing game or code arguements')

  @bot.command()
  async def button(ctx):
    await ctx.send("I'm still eepy...")

  @bot.command()
  async def help(ctx):
    embed = discord.Embed(
      title='Bot Commands',
      description='Welcome to the help section. These are all the commands.',
      color=discord.Color.blue())

    embed.set_thumbnail(url=url[int((random() * 10)) % len(url)])
    for idx in range(0, len(command_names)):
      embed.add_field(name=command_names[idx],
                      value=command_values[idx],
                      inline=False)

    await ctx.send(embed=embed)

  @bot.command()
  async def primos(ctx, what=primo_codes):
    embed = discord.Embed(title="Available Genshin Codes",
                          color=discord.Color.blue())

    embed.set_thumbnail(url=url[int((random() * 10)) % len(url)])

    code_value = db['GI']

    embed.add_field(name='Genshin Impact', value=code_value, inline=False)
    await ctx.send(embed=embed)

  @bot.command()
  async def stellar(ctx, what=stellar_codes):
    embed = discord.Embed(title="Available HSR Codes",
                          color=discord.Color.blue())

    embed.set_thumbnail(url=url[int((random() * 10)) % len(url)])

    code_value = db['HSR']

    embed.add_field(name='Honkai Star Rail', value=code_value, inline=False)
    await ctx.send(embed=embed)

  @bot.command()
  async def crystals(ctx, what=crystal_codes):
    embed = discord.Embed(title="Available HI3rd Codes",
                          color=discord.Color.blue())

    embed.set_thumbnail(url=url[int((random() * 10)) % len(url)])

    code_value = db['HI3']

    embed.add_field(name='Honkai Impact 3rd', value=code_value, inline=False)
    await ctx.send(embed=embed)

  @bot.command()
  async def codes(ctx):
    embed = discord.Embed(
      title='Game Codes',
      description='Shows codes for premium currency in gacha games.',
      color=discord.Color.blue())

    embed.set_thumbnail(url=url[int((random() * 10)) % len(url)])

    code_value = ''
    for idx in range(0, len(games)):
      if games[idx] == 'Genshin Impact':
        for i in primo_codes:
          code_value += str(i) + '\n'
      elif games[idx] == 'Honkai Impact 3rd':
        for i in crystal_codes:
          code_value += str(i) + '\n'
      else:
        for i in stellar_codes:
          code_value += str(i) + '\n'

      embed.add_field(name=games[idx], value=code_value, inline=False)

    await ctx.send(embed=embed)

  @bot.command()
  async def roll(ctx):
    embed = discord.Embed(title='Dice Roll',
                          description='Rolls a d6 die',
                          color=discord.Color.blue())

    embed.add_field(value=int((random() * 10)) % 3)
    embed.set_thumbnail(url=url[int((random() * 10)) % len(url)])
    await ctx.send(embed=embed)

  load_dotenv('.env')
  keep_alive()
  bot.run(os.getenv('TOKEN'))

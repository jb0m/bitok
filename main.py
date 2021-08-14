import discord
from discord.ext import commands
from config import settings
import random
bot = commands.Bot(command_prefix = settings['prefix'])
@bot.command() 
async def hello(ctx): 
    await ctx.send(f'Привет, {ctx.message.author.mention}!')
@bot.command()
async def gvn(ctx, num1, num2):
	x = int(num1)
	y = int(num2)
	value = random.randint(min(x,y), max(x,y))
	await ctx.send(f"{ctx.message.author.mention}, вы получили число {value}.")
@bot.command()
async def гвн(ctx, num1, num2):
	x = int(num1)
	y = int(num2)
	value = random.randint(min(x,y), max(x,y))
	await ctx.send(f"{ctx.message.author.mention}, вы получили число {value}.")
@bot.command()
async def rl(ctx, num):
	x = int(num)
	lst = list(range(1, x+1))
	random.shuffle(lst)
	value = ''
	for i in lst:
		value = value + str(i) + ', '
	await ctx.send(f'{value} {ctx.message.author.mention}.')
@bot.command()
async def рл(ctx, num):
	x = int(num)
	lst = list(range(1, x+1))
	random.shuffle(lst)
	value = ''
	for i in lst:
		value = value + str(i) + ', '
	await ctx.send(f'{value} {ctx.message.author.mention}.')
@bot.command()
async def rns(ctx, amount, num1, num2):
	x = int(amount)
	y = int(num1)
	z = int(num2)
	value = ''
	while x != 0:
		value += str(random.randint(min(y,z), max(y,z))) + ', '
		x = x - 1
	await ctx.send(f'{value} {ctx.message.author.mention}.')
@bot.command()
async def рнс(ctx, amount, num1, num2):
	x = int(amount)
	y = int(num1)
	z = int(num2)
	value = ''
	while x != 0:
		value += str(random.randint(min(y,z), max(y,z))) + ', '
		x = x - 1
	await ctx.send(f'{value} {ctx.message.author.mention}.')
@bot.command()
async def helpme(ctx):
	await ctx.send(f'{ctx.message.author.mention}, вот список команд: \n рл (rl) [число] - перемешанный список, в котором число означает лимит списка, и кол-во элементов списка \n gvn (гвн) [число1, число2] - рандомное число в промежутке число1-число2 \n rns (рнс) [кол-во чисел, число1, число2] - генератор случайных чисел в промежутке число1-число2 ')
@bot.command()
async def помощь(ctx):
	await ctx.send(f'{ctx.message.author.mention}, вот список команд: \n рл (rl) [число] - перемешанный список, в котором число означает лимит списка, и кол-во элементов списка \n gvn (гвн) [число1, число2] - рандомное число в промежутке число1-число2 \n rns (рнс) [кол-во чисел, число1, число2] - генератор случайных чисел в промежутке число1-число2 ')
bot.run(settings['token'])
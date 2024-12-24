import discord
from discord.ext import commands
from config import settings

# Создаем переменные, значение которых находится в файле конфига.
TOKEN = settings['TOKEN']
PREFIX = settings['PREFIX']
ROLE = settings['ROLE']

# Создаем права боту
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


# Создаем команду, которая при в воде будет выводить сообщение
@bot.command()
async def hello(ctx):
    await ctx.reply("Привет :)")


# Бот назначает роль новому участнику сервера
@bot.event
async def on_member_join(member):
    join_role = discord.utils.get(member.guild.roles, name=ROLE)
    await member.add_roles(join_role)


bot.run(TOKEN)

import discord
from discord.ext import commands

TOKEN = 'MTMyMDY1MDk0NDc2OTI5ODQ3Mg.Gzjufo.d4CIc4inUrATBJQbw29uH3JfESIJ_f0UCMv7Fw'

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен и готов к работе!')


@bot.command()
async def hello(ctx):
    await ctx.send('Привет! Я ваш Discord бот.')


@bot.event
async def on_member_join(member):
    role = await discord.utils.get(guild_id=member.guild.id, role_id = 1320580912978726923)

    await member.add_roles(role)



bot.run(TOKEN)

import discord
from discord.ext import commands
from config import settings

TOKEN = settings['TOKEN']
PREFIX = settings['PREFIX']
ROLE = settings['ROLE']
intents = discord.Intents().all()


bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.reply("Привет :)")


@bot.event
async def on_member_join(member):
    join_role = discord.utils.get(member.guild.roles, name=ROLE)
    await member.add_roles(join_role)


bot.run(TOKEN)

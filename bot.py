import discord
from discord.ext import commands

TOKEN = 'MTMyMDgwMTgxMzA5NTY0NTI0NA.GCwlxp.lxWclBNYgBAhqJPH8cvLX-9KN0kWegNINWFhL0'
PREFIX = '/'
intents = discord.Intents().all()
ROLE_ID = 1320807509635895378

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.reply("hello")
    await ctx.send('hello2 ')


@bot.event
async def on_member_join(member):
    guild = member.quild
    role = guild.get_role(ROLE_ID)

    if role:
        try:
            await member.add_roles(role)
            print(f'Выдана роль {role.name} пользователю {member.name}')
        except discord.Forbidden:
            print(f'Недостаточно прав для выдачи роли {role.name}')
        except discord.HTTPException:
            print(f'Не удалось выдать роль {role.name} пользователю {member.name}')


bot.run(TOKEN)

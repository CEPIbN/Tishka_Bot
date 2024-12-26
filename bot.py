import discord
from discord.ext import commands
from config import settings
import youtube_dl

# Создаем переменные, значение которых находится в файле конфига.
TOKEN = settings['TOKEN']
PREFIX = settings['PREFIX']
ROLE = settings['ROLE']

ytdl_format_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'restrictfilenames': True,
    'noplaylist': True,
    'quiet': False,
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

# Создаем права боту
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} успешно запущен!')


# Создаем команду, которая при в воде будет выводить сообщение
@bot.command()
async def hello(ctx):
    await ctx.reply("Привет :)")


# Бот назначает роль новому участнику сервера
@bot.event
async def on_member_join(member):
    join_role = discord.utils.get(member.guild.roles, name=ROLE)
    await member.add_roles(join_role)


@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Вы должны находиться в голосовом канале!")


@bot.command()
async def leave(ctx):
    if ctx.voice.client:
        await ctx.voice.client.disconnect()
    else:
        await ctx.send("Я не в голосовом канале!")


@bot.command()
async def play(ctx, *, url):
    voice_client = ctx.voice_client

    if not voice_client:
        await ctx.send("Сначала подключитесь к голосовому каналу с помощью команды !join")
        return

    async with ctx.typing():
        info = ytdl.extract_info(url, download=False)
        url = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(url, **ffmpeg_options))

    await ctx.send(f"Сейчас играет: {info['title']}")


@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.send("Музыка остановлена.")
    else:
        await ctx.send("Ничего не играет.")


bot.run(TOKEN)

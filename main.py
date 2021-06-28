from discord.ext.commands.converter import VoiceChannelConverter
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

token = "ODU5MDMwMDgxMTIwMzcwNjg5.YNmwGw.BFKJu3dEKRS3haIKnnsezHpnB9s"

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    game = discord.Game('봇이 활동중에 표시 될 이름')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(embed = discord.Embed(title = '따라하기', description = text, color = 0x00ff00))

@bot.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 유저가 접속해있지 않네요..")

@bot.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("이미 그 채널에 속해있지 않아요.")

bot.run(token)
import discord
import youtube_dl

intents = discord.Intents.default()
client = discord.Client(intents=intents)

token = "ODU5MDMwMDgxMTIwMzcwNjg5.YNmwGw.smF05bVG4XJ9MGI0oXZNq3TefIE"

## 로그인
@client.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(client.user.name)
    game = discord.Game('봇이 활동중에 표시 될 이름')
    await client.change_presence(status=discord.Status.online, activity=None)

@client.event
async def on_message(message):

    ## !따라하기 <text>
    if message.content.startswith("!따라하기"):
        text = message.content.split(" ")[1]
        await message.channel.send(embed = discord.Embed(title = '따라하기', description = text, color = 0x00ff00))

    ## !입장
    if message.content.startswith("!입장"):
        try:
            global vc
            vc = await message.author.voice.channel.connect()
            await message.channel.send("보이스채널에 입장합니다.")
        except:
            try:
                await vc.move_to(message.author.voice.channel)
            except:
                await message.channel.send("채널에 유저가 접속해있지 않네요..")

    ## !퇴장
    if message.content.startswith("!퇴장"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        try:
            await voice.disconnect()
            await message.channel.send("보이스채널에서 퇴장합니다.")
        except:
            await message.channel.send("이미 그 채널에 속해있지 않아요.")

    ## !재생 <url>
    if message.content.startswith("!재생"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        
        url = message.content.split(" ")[1]
        option = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        with youtube_dl.YoutubeDL(option) as ydl:
            info = ydl.extract_info(url, download=False)
            mTitle = info['title']
            mUrl = info['formats'][0]['url']
        
        voice.play(discord.FFmpegPCMAudio(mUrl, **FFMPEG_OPTIONS))
        await message.channel.send(mTitle + "을 재생합니다.")


client.run(token)
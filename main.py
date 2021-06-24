import discord
from discord.ext import commands
import youtube_dl
import datetime
import lazy_queue as lq

settings = {
    'token': input('Please, enter bot-token to start\n(For permanent use \
better to save token in PATH):\n'),
    'bot': '🤘Панк🤘',
    'id': 825365074850873424,
    'prefix': '+'}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'}

YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'noplaylist': True,
    'simulate': 'True',
    'preferredquality': '192',
    'preferredcodec': 'mp3',
    'key': 'FFmpegExtractAudio'}

bot = commands.Bot(command_prefix=settings['prefix'])
bot.remove_command("help")
songs_queue = lq.Queue()
loop_flag = False


@bot.event
async def on_ready():
    print('Status: online')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name='советы пьяного бомжа'))


@bot.command(aliases=['Ping', 'PING', 'Пинг', 'ПИНГ', 'зштп', 'ЗШТП', 'Зштп',
                      'пинг'])
async def ping(ctx):
    await ctx.message.reply(f'С похмелья: {round(bot.latency*1000)}ms 🧠')

#########################[JOIN BLOCK]#########################

@bot.command(aliases=['j', 'J', 'jn', 'JN','Jn', 'о', 'О', 'от', 'ОТ', 'От',
                      'сюда', 'СЮДА', 'Сюда', 'присоединись', 'ПРИСОЕДИНИСЬ',
                      'Присоединись', 'Присоединиться', 'ПРИСОЕДИНИТЬСЯ',
                      'присоединиться', 'ощшт', 'Ощшт', 'ОЩШТ', 'Join', 'JOIN'])
async def join(ctx):
    if ctx.message.author.voice:
        if not ctx.voice_client:
            await ctx.message.author.voice.channel.connect(reconnect=True)
        else:
            await ctx.voice_client.move_to(ctx.message.author.voice.channel)
    else:
        await ctx.message.reply('❗ Вы должны находиться в голосовом канале ❗')


@bot.command(aliases=['Disconnect', 'DISCONNECT', 'DC', 'dc', 'Dc', 'Disc',
                      'disc', 'DISC', 'leave', 'Leave', 'LEAVE', 'Дисконнект',
                      'ДИСКОННЕКТ', 'дисконнект', 'откл', 'ОТКЛ', 'Откл',
                      'отключись', 'ОТКЛЮЧИСЬ', 'Отключись', 'отключиться',
                      'ОТКЛЮЧИТЬСЯ', 'Отключиться', 'вшысщттусе', 'Вшысщттусе',
                      'ВШЫСЩТТУСЕ', 'ВС', 'вс', 'Вс', 'Вшыс', 'вшыс', 'ВШЫС',
                      'дуфму', 'Дуфму', 'ДУФМУ', 'Выйди', 'ВЫЙДИ', 'выйди',
                      'кыш', 'КЫШ', 'Кыш', 'уйди', 'Уйди', 'УЙДИ', 'd', 'в'])
async def disconnect(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.message.reply(f'🍺 Ушёл в запой вместе с \
{ctx.message.author.mention} 🍺')
    else:
        await ctx.message.reply('Вы попытались разбудить бота,\
 но он в отключке 💤')

#########################[PLAY MUSIC BLOCK]#########################

@bot.command()
async def add(ctx, *url):
    url = ' '.join(url)
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except:
            info = ydl.extract_info(f"ytsearch:{url}",
                                    download=False)['entries'][0]

    URL = info['formats'][0]['url']
    name = info['title']
    time = str(datetime.timedelta(seconds=info['duration']))
    songs_queue.q_add([name, time, URL])
    embed = discord.Embed(description=f'Записываю [{name}]({url}) в очередь 📝',
                          colour=discord.Colour.red())
    await ctx.message.reply(embed=embed)


def step_and_remove(voice_client):
    if loop_flag:
        songs_queue.q_add(songs_queue.get_value()[0])
    songs_queue.q_remove()
    audio_player_task(voice_client)


def audio_player_task(voice_client):
    if not voice_client.is_playing() and songs_queue.get_value():
        voice_client.play(discord.FFmpegPCMAudio(
                                  executable="ffmpeg\\bin\\ffmpeg.exe",
                                  source=songs_queue.get_value()[0][2],
                                  **FFMPEG_OPTIONS),
                                  after=lambda e: step_and_remove(voice_client))


@bot.command(aliases=['Play', 'PLAY', 'играй', 'ИГРАЙ', 'Играй', 'сыграй',
                      'Сыграй', 'СЫГРАЙ', 'здфн', 'Здфн', 'ЗДФН', 'p', 'P',
                      'pl', 'PL', 'Pl', 'з', 'З', 'зд', 'ЗД', 'Зд', 'Плей',
                      'ПЛЕЙ', 'плей'])
async def play(ctx, *url):
    await join(ctx)
    await add(ctx, ' '.join(url))
    await ctx.message.add_reaction(emoji='🎸')
    voice_client = ctx.guild.voice_client
    audio_player_task(voice_client)


@bot.command()
async def loop(ctx):
    global loop_flag
    loop_flag = True
    await ctx.message.reply('Залуплено')


@bot.command()
async def unloop(ctx):
    global loop_flag
    loop_flag = False
    await ctx.message.reply('Отлуплено')


@bot.command(aliases=['Queue', 'QUEUE', 'йгугу', 'Йгугу', 'ЙГУГУ', 'очередь',
                      'Очередь', 'ОЧЕРЕДЬ', 'список', 'Список', 'СПИСОК',
                      'list', 'List', 'LIST', 'дшые', 'Дшые', 'ДШЫЕ', 'Лист',
                      'лист', 'ЛИСТ', 'песни', 'Песни', 'ПЕСНИ', 'songs',
                      'Songs', 'SONGS', 'ыщтпы', 'ЫЩТПЫ', 'Ыщтпы', 'q'])
async def queue(ctx):
    if len(songs_queue.get_value()) > 0:
        only_names_and_time_queue = []
        for i in songs_queue.get_value():
            name = i[0]
            if len(i[0]) > 30:
                name = i[0][:30] + '...'
            only_names_and_time_queue.append(f'📀 `{name:<33}   {i[1]:>20}`\n')
        c = 0
        queue_of_queues = []
        while c < len(only_names_and_time_queue):
            queue_of_queues.append(only_names_and_time_queue[c:c + 10])
            c += 10

        embed = discord.Embed(title=f'ОЧЕРЕДЬ [LOOP: {loop_flag}]',
                              description=''.join(queue_of_queues[0]),
                              colour=discord.Colour.red())
        await ctx.send(embed=embed)

        for i in range(1, len(queue_of_queues)):
            embed = discord.Embed(description=''.join(queue_of_queues[i]),
                                  colour=discord.Colour.red())
            await ctx.send(embed=embed)
    else:
        await ctx.send('Очередь пуста 📄')


@bot.command(aliases=['ps', 'wait', 'wt', 'stop', 'стоп', 'пауза'])
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice:
        voice.pause()
        await ctx.message.reply('Шо ты сделал? Порвал струну. Без неё играй!')


@bot.command(aliases=['rs', 'continue', 'cnt', 'ct', 'продолжить'])
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice:
        if voice.is_paused():
            voice.resume()
            await ctx.message.reply('Поменял струну.')


@bot.command(aliases=['sk', 'next', 'следующая', 'скип', 'скипнуть'])
async def skip(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice:
        voice.stop()


@bot.command(aliases=['cl', 'очистить', 'c'])
async def clear(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice:
            voice.stop()
            while not songs_queue.is_empty():
                songs_queue.q_remove()


@bot.command(aliases=['rem', 'r', 'удалить'])
async def remove(ctx, index):
    try:
        if len(songs_queue.get_value()) > 0:
            index = int(index) - 1
            if index >= 0:
                d = songs_queue.q_rem_by_index(index)[0]
                await ctx.message.reply(f'Вычеркнул из списка: {d}')
        else:
            await ctx.message.reply('Нечего удалять')
    except:
        await ctx.message.reply(f'Песни с таким индексом не существует')

bot.run(settings['token'])

# 🤘 Discord Music Bot 🤘
## _This is music bot for Discord in Python_
## 📋 Requirments 📋
To build this project you need:
1) [Python 3](https://www.python.org/downloads/)
2) Libraries:
    * [discord.py](https://pypi.org/project/discord.py/)
    * [youtube_dl](https://pypi.org/project/youtube_dl/)
    * [PyNaCl](https://pypi.org/project/PyNaCl/)
3) [FFmpeg](https://www.ffmpeg.org/)
4) Discord bot token:
    * You can create your bot here: https://discord.com/developers/docs/intro
    * For first launch you can enter token from stdin, but would be better if you will read token from your $PATH
## 🚀 Getting Started 🚀
If you are Windows user:
1) Download FFmpeg from oficial site: https://www.ffmpeg.org/
2) Put FFmpeg directory near [main.py](https://github.com/LeovanGit/Discord-music-bot/blob/master/main.py) and execute [main.py](https://github.com/LeovanGit/Discord-music-bot/blob/master/main.py).

If you are GNU/Linux user:
```
git clone https://github.com/LeovanGit/Discord-music-bot
cd Discord-music-bot
```
Install FFmpeg:
```
git clone https://git.ffmpeg.org/ffmpeg.git
```
Then change [main.py](https://github.com/LeovanGit/Discord-music-bot/blob/master/main.py): executable = 'path to FFmpeg executable'
![code_image](https://i.ibb.co/GtTMndV/123.png)
```
python main.py
```

## ⚙ Features & Commands ⚙
Default prefix is +, but you can change it in [main.py](https://github.com/LeovanGit/Discord-music-bot/blob/master/main.py).

| Command | Description | Synonyms |
| ------ | ------ | ------ |
| help | shows avaivable commands |  |
| ping | shows ping | Ping, PING, Пинг, ПИНГ, зштп, ЗШТП, Зштп, пинг |
| join | join to channel | j, J, jn, JN,Jn, о, О, от, ОТ, От, сюда, СЮДА, Сюда, присоединись, ПРИСОЕДИНИСЬ, Присоединись, Присоединиться, ПРИСОЕДИНИТЬСЯ, присоединиться, ощшт, Ощшт, ОЩШТ, Join, JOIN |
| disconnect | disconnect from this channel | Disconnect, DISCONNECT, DC, dc, Dc, Disc, disc, DISC, leave, Leave, LEAVE, Дисконнект, ДИСКОННЕКТ, дисконнект, откл, ОТКЛ, Откл, отключись, ОТКЛЮЧИСЬ, Отключись, отключиться, ОТКЛЮЧИТЬСЯ, Отключиться, вшысщттусе, Вшысщттусе, ВШЫСЩТТУСЕ, ВС, вс, Вс, Вшыс, вшыс, ВШЫС, дуфму, Дуфму, ДУФМУ, Выйди, ВЫЙДИ, выйди, кыш, КЫШ, Кыш, уйди, Уйди, УЙДИ, d, в |
| add | add song to queue (via url\name), don't support playlists  | 
| play | play song (uses add) | Play, PLAY, играй, ИГРАЙ, Играй, сыграй, Сыграй, СЫГРАЙ, здфн, Здфн, ЗДФН, p, P, pl, PL, Pl, з, З, зд, ЗД, Зд, Плей, ПЛЕЙ, плей |
| queue | shows queue | Queue, QUEUE, йгугу, Йгугу, ЙГУГУ, очередь, Очередь, ОЧЕРЕДЬ, список, Список, СПИСОК, list, List, LIST, дшые, Дшые, ДШЫЕ, Лист, лист, ЛИСТ, песни, Песни, ПЕСНИ, songs, Songs, SONGS, ыщтпы, ЫЩТПЫ, Ыщтпы, q |
| loop | loop queue |  |
| unloop | unloop queue |  |
| pause | pause song | ps, wait, wt, stop, стоп, пауза |
| resume | resume song | rs, continue, cnt, ct, продолжить |
| skip | skip song | sk, next, следующая, скип, скипнуть |
| remove | remove song from queue by index | rem, r, удалить |
| clear | clear queue | cl, очистить, c |

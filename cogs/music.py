import nextcord
import nextcord
from nextcord.ext import commands
import youtube_dl


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(965182719397093376)
        vc = await channel.connect()
        ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        ydl_options = {'format': 'bestaudio/best'}
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(
                'https://www.youtube.com/watch?v=5qap5aO4i9A', download=False)
            songTitle = info.get('title', None)
            uri = info['formats'][0]['url']
            source = await nextcord.FFmpegOpusAudio.from_probe(uri, **ffmpeg_options)
            vc.play(source)
            await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=songTitle))


def setup(bot):
    bot.add_cog(music(bot))

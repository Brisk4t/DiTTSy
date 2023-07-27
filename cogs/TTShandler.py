from TTS.api import TTS
from discord.ext import commands
from elevenlabs import generate, play


def tts(text):
     audio=generate(text=text, voice="Brisk4t1")
    
class TTShandler(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tts(self, ctx, *, message):
        





def setup(bot):
	bot.add_cog(TTShandler(bot))
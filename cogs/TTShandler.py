from TTS.api import TTS
from discord.ext import commands

class TTShandler(bot):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tts(self, ctx, *, message):
        






def setup(bot):
	bot.add_cog(TTShandler(bot))
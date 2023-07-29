from TTS.api import TTS
from discord.ext import commands
from elevenlabs import generate, play
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class TextToSpeech():

    def __init__(self):
        self.chunk_size=1024
        self.url="https://api.elevenlabs.io/v1/text-to-speech/4TjmYjtAIfowLPsW3bRf/"
        self.headers=headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": os.getenv('ELEVEN_API_KEY')
        }

    async def join(self, ctx):
        if not ctx.message.author.voice: # if the message author is not in a voice channel
            await ctx.message.delete()
            await ctx.send("Please connect to a voice channel.", delete_after=5)
            return
        
        elif not ctx.guild.voice_client in self.bot.voice_clients: # if the bot is not connected
            await ctx.message.author.voice.channel.connect() # connect to the same channel as author
            
        return
    

    async def ttsgen(self, ctx, text):
        await self.join(ctx)


        voice_channel = ctx.message.guild.voice_client



        data = {
            "text": text,
            "model_id": "eleven_multilingual_v1",
            "voice_settings": {
                "stability": 0.4,
                "similarity_boost": 1
            }
        }

        response = requests.post(url, json=data, headers=self.headers)
        with open('output.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

        voice_channel.play(audio)
    
    
class TTShandler(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tts(self, ctx, *, message):
         await(TextToSpeech.ttsgen(ctx, message))
        





async def setup(bot):
    await bot.add_cog(TTShandler(bot))
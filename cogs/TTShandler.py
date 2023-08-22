from discord.ext import commands
import discord
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv
import os

load_dotenv()


set_api_key(os.getenv("ELEVEN_API_KEY"))

class TextToSpeech():

    def __init__(self, bot):
        print("Initialized TTS Class")
        self.bot = bot

    async def join(self, ctx):
        if not ctx.message.author.voice: # if the message author is not in a voice channel
            await ctx.message.delete()
            await ctx.send("Please connect to a voice channel.", delete_after=5)
            return
        
        elif not ctx.guild.voice_client in self.bot.voice_clients: # if the bot is not connected
            await ctx.message.author.voice.channel.connect() # connect to the same channel as author
            
        return
    

    async def ttsgen(self, ctx, text):
        print(text)
        await self.join(ctx)

        voice_channel = ctx.message.guild.voice_client

        audio = generate(
            text=text,
            voice="Brisk4t1",
            model='eleven_multilingual_v2',
            )

        # with open('output.mp3', 'wb') as f:
        #     for chunk in response.iter_content(chunk_size=self.chunk_size):
        #         if chunk:
        #             f.write(chunk)

        save(audio, "output.mp3")

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("output.mp3"))
        voice_channel.play(source)
    
    
class TTShandler(commands.Cog):
	
    def __init__(self, bot):
        print("Initialized TTShandler")
        self.bot = bot
        self.ttsclass = TextToSpeech(bot)

    @commands.command()
    async def tts(self, ctx, *, message):
        print("tts command received") 
        await(self.ttsclass.ttsgen(ctx, message))
        


async def setup(bot):
    print("Loaded")
    await bot.add_cog(TTShandler(bot))

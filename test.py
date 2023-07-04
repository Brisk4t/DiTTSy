from TTS.api import TTS

model = (TTS.list_models()[0])
tts = TTS(model)

wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])s
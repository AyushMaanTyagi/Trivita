import whisper
model = whisper.load_model("base")
result = model.transcribe("voice.mp3")
print("Transcription is :\n",result["text"])
# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "dsfsdfsdfsdf"
config = aai.TranscriptionConfig(language_code="hi")
transcriber = aai.Transcriber(config=config)

# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
transcript = transcriber.transcribe("new.mp3")

# print(transcript.export_subtitles_srt())

# transcribe the audio file

# get the transcript in SRT format
srt_transcript = transcript.export_subtitles_srt()

# write the transcript to a text file
with open("7 Things Mentally Strong Men Don’t Do.srt", "w", encoding="utf-8") as file:
    file.write(srt_transcript)

print("Transcript downloaded and saved to transcript_hindi.txt")

##Rylan - calming male
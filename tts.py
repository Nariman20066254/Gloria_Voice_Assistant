from silero_tts.silero_tts import SileroTTS

tts = SileroTTS(
    language='ru',
    model_id='v4_ru',
    speaker='baya'  # 👈 допустимый голос
)

tts.tts("Радость ", "Радость .wav")
print("✅ Файл сохранён: Радость .wav")





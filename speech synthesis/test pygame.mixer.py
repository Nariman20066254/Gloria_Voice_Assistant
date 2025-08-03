import json
import pygame
from vosk import Model, KaldiRecognizer
import pyaudio
import os


model = Model('model_small')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def mus():
    q = 0
    for root, dirs, files in os.walk("музыка"):
        print(files)
        print(f'сейчас играет:{files[0]}')
        pygame.mixer.init()
        pygame.mixer.music.load(f'музыка/{files[0]}')
        pygame.mixer.music.play()
        while True:
            data = stream.read(8000)
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(rec.Result())
                if answer['text']:
                    if answer['text'] == 'далее':
                        q = q + 1
                        print(f'{q} and {len(files)}')
                        if len(files) == q:
                            q = -1
                        else:
                            pygame.mixer.music.unload()
                            pygame.mixer.music.load(f'музыка/{files[q]}')
                            pygame.mixer.music.play()
                            print(f'сейчас играет:{files[q]}')
                    elif answer['text'] == 'пауза':
                        pygame.mixer.music.pause()
                    if answer['text'] == 'продолжить':
                        pygame.mixer.music.unpause()


mus()
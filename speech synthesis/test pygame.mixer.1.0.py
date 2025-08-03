from pygame import mixer
import time
mixer.init()
a = mixer.music
a.load('музыка/5000-mp3.mp3')
a.play()
a.set_volume(0.2)
print(a.get_volume())
while True:
    print(a.get_pos())
    if a.get_pos() == 193000:
        a.stop()
        print('конец')
        break
print(123)
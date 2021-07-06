import math
import pyaudio
import time

PyAudio = pyaudio.PyAudio

BITRATE = 128000    

FREQUENCY = 1900
LENGTH = 1

def split(word):
    return [char for char in word]

def beep(detail, BITRATE):
    FREQUENCY = detail[0]
    LENGTH = detail[1]
    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY+100

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''    

    #generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

    for x in range(RESTFRAMES): 
        WAVEDATA = WAVEDATA+chr(128)

    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), 
                    channels = 1, 
                    rate = BITRATE, 
                    output = True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()

def morse(letter):
    dash = [2000, 0.3]
    dot = [2000, 0.1]
    space = [1, 0.5]

    letters = {
    "a": [dot, dash],
    "b": [dash, dot, dot, dot],
    "c": [dash, dot, dash, dot],
    "d": [dash, dot, dot],
    "e": [dot],
    "f": [dot, dot, dash, dot],
    "g": [dash, dash, dot],
    "h": [dot, dot, dot, dot],
    "i": [dot, dot],
    "j": [dot, dash, dash, dash],
    "k": [dash, dot, dash],
    "l": [dot, dash, dot, dot],
    "m": [dash, dash],
    "n": [dash, dot],
    "o": [dash, dash, dash],
    "p": [dot, dash, dash, dot],
    "q": [dash, dash, dot, dash],
    "r": [dot, dash, dot],
    "s": [dot, dot, dot],
    "t": [dot],
    "u": [dot, dot, dash],
    "v": [dot, dot, dot, dash],
    "w": [dot, dash, dash],
    "x": [dash, dot, dot, dash],
    "y": [dash, dot, dash, dash],
    "z": [dash, dash, dot, dot],
    " ": [space]
    }

    for key, value in letters.items():
        if key == letter:
            if letter == " ":
                print("Playing (space)")
            else:
                print("Playing '" + letter + "'")

            for item in value:
                beep(item, BITRATE)
                time.sleep(0.2)

message = "hello"

print("Message:", message)
for letter in split(message):
    morse(letter.lower())

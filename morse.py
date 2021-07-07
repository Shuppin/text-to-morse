import math
import pyaudio
import time

PyAudio = pyaudio.PyAudio

bitrate = 128000    

def split(word):
    return [char for char in word]

def beep(detail, bitrate):
    freq = detail[0]
    length = detail[1]
    if freq > bitrate:
        bitrate = freq+100

    frames = int(bitrate * length)
    rframes = frames % bitrate
    wavedata = ''    

    #generating wawes
    for x in range(frames):
        wavedata = wavedata+chr(int(math.sin(x/((bitrate/freq)/math.pi))*127+128))    

    for x in range(rframes): 
        wavedata = wavedata+chr(128)

    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), 
                    channels = 1, 
                    rate = bitrate, 
                    output = True)

    stream.write(wavedata)
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
    "t": [dash],
    "u": [dot, dot, dash],
    "v": [dot, dot, dot, dash],
    "w": [dot, dash, dash],
    "x": [dash, dot, dot, dash],
    "y": [dash, dot, dash, dash],
    "z": [dash, dash, dot, dot],
    " ": [space],
    "0": [dash, dash, dash, dash, dash],
    "1": [dot, dash, dash, dash, dash],
    "2": [dot, dot, dash, dash, dash],
    "3": [dot, dot, dot, dash, dash],
    "4": [dot, dot, dot, dot, dash],
    "5": [dot, dot, dot, dot, dot],
    "6": [dash, dot, dot, dot, dot],
    "7": [dash, dash, dot, dot, dot],
    "8": [dash, dash, dash, dot, dot],
    "9": [dash, dash, dash, dash, dot]
    }

    for key, value in letters.items():
        if key == letter:
            if letter == " ":
                print("Playing (space)")
            else:
                print("Playing '" + letter + "'")

            for item in value:
                beep(item, bitrate)
                time.sleep(0.2)

#print("Message:", message)
#for letter in split(message):
#    morse(letter.lower())


from pynput import keyboard
import morse

def on_press(key):
    try:
        morse.morse(key.char)
    except AttributeError:
        print('Ignoring special key {0}'.format(
            key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
 
listener = keyboard.Listener(
    on_press=on_press)
listener.start()
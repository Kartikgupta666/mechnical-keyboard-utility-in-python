import keyboard
from playsound import playsound
import threading

# Path to the sound file for key presses
sound_file = "enter-button-mechanical-keyboard-14388.wav"

# Function to play the sound
def play_sound():
    playsound(sound_file)

# Function to handle key press events
def on_key_event(event):
    # Start a new thread to play the sound to avoid blocking the main thread
    threading.Thread(target=play_sound).start()

# Hook the keyboard event to the handler
keyboard.hook(on_key_event)

# Keep the script running
keyboard.wait()

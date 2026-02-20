import pyttsx3
import threading

# Initialize engine
engine = pyttsx3.init()

# Set speaking rate
engine.setProperty('rate', 170)

# Set voice (optional: 0 = male, 1 = female depending on system)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Create lock for thread safety
lock = threading.Lock()

def text_to_speech(text):
    """Speak the given text safely using threading lock"""
    with lock:
        engine.say(text)
        engine.runAndWait()

# Run only if file executed directly
if __name__ == "__main__":
    text = input("Enter text to speak: ")
    text_to_speech(text)
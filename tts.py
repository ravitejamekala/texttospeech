import pyttsx3
if __name__ == "__main__":
    while True:
        message = input("Enter your message: ")
        if message == "s":
            break
        tts = pyttsx3.init()
        tts.say(message)
        tts.runAndWait()
        print("Enter s to stop")
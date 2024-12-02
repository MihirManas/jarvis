from modules.speech_recognition import SpeechHandler
from modules.web_automation import WebAutomation
import config

class Jarvis:
    def __init__(self):
        self.speech_handler = SpeechHandler()
        self.web_automation = WebAutomation()
    
    def start(self):
        print(f"Hello! I'm {config.ASSISTANT_NAME}")
        # Main interaction loop
        while True:
            command = self.speech_handler.recognize_speech()
            self.process_command(command)
    
    def process_command(self, command):
        # Command processing logic
        pass

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.start()

import sys

class ConsoleChannel:
    def __init__(self, lang="en"):
        self.lang = lang
        self.transcript = []

    def send(self, text):
        print(text)
        self.transcript.append(("agent", text))

    def confirm(self, text):
        print(text + " [y/n]")
        self.transcript.append(("agent", text))
        # Auto-consent for demo (simulate 'y')
        print("y")
        self.transcript.append(("user", "y"))
        return True

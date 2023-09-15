# Imports #

# Create GUI #

# Command Functionality #
class persona:
    def __init__ (self, name):
        self.name = name

    def greet(self):
        print("Hello! My name is ", self.name)

    def ask(self):
        input("What can i do for you today?")

    def open(self, appName):
        print("Opening ", self.appName)

francis = persona("francis")
francis.greet()
userInput = francis.ask()
print(userInput)

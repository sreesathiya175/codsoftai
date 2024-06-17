import re

class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            r'hi|hello|hey': self.greet,
            r'bye|goodbye|see you': self.farewell,
            r'how are you': self.ask_how_are_you,
            r'what is your name': self.ask_bot_name,
            r'.*weather.*': self.ask_weather,
            r'.*help.*': self.ask_help,
            r'my name is (.*)': self.remember_name,
            r'.*name.*': self.ask_user_name,
            r'.*': self.default_response
        }
        self.user_name = None

    def greet(self, match):
        if self.user_name:
            return f"Hello {self.user_name}! How can I help you today?"
        else:
            return "Hello! How can I help you today?"

    def farewell(self, match):
        return "Goodbye! Have a great day!"

    def ask_how_are_you(self, match):
        return "I'm a chatbot, so I'm always good! How can I assist you?"

    def ask_bot_name(self, match):
        return "I'm a chatbot created by OpenAI. What's your name?"

    def ask_weather(self, match):
        return "I'm not sure about the weather right now, but you can check a weather website or app for current updates."

    def ask_help(self, match):
        return "Sure, I'm here to help! What do you need assistance with?"

    def remember_name(self, match):
        self.user_name = match.group(1)
        return f"Nice to meet you, {self.user_name}!"

    def ask_user_name(self, match):
        if self.user_name:
            return f"Your name is {self.user_name}, isn't it?"
        else:
            return "I don't think I know your name yet. What's your name?"

    def default_response(self, match):
        return "I'm sorry, I don't understand that. Can you please rephrase?"

    def get_response(self, user_input):
        for pattern, func in self.rules.items():
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                return func(match)
        return self.default_response(None)

def chat():
    bot = RuleBasedChatbot()
    print("Chatbot: Hello! I am a rule-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'bye|goodbye|see you', user_input, re.IGNORECASE):
            print(f"Chatbot: {bot.farewell(None)}")
            break
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()


        
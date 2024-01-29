# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatApp(App):
    def build(self):
        self.chatbot = self.initialize_chatbot()
        self.main_layout = BoxLayout(orientation='vertical')
        self.output_label = Label(text="Chatbot: Hello! How can I help you?")
        self.user_input = TextInput(hint_text="Type your message here", multiline=False)
        self.user_input.bind(on_text_validate=self.get_response)
        self.main_layout.add_widget(self.output_label)
        self.main_layout.add_widget(self.user_input)
        return self.main_layout

    def initialize_chatbot(self):
        chatbot = ChatBot('MyBot')
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train('chatterbot.corpus.english')
        return chatbot

    def get_response(self, instance):
        user_input = instance.text
        response = self.chatbot.get_response(user_input).text
        self.output_label.text = f"Chatbot: {response}"
        instance.text = ""

if __name__ == '__main__':
    ChatApp().run()

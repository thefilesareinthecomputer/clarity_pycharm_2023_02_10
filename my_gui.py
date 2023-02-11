# my_gui.py

import sys
import kivy
import sentiment_analysis
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class ChatInterface(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.rows = 2

        # create chat window
        self.chat_window = ScrollView(size_hint=(1, 0.8))
        self.add_widget(self.chat_window)
        self.chat_window_text = Label(text="", size_hint_y=None)
        self.chat_window_text.bind(width=self.chat_window_text.setter('text_size'))
        self.chat_window.add_widget(self.chat_window_text)

        # create input field
        self.entry_field = TextInput(multiline=False, size_hint=(1, 0.2))
        self.entry_field.bind(on_text_validate=self.send_message)
        self.add_widget(self.entry_field)

    def send_message(self, instance):
        user_input = self.entry_field.text

        # insert user's message into the chat window
        self.chat_window_text.text += "You: " + user_input + "\n"

        # clear the input field
        self.entry_field.text = ""

        # get response from the AI model and insert it into the chat window
        chatbot_response = sentiment_analysis.get_response(user_input)
        self.chat_window_text.text += "Clarity: " + chatbot_response + "\n"

class ChatApp(App):
    def build(self):
        return ChatInterface()

if __name__ == "__main__":
    ChatApp().run()
    print("The GUI was loaded and displayed successfully!")

import sys
import kivy
import sentiment_analysis
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class ChatInterface(GridLayout):
    def __init__(self, df, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.df = df


        # create chat window
        self.chat_window = ScrollView(size_hint=(1, 0.8))
        self.chat_window_text = Label(text="", size_hint_y=None)
        self.chat_window_text.bind(width=self.chat_window_text.setter('text_size'))
        self.chat_window.add_widget(self.chat_window_text)
        self.add_widget(self.chat_window)

        # create input field
        self.entry_field = TextInput(multiline=False, size_hint=(1, 0.2))
        self.entry_field.bind(on_text_validate=self.send_message)
        self.add_widget(self.entry_field)

    def send_message(self, instance):
        user_input = self.entry_field.text
        self.chat_window_text.text += "You: " + user_input + "\n"
        self.entry_field.text = ""
        chatbot_response = sentiment_analysis.generate_response(self.df, user_input)
        self.show_response(chatbot_response)

    def show_response(self, response):
        self.chat_window_text.text += "Bot: " + response + "\n"
        self.chat_window.scroll_y = 0

class MainApp(App):
    def __init__(self, df, **kwargs):
        super().__init__(**kwargs)
        self.df = df

    def build(self):
        self.chat_interface = ChatInterface(df=self.df)
        return self.chat_interface

if __name__ == "__main__":
    MainApp().run()


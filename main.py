# main.py

import kivy
import data_preprocessing
import sentiment_analysis
import my_gui
from kivy.app import App
from my_gui import ChatApp


if __name__ == "__main__":
    df = data_preprocessing.create_dataframe(data_preprocessing.directories)
    ChatApp().run()

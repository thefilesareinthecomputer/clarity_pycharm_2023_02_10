import my_gui
import data_preprocessing
import sentiment_analysis
from kivy.app import App
from my_gui import MainApp
from data_preprocessing import df
class MainApp(App):
    def __init__(self, **kwargs):
        print("Constructing MainApp")
        self.df = data_preprocessing.create_dataframe(data_preprocessing.directories)
        super().__init__(**kwargs)

    def build(self):
        print("Building MainApp")
        self.main_app = my_gui.MainApp(df=self.df)
        self.root = self.main_app.root
        return self.root

    def handle_user_input(self, user_input):
        response = sentiment_analysis.generate_response(self.df, user_input)
        self.main_app.show_response(response)

if __name__ == "__main__":
    MainApp().run()



from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from sys import exit
from api import apis

Builder.load_file('design/design.kv')
result = "Your result"
user_input = ""  # using it to define the input when clicks one more


class FirstPage(Screen):

    def result_page(self, value):
        global result, user_input
        user_input = value
        if value == "quote":
            result = apis.getQuote()
            print(result)
        elif value == "joke":
            result = apis.getJoke()
            print(result)
        self.manager.get_screen('Result').labelText = result
        self.manager.current = "Result"

    def synonym_page(self):
        self.manager.current = "synonym"


class RootWidget(ScreenManager):
    pass


class ResultScreen(Screen):
    labelText = StringProperty('My label')

    def home(self):
        self.manager.current = "home_page"

    def again(self):
        FirstPage.result_page(self, user_input)

    def close_app(self):
        exit()


class FindSynonyms(Screen):
    definition = StringProperty()
    example = StringProperty()
    synonym_words = StringProperty()

    def get_synonym(self, word):
        if word is not "":
            result = apis.synonyms(word)
            print(result)
            self.manager.get_screen('synonym').definition = 'Definition : '+result['definition']
            self.manager.get_screen('synonym').example = 'Example : '+result['example']
            if type(result['synonyms']) is list:
                words = "\u2022 ".join(str(x + '  ') for x in result['synonyms'])
            else:
                words = result['synonyms']
            self.manager.get_screen('synonym').synonym_words = 'Synonyms :\n \u2022 '+words
        else:
            self.manager.get_screen('synonym').definition = "Please enter a word to search!!"

    def clear_input(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ''

    def home(self):
        ResultScreen.home(self)

    def close_app(self):
        exit()


class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        print('pressed')


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()

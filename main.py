from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text="Hello, Kivy!\n打包成功！")

if __name__ == '__main__':
    TestApp().run()

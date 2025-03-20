from cProfile import label

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


##appclassとInterfaceクラスの作成
class Interface(FloatLayout):
    def display_information(self):
        data=self.ids.textInput.text
        self.ids.label.text=data


##appclass
class ProjectApp(App):
##AppclassにInterfaceclassを定義
    pass

##実行方法
ProjectApp().run()

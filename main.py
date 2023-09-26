from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class WumpaTime(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        title = Label(text='Wumpa Time Countdown', size_hint_y=None, height=100, )
        self.t = TextInput(font_size=80, size_hint_y=None, height=200, halign='right')
        self.lista = Label(font_size=100)
        box = BoxLayout()
        box2 = BoxLayout()
        bremove = Button(text="Remove", size_hint=(None, None), size=(100, 100))
        badd = Button(text="Add", size_hint=(None, None), size=(100, 200), on_release=self.update_label)

        #t.bind(text=lista.setter('text'))

        box.add_widget(self.t)
        box.add_widget(badd)
        layout.add_widget(title)
        layout.add_widget(self.lista)
        layout.add_widget(box)

        return layout

    def update_label(self, button_instance):
        self.lista.text = self.t.text


WumpaTime().run()
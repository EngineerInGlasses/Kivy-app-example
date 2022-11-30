#не забудь импортировать необходимые элементы!
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
class MainScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name = name)
        hl = BoxLayout(orientation = 'horizontal')
        vl = BoxLayout(orientation = 'vertical', padding = 3, spacing = 8)
        txt = Label(text = 'Выбери экран:')
        btn1 = Button(text = 'Экран 1')
        btn2 = Button(text = 'Экран 2')
        btn3 = Button(text = 'Экран 3')
        btn4 = Button(text = 'Экран 4')
        btn1.on_press = self.switch
        btn2.on_press = self.flip
        btn3.on_press = self.plif
        btn4.on_press = self.hctiws
        hl.add_widget(txt)
        vl.add_widget(btn1)
        vl.add_widget(btn2)
        vl.add_widget(btn3)
        vl.add_widget(btn4)
        hl.add_widget(vl)
        self.add_widget(hl)
    def switch(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'
    def flip(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
    def plif(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'third'
    def hctiws(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'fourth'
class FirstScr(Screen):
    def __init__(self, name = 'first'):
        super().__init__(name = name)
        btn1 = Button(text = 'Не нажимай', size_hint = (0.4, 0.2), pos_hint = {"center_x": 0.3, "center_y": 0.55})
        btn2 = Button(text = 'Вернуться назад', size_hint = (0.4, 0.2), pos_hint = {"center_x": 0.7, "center_y": 0.35})
        btn2.on_press = self.back
        self.add_widget(btn1)
        self.add_widget(btn2)
    def back (self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'main'
class SecondScr(Screen):
    def __init__(self, name = 'second'):
        super().__init__(name = name)
        hl = BoxLayout()
        txt = Label(text = 'И здесь тоже')
        btn = Button(text = 'Вернуться назад')
        btn.on_press = self.back
        hl.add_widget(btn)
        hl.add_widget(txt)
        self.add_widget(hl)
    def back (self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
class ThirdScr(Screen):
    def __init__(self, name = 'third'):
        super().__init__(name = name)
        hl = BoxLayout()
        txt = Label(text = 'Абсолютное ничто.')
        btn = Button(text = 'Вернуться назад')
        btn.on_press = self.back
        hl.add_widget(txt)
        hl.add_widget(btn)
        self.add_widget(hl)
    def back (self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'
class FourthScr(Screen):
    def __init__(self, name = 'fourth'):
        super().__init__(name = name)
        vl = BoxLayout(orientation = 'vertical')
        txt = Label(text = 'Даже не знаю что здесь написать...')
        btn = Button(text = 'Вернуться назад')
        btn.on_press = self.back
        vl.add_widget(btn)
        vl.add_widget(txt)
        self.add_widget(vl)
    def back (self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'main'
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        return sm
app = MyApp()
app.run()
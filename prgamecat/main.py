from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.animation import Animation

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Додаємо кота та рибку на екран
        self.cat = Cat(source='assets/pictures/cat.png', size_hint=(None, None), size=(200, 200),
                       pos_hint={'x': 0.5, 'y': 0.100})
        self.fish = Fish(source='assets/pictures/fish.png', size_hint=(None, None), size=(100, 100),
                         pos_hint={'x': 0.2, 'y': 0.3})
        self.add_widget(self.cat)
        self.add_widget(self.fish)

        # Створення кнопки та додавання обробника події click
        self.button = Button(text='Натисни мене', size_hint=(None, None), size=(150, 50))
        self.button.bind(on_press=self.click)
        self.add_widget(self.button)

    def click(self, instance):
        print('Натиснуто на кнопку')
        self.cat.jump()
        self.fish.fall()

class GameScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(GameScreen(name="game"))
        return sm

class Cat(Image):
    def jump(self):
        # Анімація підскоку котика
        cat_animation = Animation(pos_hint={'center_x': 0.5, 'y': 0.3}, duration=0.2) + \
                        Animation(pos_hint={'center_x': 0.5, 'y': 0.1}, duration=0.2)
        cat_animation.start(self)

class Fish(Image):
    def fall(self):
        # Анімація падіння рибки
        fish_animation = Animation(pos_hint={'center_x': 0.2, 'y': 0.5}, duration=0.3)+ \
        Animation(pos_hint={'center_x': 0.3, 'y': 0.3}, duration=0.3) 
                        
        fish_animation.start(self)

if platform != 'android':
    Window.size = (400, 800)
    Window.left = 750

if __name__ == "__main__":
    MainApp().run()
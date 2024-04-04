
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        for i in range(1, 5):
            btn = Button(text=f'Page {i}')
            btn.bind(on_press=self.change_screen)
            layout.add_widget(btn)
        self.add_widget(layout)

    def change_screen(self, instance):

        target_screen_name = 'page ' + instance.text.split(' ')[-1].lower()
        self.manager.current = target_screen_name

class PageScreen(Screen):
    def __init__(self, page_number, **kwargs):
        super().__init__(**kwargs)
        self.name = f'page {page_number}'
        layout = BoxLayout(orientation='vertical')

        # Додаткові кнопки для інших функцій або переходів
        for i in range(1, 4):  # Створення трьох додаткових кнопок
            btn = Button(text=f'Page {page_number}')
            layout.add_widget(btn)

        back_btn = Button(text='Back to Main')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        for i in range(1, 5):
            sm.add_widget(PageScreen(i))
        return sm


if __name__ == '__main__':
    MyApp().run()
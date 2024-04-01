#https://labdeck.com/python-designer/python-gui-designer/
#Rishabh_0507
#Aowu282n@££@2927Ka


import time
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.clock import Clock
from Get_Images import Start
import requests
import random
from TouchRippleButton import RippleButton
from kivy.uix.scrollview import ScrollView
import os

os.environ["KIVY_NO_CONSOLELOG"] = "1"

class Scroll_for_wallpapers(ScrollView):
    pass

class MainScreen(Screen):
        from Get_Images import Start
        def do(self):
            name = f"Image{time.time()}.png"
            list1, status = Start(self.ids.reddit_name.text, self.ids.username.text, self.ids.password.text)
            print(list1)
            f = open(
                f"/home/Sk7/Documents/python/Python/Wallpaper_proper/cache/{name}", "wb")
            image = requests.get(random.choice(list1))
            f.write(image.content)
            f.close()
            #for KDE
            os.system(f'plasma-apply-wallpaperimage /home/Sk7/Documents/python/Python/Wallpaper_proper/cache/{name}')

            #for Gnome
            # os.system(
            #     f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/Sk7/Documents/python/Python/Wallpaper_proper/cache/{name}")
            
        
class FrontScreen(Screen):
    def c_s(self):
        sm.transition = FadeTransition()
        sm.transition.duration = .5
        sm.current = "Mainscreen"
    Clock.schedule_once(c_s, 0)

class MyApp(App):
    def build(self):
        global sm
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(FrontScreen(name="FrontScreen"))
        sm.add_widget(MainScreen(name="Mainscreen"))
        sm.current = "FrontScreen"
        return sm

if __name__ == "__main__":
    MyApp().run()



print()
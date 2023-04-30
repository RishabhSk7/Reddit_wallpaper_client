from kivy.uix.behaviors.touchripple import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.clock import Clock
#import threading

class RippleButton(TouchRippleBehavior, Button):
    def __init__(self, **kwargs):
        super(RippleButton, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        if collide_point:
            touch.grab(self)

            self.transparency = self.background_color[3]
            self.background_color[3] = .5
            self.background_normal = 'file.png'

            self.ripple_duration_in = 0.2
            self.ripple_duration_out = 0.5
            self.ripple_show(touch)
            self.dispatch('on_press')
            return True
        return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_fade()

            def defer_release(dt):
                self.background_color[3] = self.transparency
                self.background_normal = "file.png"
                self.dispatch('on_release')
            Clock.schedule_once(defer_release, self.ripple_duration_out)
            return True

        return False

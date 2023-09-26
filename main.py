from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.scrollview import ScrollView


#class ScrollViewExample(ScrollView):
#+pass


class WidgetsExample(BoxLayout):
    count = 0
    count_enabled = False
    my_text = StringProperty("0")

    def On_Count_Click(self):
        if self.count_enabled == True:
            self.count += 1
            self.my_text = str(self.count)

    def On_Toggle_Button(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True



class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        size = dp(100)
        for i in range(0, 100):
            b = Button(text = str(i), size_hint=(None, None), size = (size , size))
            self.add_widget(b)
#class GridLayoutExample(GridLayout):
#   pass

class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text = "A")
        b2 = Button(text = "B")
        b3 = Button(text = "C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


TheLabApp().run()
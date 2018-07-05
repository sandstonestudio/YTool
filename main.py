#-*- coding: utf-8 -*-

from random import sample
from string import ascii_lowercase

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty


class LeftNavi(BoxLayout):
    navimenuswitcher = StringProperty()
    is_navimenuExpand = BooleanProperty()

    def __init__(self, **kwargs):
        super(LeftNavi, self).__init__(**kwargs)
        self.navimenuswitcher = str(u'\uF142')
        self.is_navimenuExpand = bool(False)

    def naviMenuSwitch(self):
        if self.is_navimenuExpand:
            self.navimenuswitcher = str(u'\uF142')
            self.is_navimenuExpand = False
        else:
            self.navimenuswitcher = str(u'\uF0C9')
            self.is_navimenuExpand = True
        
        

class ListSection(BoxLayout):
    def populate(self):
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]

class ContentSection(BoxLayout):
    pass

class YToolRoot(BoxLayout):
    pass



class YToolApp(App):
    pass

if __name__ == '__main__':
    YToolApp().run()
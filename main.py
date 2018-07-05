from random import sample
from string import ascii_lowercase

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory

class LeftNavi(BoxLayout):
    def printwidget(self):
        print('LeftNavi widget is called!')

    def populate(self):
        print('LeftNavi test button is called!')
        #self.root.children[1].populate()
        #app.root.listSection.populate()
    
    def leftNavi_goto(self, itemname):
        print('LeftNavi LABEL:{} is called!'.format(itemname))

class ListSection(BoxLayout):
    def printwidget(self):
        print('ListSection widget is called!')

    def populate(self):
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        self.rv.data.insert(0, {'value': value or 'default value'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['value'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)

class ContentSection(BoxLayout):
    def printwidget(self):
        print('ContentSection widget is called!')

class YToolRoot(BoxLayout):
    def printwidget(self):
        print('YToolRoot widget is called!')



class YToolApp(App):
    pass

if __name__ == '__main__':
    YToolApp().run()
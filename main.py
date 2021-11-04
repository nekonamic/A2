"""
Name: Roswaal Mathers
Date: 11/4/2021
Brief Project Description: Album Tracker 2.0
"""
import csv

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from album import Album
from albumcollection import AlbumCollection

LogHandler = AlbumCollection()


class AlbumTrackerApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        LogHandler.load_albums()
        self.create_albums_box()

    def build(self):
        self.title = "Album Tracker 2.0"
        self.root = Builder.load_file("app.kv")
        return self.root

    def change_sort_rule(self, new_rule):
        self.root.ids.sort_rule.text = new_rule

    def clear_albums_box(self):
        self.root.ids.albums_box.clear_widgets()

    def create_albums_box(self):
        for serial, album in enumerate(LogHandler.list_of_albums):
            temp_button = Button(text="{} by {},({})".format(album.title, album.artist, album.year),
                                 id=serial, background_color=())
            if album.c_or_r == "r":
                temp_button = Button(background_color=(1.0, 0.0, 0.0, 1.0))
            temp_button.bind(on_press=self.press_down_button(serial))

    def press_down_button(self, serial):
        new_list_of_albums = list(LogHandler.list_of_albums)
        if new_list_of_albums[serial][3] == "r":
            new_list_of_albums[serial][3] = "c"
            self.root.ids.albums_box.background_color = ()
            with open("albums.csv", "w", newline="") as albums:
                writer = csv.writer(albums)
                writer.writerows(new_list_of_albums)
        else:
            new_list_of_albums[serial][3] = "r"
            self.root.ids.albums_box.background_color = (1.0, 0.0, 0.0, 1.0)
            with open("albums.csv", "w", newline="") as albums:
                writer = csv.writer(albums)
                writer.writerows(new_list_of_albums)


if __name__ == "__main__":
    AlbumTrackerApp().run()

import csv
from album import Album


class AlbumCollection:
    def __init__(self):
        self.list_of_albums = []
        self.add_album = []

    def load_albums(self):
        with open("albums.csv", "r") as albums:
            reader = csv.reader(albums)
            for index, row in enumerate(reader):
                self.list_of_albums.append(row[0])
                self.list_of_albums[index] = Album(row[0], row[1], row[2], row[3])

    def save_albums(self):
        with open("albums.csv", "w") as albums:
            writer = csv.writer(albums)
            writer.writerows(self.list_of_albums)

    def add_album(self):
        with open("albums.csv", "a") as albums:
            writer = csv.writer(albums)
            writer.writerow(self.add_album)

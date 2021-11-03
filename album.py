class Album:
    def __init__(self, title, artist, year, is_completed):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_completed = is_completed

    def __str__(self):
        if self.is_completed:
            return "completed"
        else:
            return "required"

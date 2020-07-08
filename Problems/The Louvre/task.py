class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


painting = Painting(input(), input(), input())
print('"{}" by {} ({}) hangs in the {}.'
      .format(painting.title,
              painting.artist,
              painting.year,
              Painting.museum))

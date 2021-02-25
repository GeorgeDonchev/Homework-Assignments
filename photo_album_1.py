import math

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[]for n in range(1, pages+1)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages = math.ceil(photos_count/4))

    def add_photo(self, label):
        for i in range(len(self.photos)):
            if len(self.photos[i])<4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i} slot {len(self.photos[i])}"
        return "No more free spots"

    def display(self):
        result = '-'*11 + '\n'
        for p in range(len(self.photos)):
            temp=("[] "*len(self.photos[p])).rstrip()
            result+= temp+ '\n' + '-'*11 + '\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

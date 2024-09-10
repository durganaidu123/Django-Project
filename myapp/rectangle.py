# myapp/rectangle.py
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield length first in the required format
        yield {'length': self.length}
        # Then yield width in the required format
        yield {'width': self.width}

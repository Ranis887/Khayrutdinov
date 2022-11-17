from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def draw(self):
        print('Zapusk otrisovki')


class Pen(Stationery):
    def __init__(self):
        super().__init__('pen')

    def draw(self):
        print(self.title)


class Pencil(Stationery):
    def __init__(self):
        super().__init__('pencil')

    def draw(self):
        print(self.title)


class Handle(Stationery):
    def __init__(self):
        super().__init__('handle')

    def draw(self):
        print(self.title)


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()

class Cat:
    def __init__(self, imya, okras, vozrast):
        self.imya = imya
        self.okras = okras
        self.vozrast = vozrast

    def meow(self):
        print(self.imya + ' - МяуМяу')

    def mur(self):
        print(self.imya + ' - МурМур')

    def bro(self):
        print(self.imya + ' - Whatsup bro')


c = Cat('Pushok', 'Black Edition', '7')
# Атрибуты
print(c.imya)
print(c.okras)
print(c.vozrast)
# Методы
c.meow()
c.mur()
c.bro()
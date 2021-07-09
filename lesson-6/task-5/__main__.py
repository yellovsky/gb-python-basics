class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print('Start drawing by pen')


class Pencil(Stationery):
    def draw(self):
        print('Start drawing by pencil')


class Handle(Stationery):
    def draw(self):
        print('Start drawing by handle')


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

pen.draw()
pencil.draw()
handle.draw()

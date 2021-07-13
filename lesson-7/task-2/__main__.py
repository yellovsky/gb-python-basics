from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def get_fiber_count(self):
        pass


class Coat(Clothes):
    size = None

    def __init__(self, size):
        self.size = size

    @property
    def get_fiber_count(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    height = None

    def __init__(self, height):
        self.height = height

    @property
    def get_fiber_count(self):
        return 2 * self.height + 0.3

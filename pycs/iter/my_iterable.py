

class MyIterable:

    def __init__(self, data: list[int]):
        self.data: list[int] = data

    def __getitem__(self, item):
        return self.data[item]

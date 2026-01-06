
__all__ = ["MyData"]


class MyData:

    def __init__(self, data: list):
        self._data: list = data

    def __iter__(self):
        return MyDataIterator(data=self._data)


class MyDataIterator:

    def __init__(self, data: list):
        self._data = data
        self._pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._pointer < len(self._data):
            self._pointer += 1
            return self._data[self._pointer - 1]
        else:
            raise StopIteration

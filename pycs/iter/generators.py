

class MyGenerator:

    def __init__(self, n: int):
        self._n: int = n

    def __iter__(self):
        for i in range(self._n):
            yield i


if __name__ == "__main__":

    gen_ = (x for x in range(10))
    while True:
        try:
            print(next(gen_))
        except StopIteration:
            print(f"{StopIteration.__name__} error has been caught")
            break

    my_gen = MyGenerator(20)
    my_gen_iter = iter(my_gen)
    next(my_gen_iter)

    for x in MyGenerator(10):
        print(x)

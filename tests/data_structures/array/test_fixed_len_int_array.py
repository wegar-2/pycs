import random

from pytest import fixture, raises

from pycs.data_structures.array.fixed_len_int_array import FixedLenIntArray


@fixture
def fli_data_array() -> FixedLenIntArray:
    ar: FixedLenIntArray = FixedLenIntArray(l=100)
    for i in range(len(ar)):
        ar[i] = random.randint(a=0, b=1_000)
    return ar


def test_fixed_len_int_array_creation():
    ar: FixedLenIntArray = FixedLenIntArray(l=100)
    assert isinstance(ar, FixedLenIntArray)
    assert len(ar) == 100


def test_set_array_members(fli_data_array):
    with raises(IndexError):
        fli_data_array[1000] = 123
    with raises(ValueError):
        fli_data_array[59] = "qwerty"


def test_as_iterable(fli_data_array):
    data_ = [x for x in fli_data_array]
    assert fli_data_array.data == data_

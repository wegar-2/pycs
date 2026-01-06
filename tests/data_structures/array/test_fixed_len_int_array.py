import random

from pytest import raises

from pycs.data_structures.array.fixed_len_int_array import FixedLenIntArray


def test_fixed_len_int_array_creation():
    ar: FixedLenIntArray = FixedLenIntArray(l=100)
    assert isinstance(ar, FixedLenIntArray)
    assert len(ar) == 100


def test_set_array_members():
    ar: FixedLenIntArray = FixedLenIntArray(l=100)
    for i in range(len(ar)):
        ar[i] = random.randint(a=0, b=1_000)
    with raises(IndexError):
        ar[1000] = 123
    with raises(ValueError):
        ar[59] = "qwerty"

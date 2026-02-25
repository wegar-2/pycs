from pytest import fixture

from pycs.sm import bfsm
from pycs.common.load_data import load_data


@fixture
def thucydides() -> str:
    return load_data("peloponnesian_war")


def test_bfsm_case1():
    assert bfsm(
        text="poinuoiun qwerty nmnmbbhhbfdqwerty",
        pattern="qwerty"
    ) == [10, 30]


def test_bfsm_case2(thucydides):
    assert bfsm(
        text=thucydides,
        pattern="war"
    ) == []

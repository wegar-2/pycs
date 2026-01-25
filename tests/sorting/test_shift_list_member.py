from pycs.sorting.shift_list_member import shift_list_member

from pytest import fixture


@fixture
def default_list():
    return [1, 9, 3, 5, 4, 2, 4]


def test_right_to_left(default_list):
    assert (
            shift_list_member(values=default_list, pos_from=5, pos_to=1) ==
            [1, 2, 9, 3, 5, 4, 4]
    )


def test_left_to_right(default_list):
    assert (
            shift_list_member(values=default_list, pos_from=1, pos_to=5) ==
            [1, 3, 5, 4, 2, 9, 4]
    )


def test_keep_unchanged(default_list):
    assert (
        shift_list_member(values=default_list, pos_from=3, pos_to=3) ==
        default_list
    )

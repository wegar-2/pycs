from pycs.sm import (
    compute_prefix_function_value, compute_prefix_function)


def test_compute_prefix_function_value_pattern1():
    # 0123 4 56789
    # abca b bcbab
    pattern = "abcabbcbaba"
    assert compute_prefix_function_value(pattern, 4) == 2
    assert compute_prefix_function_value(pattern, 0) == 0
    assert compute_prefix_function_value(pattern, 3) == 1


def test_compute_prefix_function_value_patter2():
    #          |         |
    #          012345678901234
    pattern = "011001101010011"
    assert compute_prefix_function_value(pattern, 6) == 3
    assert compute_prefix_function_value(pattern, 0) == 0
    assert compute_prefix_function_value(pattern, 8) == 2


def test_compute_prefix_function():
    #          |         |         |
    #          0123456789 01234567890
    pattern = "010111010101110100001"
    assert compute_prefix_function(pattern) == [
        0, 0, 1, 2, 0,
        0, 1, 2, 3, 4,
        3, 4, 5, 6, 7,
        8, 9, 1, 1, 1,
        2
    ]


def test_kmpsm_pattern1():
    pass


def test_kmpsm_pattern2():
    pass

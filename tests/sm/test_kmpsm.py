from pycs.sm import compute_prefix_function_value


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

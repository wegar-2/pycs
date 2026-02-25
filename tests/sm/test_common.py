from pytest import raises

from pycs.sm import validate_sm_inputs, python_sm


def test_validate_sm_inputs_case1():
    with raises(TypeError):
        validate_sm_inputs(1234, "qwerty")


def test_validate_sm_inputs_case2():
    with raises(TypeError):
        validate_sm_inputs("qwerty asfdgpok", None)


def test_validate_sm_inputs_case3():
    with raises(ValueError):
        validate_sm_inputs("qwerty", "qwertyasdf")


def test_python_sm_case1():
    assert python_sm(text="okokmnasdfpomnj", pattern="asdf") == [6]


def test_python_sm_case2():
    assert python_sm(text="okokmnasdfpomnj", pattern="qwerty") == []


def test_python_sm_case3():
    assert python_sm(text="okokmnasdfpomnj", pattern="qwerty") == []


def test_python_sm_case4():
    assert python_sm(text="okokmnasdfpomnj", pattern="qwerty") == []

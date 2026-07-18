import pytest , calculator


def test_divide():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5,0)
    
def test_divide_normal():
    assert calculator.divide(10,2)==5    
import calculator

def test_add():
    assert calculator.add(1,4) == 5
    assert calculator.add(0,0) == 0
    assert calculator.add(0,-1) == -1 
    assert calculator.add(5,0) == 5


def test_square():
    assert calculator.square(2) == 4
    assert calculator.square(3) == 9
    assert calculator.square(-2) == 4
    assert calculator.square(0) == 0
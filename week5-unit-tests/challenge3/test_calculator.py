import pytest ,  calculator

def test_zero_volum():
    with pytest.raises(ValueError):
        calculator.calculate_concentration(5,0)

def test_negative_volum():
    with pytest.raises(ValueError):
        calculator.calculate_concentration(5,-1)


def test_negative_mass():
    with pytest.raises(ValueError):
        calculator.calculate_concentration(-5,7)

def test_normal_state():
    assert calculator.calculate_concentration(20,5) == 4







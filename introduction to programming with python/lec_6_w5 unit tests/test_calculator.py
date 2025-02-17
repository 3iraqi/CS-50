"""PEP"""
import pytest
from calculator import square



def test_positive():
    """PEP"""
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    """PEP"""
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    """PEP"""
    assert square(0) == 0

def test_str():
    """PEP"""
    with pytest.raises(TypeError):
        square("cat")

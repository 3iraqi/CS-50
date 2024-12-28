""" Import hello Function"""
from hello import hello

def test_hello():
    """Test hello function"""
    hello("David")=="hello, David"
    # can not check equality of print function because it not return value.
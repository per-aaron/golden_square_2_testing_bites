from lib.greet import *

def test_greet_says_hello():
    result = greet("Ben")
    assert result == "Hello, Ben!"
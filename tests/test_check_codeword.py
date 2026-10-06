from lib.check_codeword import *

def test_check_codeword_returns_wrong_for_invalid():
    result = check_codeword("neigh")
    assert result == "WRONG!"

def test_check_codeword_returns_close_for_h__e():
    result = check_codeword("hope")
    assert result == "Close, but nope."

def test_check_codeword_returns_correct_for_valid():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
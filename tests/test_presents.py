import pytest
from lib.presents import *

#When using wrap with a string, and then calling unwrap
#unwrap returns the original string
def test_presents_wrap_and_unwrap_returns_original_string():
    present = Present()
    present.wrap("bear")
    result = present.unwrap()
    assert result == "bear"

#When calling unwrap without any presents wrapped
#The correct exception "No contents have been wrapped." is raised
def test_presents_unwrap_raises_error_with_no_presents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error = str(e.value)
    assert error == "No contents have been wrapped."

#When calling wrap twice sequentially
#second wrap raises correct exception "A contents has already been wrapped."
def test_presents_double_wrap_raises_error_already_wrapped():
    present = Present()
    present.wrap("panda")
    with pytest.raises(Exception) as e:
        present.wrap("lamb")
    error = str(e.value)
    assert error == "A contents has already been wrapped."

#When calling wrap twice sequentially
#The first value remains the value in contents
def test_presents_double_wrap_stores_first_item_only():
    present = Present()
    present.wrap("panda")
    with pytest.raises(Exception):
        present.wrap("lamb")
    result = present.unwrap()
    assert result == "panda"
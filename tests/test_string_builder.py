from lib.string_builder import *

def test_string_builder_returns_string():
    builder = StringBuilder()
    builder.add("boo!")
    result = builder.output()
    assert type(result) == str

def test_string_builder_combines_strings():
    builder = StringBuilder()
    builder.add("Noot")
    builder.add("Noot!")
    result = builder.output()
    assert result == "NootNoot!"

def test_string_builder_returns_correct_length():
    builder = StringBuilder()
    builder.add("This string is 22 long")
    result = builder.size()
    assert result == 22
from lib.gratitudes import *

#When no string is added
#Format() returns just "Be grateful for: "
def test_gratitudes_when_empty():
    grateful = Gratitudes()
    result = grateful.format()
    assert result == "Be grateful for: "

#When you add three strings
#All 3 strings are appended, seperated by commas with Format()
def test_gratitudes_with_3_strings():
    grateful = Gratitudes()
    grateful.add("health")
    grateful.add("shelf")
    grateful.add("elf")
    result = grateful.format()
    assert result == "Be grateful for: health, shelf, elf"

#When you add mixed strings and ints
#Format() casts int to string to list numbers (failing test example)
#def test_gratitudes_with_ints_and_strings():
#    grateful = Gratitudes()
#    grateful.add(12)
#    grateful.add("twelfth")
#    grateful.add(42)
#    result = grateful.format()
#    grateful.add("sporty shoe")
#    assert result == "Be grateful for: 12, twelfth, 42, sporty shoe"
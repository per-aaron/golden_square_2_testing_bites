from lib.counter import *

def test_counter_starts_at_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_3_adds_to_3():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 3 so far."

def test_counter_two_ones_add_up_to_two():
    counter = Counter()
    counter.add(1)
    counter.add(1)
    result = counter.report()
    assert result == "Counted to 2 so far."
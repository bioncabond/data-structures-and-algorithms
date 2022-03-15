from code_challenges.hashmap_repeated_word.hashmap_repeated_word import repeated_word
import pytest
from code_challenges.hash_tables.hashtable import Hashtable

class Test_Input:
    a_check = "Once upon a time, there was a brave princess who..."

    it_check = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

    summer_check = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."


def test_make_a_hashmap():
    hashmap = Hashtable()
    assert hashmap

@pytest.fixture
def input():
    str = Test_Input()
    return str

def test_repeated_word_a(str):
    actual = repeated_word(str.a_check)
    assert actual ['dup'] == 'a'

def test_repeated_word_a(str):
    actual = repeated_word(str.it_check)
    assert actual ['dup'] == 'it'

def test_repeated_word_a(str):
    actual = repeated_word(str.summer_check)
    assert actual ['dup'] == 'summer'




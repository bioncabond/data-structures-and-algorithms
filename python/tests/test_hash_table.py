from code_challenges.hash_tables.hashtable import Hashtable
from code_challenges.linked_list.linked_list import LinkedList


def test_hashtable_exists():
    hashtable = Hashtable()
    assert hashtable

def test_hash_consistency():
    hashtable = Hashtable()
    key = "apple"
    index = hashtable.hash(key)
    # expected = '1'
    # assert actual == expected
    actual = hashtable.hash(key)
    assert actual == index

def test_same_index():
    hashtable = Hashtable()
    key_a = "listen"
    key_b = "silent"
    assert hashtable.hash(key_a) == hashtable.hash(key_b)

def test_different_index():
    hashtable = Hashtable()
    key_a = "listen"
    key_b = "zilent"
    assert hashtable.hash(key_a) != hashtable.hash(key_b)

def test_set():
    hashtable = Hashtable()
    index = hashtable.hash("spam")
    assert hashtable.buckets[index] is None
    hashtable.set("spam", "eggs")
    bucket = hashtable.buckets[index]
    assert bucket

def test_get():
    hashtable = Hashtable()
    hashtable.set("spam", "eggs")
    find = hashtable.get("spam")
    assert find == "eggs"

def test_key_retreive_value():
    hashtable = Hashtable()
    hashtable.set("alpha", "test_value")
    actual = hashtable.get("alpha")
    expected = "test_value"
    assert actual == expected

def test_key_retrieve_value_collision():
    hashtable = Hashtable()
    hashtable.set("listen", "test_value")
    hashtable.set("silent", "other_value")
    actual = hashtable.get("silent")
    expected = "other_value"
    assert actual == expected

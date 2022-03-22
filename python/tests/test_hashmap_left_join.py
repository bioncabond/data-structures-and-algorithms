from code_challenges.hashmap_left_join.hashmap_left_join import left_join
import pytest


def test_simple_left_join():
    d1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    d2 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}
    assert left_join(d1,d2) == [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', 'Null'], ['guide', 'usher', 'follow']]



def test_no_common_keys():
    map1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    map2 = {'see':'look','talk':'speak','yes':'no','chair':'table'}
    assert left_join(map1,map2) == [['fond', 'enamored', 'Null'], ['wrath', 'anger', 'Null'], ['diligent', 'employed', 'Null'], ['outfit', 'garb', 'Null'], ['guide', 'usher', 'Null']]

def test_1st_hashmap_is_empty():
    map1 = {}
    map2 = {'up':'down','fast':'quick','nope':'yup','square':'box'}
    assert left_join(map1,map2) == []

def test_2nd_dictionary_empty():
    map1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    map2 = {}
    assert left_join(map1,map2) == [['fond', 'enamored', 'Null'], ['wrath', 'anger', 'Null'], ['diligent', 'employed', 'Null'], ['outfit', 'garb', 'Null'], ['guide', 'usher', 'Null']]

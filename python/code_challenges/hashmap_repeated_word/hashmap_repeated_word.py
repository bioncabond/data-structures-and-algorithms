from code_challenges.linked_list.linked_list import LinkedList
import re

def repeated_word(str):
    if len(str) == 0:
        return None

    hashmap = Hashtable()
    lowered =str.lower()
    words = re.findall(r"/w+", lowered)

    for word in words:
        if hashmap.contains(word):
            return word
        else:
            hashmap.add(word,word)
    return None


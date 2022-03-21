from code_challenges.hash_tables.hashtable import Hashtable
import re

def repeated_word(str):
    if len(str) == 0:
        return None

    hashmap = Hashtable()
    lowered =str.lower()
    words = re.findall(r"/w+", lowered)
    print(f"{words}")

    for word in words:
        if hashmap.contains(word):
            return word
        else:
            hashmap.add(word,word)
    return None

# if __name__ == "__main__":
#     string = 'Once upon a time, there was a brave princess who...'
#     repeated_word(string)

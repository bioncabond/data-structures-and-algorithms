left_table = {
    "fond": "enamored",
    "wrath": "anger",
    "diligent": "employed",
    "outfit": "garb",
    "guide": "usher",
}

right_table = {
    "fond": "adverse",
    "wrath": "delight",
    "diligent": "idle",
    "flow": "jam",
    "guide": "follow",
}

def left_join(hashmap1,hashmap2):
    matches = []
    for key in hashmap1:
        if key in hashmap2:
            map2 = hashmap2[key]
        else:
            map2 = 'Null'
        matches.append([key, hashmap1[key], map2])
    return matches



from code_challenges.linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self,size = 1024):
        self.size = size
        self.buckets = [None] * self.size

    def set(self,key,value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()

        bucket = self.buckets[index]
        bucket.insert([key,value])

    def get(self,key):
        index = self.hash(key)
        if self.buckets[index] is None:
            return None

        current = self.buckets[index].head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def contains(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            return False
        current = self.buckets[index].head
        while current:
            if current.value[0] == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self.buckets:
            if bucket is not None:
                if len(bucket) > 1:
                    for k in bucket:
                        keys.append(k[0])
                else:
                    keys.append(bucket[0][0])
        keys.sort()
        return keys

    def hash(self,key):
        index = 0
        for ch in key:
            index += ord(ch)
        index *= 769
        index = index % self.size
        return index

if __name__ == "__main__":
    print('Hello World')

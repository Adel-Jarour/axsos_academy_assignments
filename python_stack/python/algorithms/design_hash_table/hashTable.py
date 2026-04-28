"""
Design a HashMap without using any built-in hash table libraries.
"""


"""
1. Using GitHub Copilot, I implemented a simple hash map.
"""
# class MyHashMap:

#     def __init__(self):
#         self.size = 1000
#         self.buckets = [[] for _ in range(self.size)]

#     def _hash(self, key):
#         return key % self.size

#     def put(self, key, value):
#         index = self._hash(key)
#         bucket = self.buckets[index]

#         for pair in bucket:
#             if pair[0] == key:
#                 pair[1] = value  # update
#                 return

#         bucket.append([key, value])  # insert

#     def get(self, key):
#         index = self._hash(key)
#         bucket = self.buckets[index]

#         for pair in bucket:
#             if pair[0] == key:
#                 return pair[1]

#         return -1

#     def remove(self, key):
#         index = self._hash(key)
#         bucket = self.buckets[index]

#         for i, pair in enumerate(bucket):
#             if pair[0] == key:
#                 bucket.pop(i)
#                 return

"""
2. I implemented a simple hash map using open addressing with linear probing for collision resolution.
"""
class MyHashMap:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for _ in range(self.size):

            if self.table[index] is None or self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            else:
                index = (index + 1) % self.size


    def get(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is not None and self.table[index][0] == key:
                return self.table[index][1]
            else:
                index = (index + 1) % self.size
        return -1
    
    def remove(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is not None and self.table[index][0] == key:
                self.table[index] = None
                return
            else:
                index = (index + 1) % self.size


    def display(self):
        for i in range(self.size):
            print(f"{i}  |  {self.table[i]}")

hashTable = MyHashMap()
hashTable.put('f-name', 'Adel')
hashTable.put('l-name', 'Jarour')
hashTable.put('age', '25')
hashTable.put('country', 'ps')
print(hashTable.get('l-name'))
print(hashTable.get('age'))
print(hashTable.get('country'))
hashTable.remove('age')
print(hashTable.get('age'))
hashTable.display()

"""
3. I implemented a simple hash map using separate chaining for collision resolution.
"""

# class MyHashMap:
    # def __init__(self, size=5):
    #     self.size = size
    #     self.table = [[] for _ in range(self.size)]
    
    # def _hash(self, key):
    #     return hash(key) % self.size

    # def put(self, key, value):
    #     index = self._hash(key)
    #     bucket = self.table[index]

    #     for i in range(len(bucket)):
    #         if bucket[i][0] == key:
    #             bucket[i] = (key, value)  # update
    #             return

    #     bucket.append((key, value))  # insert

    # def get(self, key):
    #     index = self._hash(key)
    #     bucket = self.table[index]

    #     for i in range(len(bucket)):
    #         if bucket[i][0] == key:
    #             return bucket[i][1]
            
    #     return -1
    
    # def remove(self, key):
    #     index = self._hash(key)
    #     bucket = self.table[index]

    #     for i in range(len(bucket)):
    #         if bucket[i][0] == key:
    #             bucket.pop(i)
    #             return


#     def display(self):
#         for i in range(self.size):
#             print(f"{i}  |  {self.table[i]}")

# hashTable = MyHashMap()
# hashTable.put('f-name', 'Adel')
# hashTable.put('l-name', 'Jarour')
# hashTable.put('age', '25')
# hashTable.put('country', 'ps')
# print(hashTable.get('l-name'))
# print(hashTable.get('age'))
# print(hashTable.get('country'))
# hashTable.remove('age')
# print(hashTable.get('age'))
# hashTable.display()
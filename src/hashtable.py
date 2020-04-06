# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key}:{self.value}"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        new_pair = LinkedPair(key, value)
        index = self._hash_mod(key)
        if self.storage[index] is None:
            self.storage[index] = new_pair
        else:
            # print(f"Can't store {value} at {key}")
            current_item = self.storage[index]
            found_key = False
            while current_item.next is not None:
                if current_item.key == key:
                    current_item.value = value
                    found_key = True
                    break
                current_item = current_item.next
            if current_item.key == key:
                current_item.value = value
                found_key = True
            if not found_key:
                current_item.next = new_pair



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            print("nothing stored to that key")
        else:
            if self.storage[index].key == key:
                self.storage[index] = self.storage[index].next
            else:
                previous_node = self.storage[index]
                current_node = self.storage[index].next
                found = False
                while current_node is not None:
                    if current_node.key == key:
                        previous_node.next = current_node.next
                        found = True
                        break
                    previous_node = current_node
                    current_node = current_node.next
                if not found:
                    print("key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            node = self.storage[index]
            while node is not None:
                if node.key == key:
                    return node.value
                node = node.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for pair in self.storage:
            if pair is not None:
                new_index = self._hash_mod(pair.key)
                if new_storage[new_index] is None:
                    new_storage[new_index] = pair
                else:
                    # print(f"Lost {pair.key}, {pair.value}")
                    node = new_storage[new_index]
                    while node.next is not None:
                        node = node.next
                    node.next = pair
        self.storage = new_storage



if __name__ == "__main__":
    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")

    table = HashTable(5)

    table.insert("key1", "value1")
    print(table.storage)

    table.insert("key1", "value1-2")
    print(table.storage)

    table.insert("key2", "value2")
    print(table.storage)
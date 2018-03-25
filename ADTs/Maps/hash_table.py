class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # this holds keys
        self.data = [None] * self.size  # this hods values

    @staticmethod
    def hash_function(key, size):
        """calculates hash value using simple remainder method
        Note:
        This is a static method because there is no implicit self
        i.e., it does not use any instance method or operate on
        any instance variables.
        """
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        """facilitates linear probing with plus 1 rehash"""
        return (old_hash + 1) % size

    def put(self, key, val):
        """puts a value to the location specified by key
        Note:
            It assumes that there will eventually be an empty slot
            unless the key is already present in the self.slots.
            It computes the original hash value and if that slot
            is not empty, iterates the rehash function until an
            empty slot occurs. If a nonempty slot already contains
            the key, the old data value is replaced with the new data value

        """
        hash_value = HashTable.hash_function(key, self.size)

        # if slot is vacant, simply put it
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = val
        else:
            # if occupied with same key, replace it
            if self.slots[hash_value] == key:
                self.data[hash_value] = val

            # if occupied with different key, apply linear probing
            else:
                next_slot = HashTable.rehash(hash_value, self.size)

                # loop until an empty slot or slot with same key is found
                while (self.slots[next_slot] is not None and
                        self.slots[next_slot] != key):
                    next_slot = HashTable.rehash(next_slot, self.size)

                # if empty slot is found put it
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = val

                else:  # if slot with same key is found, replace value
                    self.data[next_slot] = val

    def get(self, key):
        """Given a key, return the value stored in the map or None otherwise.

        Note:
            This method begins by computing the initial hash value.
            If the value is not in the initial slot, rehash is used to locate
            the next possible position. The search will terminate if we have
            returned to the initial slot. If that happens, we have exhausted
            all possible slots and the item must not be present.
        """
        starting_hash = HashTable.hash_function(key, self.size)

        data = None
        stop = False
        found = False
        position = starting_hash

        while (self.slots[position] is not None
                and not found and not stop):

            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = HashTable.rehash(position, self.size)

                if position == starting_hash:
                    stop = True

        return data

    def __getitem__(self, key):
            """overloaded method that allows access using [] """
            return self.get(key)

    def __setitem__(self, key, value):
        """overloaded method that allows assignment using [] """
        self.put(key, value)


if __name__ == "__main__":

    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)

    print(H[20])

    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H[99])

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def replace(self, key, value):
        """
        Given a key and a value, recursively traverse a HashTableEntry object and check for a key match.
        If a key match is found, replace the current value with the input value.
        Otherwise, store the key and value as a new node at the end.
        """
        if self.key == key:
            self.value = value
            return

        else:
            if self.next == None:
                self.next = HashTableEntry(key, value)
                return 
            
            self.next.replace(key, value)
    
    def __str__(self):
        string = "Key: {}  Value: {}\t".format(self.key, self.value)
        curr = self.next
        while curr != None:
            string += "Key: {}  Value: {}\t".format(curr.key, curr.value)
            curr = curr.next
        return string[0:-2]

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        return self.items / len(self.buckets)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        
        # random prime number that works for some reason
        hash = 5381

        # convert each letter in key string to Unicode numbers using ord()
        # no idea what this 33 is doing -> this tries to explain it https://stackoverflow.com/questions/10696223/reason-for-5381-number-in-djb-hash-function/13809282#13809282
        for letter in key:
            hash = (hash * 33) + ord(letter)
        
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        
        # use hash value to get the index for the correct bucket
        index = self.hash_index(key)


        # If the bucket is empty
        if self.buckets[index] == None:

            # Instantiate Hash Table Entry object with the key and value
            entry = HashTableEntry(key, value)

            # store the entry 
            self.buckets[index] = entry

            self.items += 1

            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
        
        # If the bucket is not empty (collision is possible)
        else:
            self.buckets[index].replace(key, value)

            # curr = self.buckets[index]
            
            # while curr != None:
            #     if curr.key == key:
            #         print(key, value, curr.value)
            #         curr.value = value
            #         break
            #     else:
            #         curr = curr.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # If bucket is blank
        if self.buckets[index] == None:
            print("Key not found")
            return
        
        # If bucket has only 1 entry
        elif self.buckets[index].next == None:
            if self.buckets[index].key == key:
                self.buckets[index] = None
                self.items -= 1
                return
            else:
                print("Key not found")
                return
        
        # If bucket has multiple entries
        else:
            prev = self.buckets[index]
            curr = self.buckets[index].next
            
            # If the first entry is the key
            if prev.key == key:
                self.buckets[index] = prev.next
                self.items -= 1
                return
            
            # Loop through 2nd entry until end
            while curr != None:
                
                # If match found, delete by reassigning pointers
                if curr.key == key:
                    prev.next = curr.next
                    self.items -= 1
                    return
                
                else:
                    prev = curr
                    curr = curr.next
            
            # If no matches were found
            print("Key not found")
            return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)

        entry = self.buckets[index]

        # Check for non-existent entry at the key's index
        if entry == None:
            return None

        # If the index has an entry
        else:
            
            # Search for the node with the correct key
            while entry != None:
                if entry.key == key:
                    return entry.value

                else:
                    entry = entry.next

            # If no node matches the key
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_buckets = [None] * new_capacity

        self.capacity = new_capacity

        # We cannot just move entries from the old bucket list to the new bucket list because the hash indices for the keys might change
        # So we loop through each entry and all of its nodes (key/value pairs) individually to the new buckets list
        for entry in self.buckets:
            while entry != None:
                index = self.hash_index(entry.key)

                # Since we are operating on a list and not a Hash Table, we can't use the .put() method
                # But we can easily adapt the code since .put() did not rely on other Hash Table functions.
                if new_buckets[index] == None:
                    #  Use a new entry object so that we don't inherit the 'next' pointer
                    new_buckets[index] = HashTableEntry(entry.key, entry.value)
                else:
                    new_buckets[index].replace(entry.key, entry.value)
                
                entry = entry.next

        self.buckets = new_buckets


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(i, ht.get(f"line_{i}"))

    print("")


    """
    q = HashTableEntry('A', 1)
    q.next = HashTableEntry('B', 2)
    q.next.next = HashTableEntry('C', 3)

    w = q
    while w != None:
        print(w.key, w.value)
        w = w.next
    
    print('\n\n')

    q.replace('B', 8)

    w = q
    while w != None:
        print(w.key, w.value)
        w = w.next
    """
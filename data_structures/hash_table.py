class HashTable:
    """ Hashtable built using double hashing."""
    
    def __init__(self, table_length):
        self.table = [None] * table_length

    def __str__(self):
        result = ''
        for elem in self.table:
            result = result + str(elem) +',\n'
        return result

    
    def _find_index(self, key):
        """Hash function using built in hash and Double Hashing for Collisions.
        Parameters:
            key -- the value to be hashed
        
        Return:
            tuple -- (index, bool for wether it exists in the table or not)
        """

        hash1 = hash(key)
        table_length = len(self.table)
        initial_index = hash1 % table_length

        if not self.table[initial_index]:
            return (initial_index, False)

        elif self.table[initial_index][0] == key:
            return (initial_index, True) 
        
        # There exists a collision!
        hash2 = hash(key + 'yuz')
        move_amount = hash2 % (table_length - 1) + 1
        index = (initial_index + move_amount) % table_length

        while index != initial_index:

            if not self.table[index]:
                return (index, False)

            elif self.table[index] == key:
                return (index, True)

            else:
                index = (index + move_amount) % table_length
            
        return (-1, False) # the table is full


    def insert(self, key, value):
        """
            Add element to the list, if full do nothing

            parameters:
                key, value -- pair to be added to list
            
            Return -- None
        """

        index, does_exist = self._find_index(key)
        
        # table is full
        if index == -1:
            return

        # The key already exists
        if does_exist:
            self.table[index][1] = value
            return
        
        self.table[index] = [key, value]


    def search(self, key):
        index, does_exist = self._find_index(key)

        if index == -1:
            return False
        
        if not does_exist:
            return False
        
        return self.table[index][1]

    def delete(self, key):
        pass


if __name__ == "__main__":
    ht = HashTable(5)
    ht.insert('key1', 9)
    ht.insert('key2', 2)
    ht.insert('key3', 10)
    ht.insert('key4', 100)
    assert not ht.search('key5') # Since this key doesn't exist yet, it should return False.
    ht.insert('key5', 10)

    assert ht.search('key1') == 9
    assert ht.search('key2') == 2
    assert ht.search('key3') == 10
    assert ht.search('key4') == 100
    assert ht.search('key5') == 10
    assert not ht.search('key6') # Since this key doesn't exist, it should return False.


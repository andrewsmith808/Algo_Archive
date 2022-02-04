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
        hash1 = hash(key)
        table_length = len(self.table)
        initial_index = hash1 % table_length

        if not self.table[initial_index]:
            return (initial_index, False)
        
        elif self.table[initial_index] == 'REDACTED':
            return (initial_index, True)

        elif self.table[initial_index][0] == key:
            return (initial_index, True) 
        
        # There exists a collision!
        hash2 = hash(key + 'd')
        move_amount = hash2 % (table_length - 1) + 1
        index = (initial_index + move_amount) % table_length

        while index != initial_index:

            if not self.table[index]:
                return (index, False)

            elif self.table[initial_index] == 'REDACTED':
                return (initial_index, True)

            elif self.table[index][0] == key:
                return (index, True)

            else:
                index = (index + move_amount) % table_length
            
        return (-1, False) # the table is full


    def insert(self, key, value):
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

    def remove(self, key):
        index, does_exist = self._find_index(key)

        if not does_exist:
            return

        # cannot delete in double hashing
        # used a reserved word instead to mean removed!
        if does_exist:
            self.table[index][0] = 'REDACTED'
            self.table[index][1] = 'REDACTED'
        pass



if __name__ == "__main__":
    ht = HashTable(5)
    ht.insert('key1', 9)
    ht.insert('key2', 2)
    ht.insert('key3', 10)
    ht.insert('key4', 100)
    assert not ht.search('key5')
    ht.insert('key5', 10)

    assert ht.search('key1') == 9
    assert ht.search('key2') == 2
    assert ht.search('key3') == 10
    assert ht.search('key4') == 100
    assert ht.search('key5') == 10
    assert not ht.search('key6')

    ht.remove('key1')
    ht.remove('key2')
    ht.remove('key3')
    ht.remove('key4')

    assert not ht.search('key1')
    assert not ht.search('key2')
    assert not ht.search('key3')
    assert not ht.search('key4')
    assert ht.search('key5') == 10
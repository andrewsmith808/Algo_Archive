from mimetypes import init


class HashTable:
    """ Hashtable built using djb2 and double hashing.
    
    """
    def __init__(self, table_length):
        self.table = [None] * table_length
    
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
        elif self.table[initial_index] == key:
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
        index = self.find_index(key)
        pass

    def search(self, key):
        pass

    def delete(self, key):
        pass


if __name__ == "__main__":
    pass

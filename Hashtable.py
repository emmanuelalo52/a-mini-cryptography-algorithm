#creating a hash table
class hash_item(object):
    def __init__(self,key,value):
        self.key=key
        self.value=value
        #because it is a key-value hash table
class hash_table(object):
    def __init__(self):
        self.size=256
        self.slots=[None for i in range(self.size)]
        self.count=0
    """NOTE:self.size is the total number of slots used and unused while count is the total used slots"""
    def _hash(self,key):
        """using a chaining system to find empty slots"""
        """because the hash function will be used in the class hash_table we put an underscore"""
        multiplier=1
        hash_value=0
        for word in key:
            hash_value+=multiplier*sum(map(ord,word))
            multiplier+=1
            return hash_value % self.size #so as to know the remainder of slots we divide the new hash value by the size of slots
    def put_elements(self,key,value):
        item=hash_item(key,value)
        h=self._hash(key)
        """NOTE:here we try avoid collision when adding data by adding plus one to the last hash value so that when divided by the size it will give us an empty slot"""
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h=(h+1) % self.size
        if self.slots[h] is None:
            self.count+=1
            self.slots[h]=item
    def get_elements(self,key):
        h=self._hash(key)
        #in case of an incorrect key we use the put method
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return sum(map(ord,self.slots[h].value))
            h=(h+1) % self.size
            return None
    #Rather than using the defined statement , i made a classmethod that helps in moving fast
    def __setitem__(self,key,value):
        self.put_elements(key,value)
    def __getitem__(self,key):
        return self.get_elements(key)
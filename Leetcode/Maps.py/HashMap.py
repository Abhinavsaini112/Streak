
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketsize = 10
        self.bucket = [None for i in range(self.bucketsize)]
        self.count = 0

    def size(self):
        return self.count
    
    def getBucketIndex(self, hc):
        return abs(hc)%(self.bucketsize)
    
    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        # print(index)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        head = self.bucket[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.bucket[index] = newNode
        self.count += 1

        # Now we will check the load factor after insertion.
        loadFactor = self.count/self.bucketsize
        if loadFactor >= 0.7:
            self.rehash()

    def getValue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.bucket[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return head.value
            prev = head
            head = head.next
        return None
    
    def rehash(self):
        temp = self.bucket  #To store the old bucket
        self.bucket = [None for i in range(2 * self.bucketsize)]
        self.bucketsize = 2 * self.bucketsize #doubling the size
        self.count = 0
        for head in temp:  #inserting each value of old bucket to new one
            while head is not None:
                self.insert(head.key,head.value)
                head = head.next





m = Map()

m.insert("Abhinav", 2)
m.insert("Kartavya", 9)

print(m.size())      # 2
print(m.remove("Abhinav"))  # 2
print(m.size())      # 1
print(m.getValue("Abhinav")) # None


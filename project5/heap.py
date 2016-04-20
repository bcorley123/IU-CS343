from swap import swap

def less(x, y):
    return x < y

def less_key(x, y):
    return x.key < y.key

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * (i + 1)

def parent(i):
    return (i-1) / 2

# Student code -- fill in all the methods that have pass as the only statement
class Heap:
    def __init__(self, data, less = less):
        self.data = data
        self.less = less
        self.build_min_heap()
        
    def __repr__(self):
        return repr(self.data)
    
    def minimum(self):
        return self.data[0]

    def insert(self, obj):
        self.data.append(1000000)
        i = len(self.data)-1
        self.data[i] = obj
        node = self.data[i]
        nodeP = self.data[parent(i)]
        while less(0,i) and self.less(node, nodeP):
            swap(self.data, i, parent(i))
            i = parent(i)
            node = self.data[i]
            nodeP = self.data[parent(i)]
    

    def extract_min(self):
        if len(self.data) == 0:
            return 'error underflow'
        m = self.minimum()
        self.data[0] = self.data[len(self.data)-1]
        self.data.pop(len(self.data)-1)
        self.min_heapify(0)
        return m
        
    def min_heapify(self, i):
        l = left(i)
        r = right(i)
        if l < len(self.data) and self.less(self.data[l], self.data[i]):
            smallest = l
        else:
            smallest = i
        if r < len(self.data)  and self.less(self.data[r], self.data[smallest]):
            smallest = r
        if smallest != i:
            swap(self.data, i, smallest)
            self.min_heapify(smallest)
    
    def build_min_heap(self):
        i = len(self.data)/2
        while i > 0:
            self.min_heapify(i)
            i-=1
    
class PriorityQueue:
    def __init__(self, less=less_key):
        self.heap = Heap([], less)

    def __repr__(self):
        return repr(self.heap)

    def push(self, obj):
        self.heap.insert(obj)

    def pop(self):
        return self.heap.extract_min()

if __name__ == "__main__":
    h = Heap([0,2,3,4,5,6,7],less)
    h.insert(1)
    print h.minimum()
    
    h.extract_min()
    print h
    pass

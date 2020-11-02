# Author: Saurav Bhattarai

class Heap:
    def __init__(self, is_max=True):
        self.arr = []
        self.is_max = is_max

    def swap(self, idx1, idx2):
        self.arr[idx1], self.arr[idx2] = self.arr[idx2], self.arr[idx1]

    def compare(self, val1, val2):
        if self.is_max: return val1 < val2
        else: return not(val1 < val2)
        
    def heapify_up(self, idx):
        if idx == 0:
            return
        parent = (idx - 1) // 2
        if self.compare(self.arr[parent], self.arr[idx]):
            self.swap(parent, idx)
            self.heapify_up(parent)
        return
    
    def heapify_down(self, idx):
        idx_child1 = idx * 2 + 1
        idx_child2 = idx * 2 + 2
        if idx_child1 >= len(self.arr) and idx_child2 >= len(self.arr):
            return
        max_child_idx = idx_child1
        if idx_child2 < len(self.arr):
            max_child = idx_child2\
                if self.compare(self.arr[max_child_idx],\
                                self.arr[idx_child2]) else max_child_idx
        if self.compare(self.arr[idx], self.arr[max_child_idx]):
            self.swap(idx, max_child_idx)
            self.heapify_down(max_child_idx)
            
    def push(self, val):
        self.arr.append(val)
        self.heapify_up(len(self.arr) - 1)
        
    def pop(self):
        if len(self.arr) == 0: return None
        ret = self.arr[0]
        self.swap(0, len(self.arr) - 1)
        self.arr.pop()
        self.heapify_down(0)
        return ret

    def __str__(self):
        ret = []
        delim = ''
        ret.append('[')
        for item in self.arr:
            ret.append(delim + str(item))
            delim = ", "
        ret.append(']')
        return ''.join(ret)

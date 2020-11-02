# Author: Saurav Bhattarai

#####################################################################
# An algorithm using the idea of heaps and simple heuristic function
#####################################################################

#####################################################################
# TODO
# pop in heap by email
# learn function in lead
#####################################################################



from lead import *
from heap import *

lead1 = Lead("Victor", 19, 'M', 740, "v@gmail.com")
lead2 = Lead("Jessica", 20, 'F', 760, "j@gmail.com")
lead3 = Lead("Robin", 80, 'F', 800, "s@gmail.com")
max_heap = Heap()
max_heap.push(lead1)
print (max_heap)
max_heap.push(lead2)
print (max_heap)
max_heap.push(lead3)
print (max_heap)

l = max_heap.pop()
print (l)
print (max_heap)

l = max_heap.pop()
print (l)
print (max_heap)

class Node:
  def __init__(self,name,key):
    self.name = name
    self.key = key

class minHeap:
  def __init__(self,List = []):
    self.A = []
    for i in range(len(List)):
      self.A.append(Node(i,List[i]))
      
  def make_heap(self):
    n = len(self.A)
    for k in range(n-1,-1,-1):
      self.heapify_down(k,n)

  def insert(self,name,key):
    self.A.append(Node(name,key))
    self.heapify_up(len(self.A)-1)

  def heapify_up(self,k):
    while k > 0 and self.A[(k-1)//2].key > self.A[k].key:
      self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
      k = (k-1)//2
  
  def delete_min(self):
    if len(self.A) == 0:
      return None
    NodeName = self.A[0].name
    self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
    self.A.pop()
    self.heapify_down(0,len(self.A))
    return NodeName

  def heapify_down(self,k,n):
    while 2*k+1 < n:
      L,R = 2*k+1, 2*k+2
      if L < n and self.A[L].key < self.A[k].key:
        m = L
      else:
        m = k
      if R < n and self.A[R].key < self.A[m].key:
        m = R
      if m != k:
        self.A[k], self.A[m] = self.A[m], self.A[k]
        k = m
      else:
        break

heap = minHeap()
heap.insert(0,6)
heap.insert(1,2)
heap.insert(2,5)
heap.insert(3,1)
heap.insert(4,0)

for i in range(len(heap.A)):
  print(heap.A[i].name, heap.A[i].key)
  
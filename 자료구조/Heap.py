class maxHeap:
  def __init__(self, L=[]):
    self.A = L
  def __str__(self):
    return str(self.A)

  def heapify_down(self, k, n):
    while 2*k+1 < n:
      L,R = 2*k+1, 2*k+2
      if L < n and self.A[L] > self.A[k]:
        m = L
      else:
        m = k
      if R < n and self.A[R] > self.A[m]:
        m = R
      if m!= k:
        self.A[k], self.A[m] = self.A[m], self.A[k]
        k = m
      else:
        break

  def make_heap(self):
    n = len(self.A)
    for k in range(n-1,-1,-1):
      self.heapify_down(k,n)

  def heap_sort(self):
    n = len(self.A)
    for k in range(len(self.A)-1,-1,-1):
      self.A[0], self.A[k] = self.A[k], self.A[0]
      n = n-1
      self.heapify_down(0,n)
  
  def heapify_up(self,k):
    while k > 0 and self.A[(k-1)//2] < self.A[k] :
      self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
      k = (k-1)//2
  
  def insert(self,key):
    self.A.append(key)
    self.heapify_up(len(self.A)-1)

  def delete_max(self):
    if len(self.A) == 0:
      return None
    key = self.A[0]
    self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
    self.A.pop()
    self.heapify_down(0, len(self.A))
    return key

class minHeap:
  def __init__(self, L = []):
    self.A = L
  def __str__(self):
    return str(self.A)

  def heapify_down(self,k,n):
    while 2*k+1 < n:
      L,R = 2*k+1, 2*k+2
      if L < n and self.A[L] < self.A[k]:
        m = L
      else:
        m = k
      if R < n and self.A[R] < self.A[m]:
        m = R
      if m != k:
        self.A[k], self.A[m] = self.A[m], self.A[k]
        k = m
      else:
        break

  def make_heap(self):
    n = len(self.A)
    for k in range(n-1,-1,-1 ):
      self.heapify_down(k,n)
  
  def heapify_up(self,k):
    while k > 0 and self.A[(k-1)//2] > self.A[k]:
      self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
      k = (k-1)//2

  def insert(self,key):
    self.A.append(key)
    self.heapify_up(len(self.A)-1)

  def delete_min(self):
    if len(self.A) == 0:
      return None
    key = self.A[0]
    self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
    self.A.pop()
    self.heapify_down(0,len(self.A))
    return key

A = [int(a) for a in input().split()]
small = maxHeap()
big = minHeap()

median = A[0]
sum_median = median
small_len,big_len = 0,0
for A_ in A:
  if A_ > median:
    big.insert(A_)
    big_len += 1
  elif A_ < median:
    small.insert(A_)
    small_len += 1

  if small_len > big_len:
    big.insert(median)
    median = small.delete_max()
  elif small_len < big_len:
    small.insert(median)
    median = big.delete_min()
  sum_median += median

print(sum_median)
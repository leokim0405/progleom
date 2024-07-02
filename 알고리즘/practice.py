import sys

N, M = map(int,sys.stdin.readline().split())
list_ = [ 0 for i in range(N)]

for j in range(M):
  a,b,c = map(int,sys.stdin.readline().split())
  for k in range(a-1,b):
    list_[k] = c
  print(list_)
    
for x in list_:
  print(x, end=" ")


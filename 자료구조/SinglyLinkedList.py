class Node:
  def __init__(self, key=None):
    self.key = key
    self.next = None
  def __str__(self):
    return str(self.key)
  
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def __len__(self):
    return self.size

  def __iter__(self):
    v = self.head
    while v:
      yield v
      v = v.next
  
  def printList(self): # 변경없이 사용할 것!
    v = self.head
    while(v):
      print(v.key, "->", end=" ")
      v = v.next
    print("None")
    
  def pushFront(self,key):
    newhead = Node(key)
    if self.size == 0:
      self.head = newhead
    else:
      newhead.next = self.head
      self.head = newhead
    self.size += 1
  
  def pushBack(self, key):
    newtail = Node(key)
    if self.size == 0:
      self.head = newtail
    else:
      tail = self.head
      while tail.next != None:
        tail = tail.next
      tail.next = newtail
    self.size += 1
  
  def popFront(self):
    if self.size == 0:
      return None
    else:	 # head 노드의 값 리턴. empty list이면 None 리턴
      value = self.head.key
      self.head = self.head.next
      self.size -= 1
      return value
  
  def popBack(self):
    if self.size == 0:
      return None	# tail 노드의 값 리턴. empty list이면 None 리턴
    else:
      prev, tail = None, self.head
      while tail.next != None:
        prev = tail
        tail = tail.next
      if prev != None:
        prev.next = None
      else:
        self.head = tail.next
      self.size -= 1	
      return tail.key
  
  def search(self, key):
    temp = self.head	# key 값을 저장된 노드 리턴. 없으면 None 리턴
    while temp != None:
      if temp.key == key:
        return temp
      temp = temp.next
    return None
  
  def remove(self, x):
    temp,prev = self.head,None	# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
    while temp != None:
      if temp == x:
        if prev == None:
          self.head = temp.next
        else:
          prev.next = temp.next
        self.size -= 1
        return True
      prev = temp
      temp = temp.next
    return False
  
  def reverse(self):
    if self.size > 1:
      frontNode, currentNode = None, self.head
      while True:
        if currentNode == None:
          break
        currentNode.next, frontNode, currentNode = frontNode, currentNode, currentNode.next
      self.head = frontNode
  
  def findMax(self):
    if self.size == 0:	# self가 empty이면 None, 아니면 max key 리턴
      return None
    else:
      maxKey = self.head.key
      node = self.head
      while node != None:
        if maxKey < node.key:
          maxKey = node.key
        node = node.next
      return maxKey
  
  def deleteMax(self):
    if self.size == 0:	# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
      return None
    else:
      result = self.findMax()
      self.remove(self.search(result))
      return result
  
  def insert(self, k, val):
    if self.size < k:
      self.pushBack(val)
    else:
      start,newNode = self.head, Node(val)
      for i in range(k-1):
        start = start.next
      start.next, newNode.next = newNode, start.next
  
  def size(self):
    return self.size
  
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
  cmd = input().split()
  if cmd[0] == "pushFront":
    L.pushFront(int(cmd[1]))
    print(int(cmd[1]), "is pushed at front.")
  elif cmd[0] == "pushBack":
    L.pushBack(int(cmd[1]))
    print(int(cmd[1]), "is pushed at back.")
  elif cmd[0] == "popFront":
    x = L.popFront()
    if x == None:
      print("List is empty.")
    else:
      print(x, "is popped from front.")
  elif cmd[0] == "popBack":
    x = L.popBack()
    if x == None:
      print("List is empty.")
    else:
      print(x, "is popped from back.")
  elif cmd[0] == "search":
    x = L.search(int(cmd[1]))
    if x == None:
      print(int(cmd[1]), "is not found!")
    else:
      print(int(cmd[1]), "is found!")
  elif cmd[0] == "remove":
    x = L.search(int(cmd[1]))
    if L.remove(x):
      print(x.key, "is removed.")
    else:
      print("Key is not removed for some reason.")
  elif cmd[0] == "reverse":
    L.reverse()
  elif cmd[0] == "findMax":
    m = L.findMax()
    if m == None:
      print("Empty list!")
    else:
      print("Max key is", m)
  elif cmd[0] == "deleteMax":
    m = L.deleteMax()
    if m == None:
      print("Empty list!")
    else:
      print("Max key", m, "is deleted.")
  elif cmd[0] == "insert":
    L.insert(int(cmd[1]), int(cmd[2]))
    print(cmd[2], "is inserted at", cmd[1]+"-th position.")
  elif cmd[0] == "printList":
    L.printList()
  elif cmd[0] == "size":
    print("list has", len(L), "nodes.")
  elif cmd[0] == "exit":
    print("DONE!")
    break
  else:
    print("Not allowed operation! Enter a legal one!")
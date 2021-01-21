# 1. class Node 선언 부분
class Node:
	def __init__(self,key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)
# 2. class DoublyLinkedList 선언부분
class DoublyLinkedList:
	def __init__(self):
		self.head = Node()
		self.size = 0

	def splice(self,a,b,x):
		if a == None or b == None or x == None:
			return
		a.prev.next = b.next
		b.next.prev = a.prev
		x.next.prev = b
		b.next = x.next
		a.prev = x
		x.next = a
		
		'''if self.isEmpty():
			self.head.next ,self.head.prev, a.next, a.prev = a, a, self.head, self.head
			return
		a.prev.next = b.next
		b.next.prev = a.prev
		x.next, a.prev, b.next, x.next.prev = a, x, x.next, b'''
		ap = a.prev
		bn = b.next
		ap.next = bn
		bn.prev = ap
		xn = x.next
		xn.prev = b
		b.next = xn
		a.prev = x
		x.next = a

	def moveAfter(self,a,x):
		self.splice(a,a,x)
		
	def moveBefore(self,a,x):
		self.splice(a,a,x.prev)
		
	def insertAfter(self,a,key):
		newNode = Node(key)
		self.moveAfter(newNode,a)
		
	def insertBefore(self,a,key):
		newNode = Node(key)
		self.moveBefore(newNode,a)
		
	def pushFront(self,key):
		self.insertAfter(self.head,key)
		
	def pushBack(self,key):
		self.insertBefore(self.head,key)
		
	def deleteNode(self, x):
		x.prev.next, x.next.prev = x.next, x.prev
		
	def popFront(self):
		result = self.head.next.key
		self.deleteNode(self.head.next)
		return result
	
	def popBack(self):
		result = self.head.prev.key
		self.deleteNode(self.head.prev)
		return result
	
	def search(self, value):
		finding = self.head.next
		while finding != self.head:
			if finding.key == value:
				return finding
			finding = finding.next
		return None
	
	def first(self):
		return self.head.next.key
	
	def last(self):
		return self.head.prev.key
	
	def isEmpty(self):
		if self.head.next == self.head:
			return True
		else:
			return False
		
	def printList(self):
		if not self.isEmpty():
			print("h", end='')
			printing = self.head.next
			while printing != self.head:
				print(" -> {0}".format(printing.key), end='')
				printing = printing.next
			print(" -> h")
		else:
			print("h")

	def join(self,list2):
		self.splice(list2.head.next, list2.head.prev, self.head.prev)

	def split(self,x):
		list2 = DoublyLinkedList()
		list2.splice(x,self.head.prev,list2.head)
		return list2

L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
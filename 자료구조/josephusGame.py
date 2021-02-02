class Node:
	def __init__(self,key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node()
		self.size = 0
	def splice(self,a,b,x):
		if a == None or b == None or x == None:
			return
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

def josephus(n, k):
 	# DoublyLinkedList 클래스 인스탠스 L을 선언
	L = DoublyLinkedList()
	# 1번부터 n번까지의 key 값을 갖는 노드를 pushBack 함수를 써서 L에 삽입
	for number in range(1,n+1):
		L.pushBack(number)
	# k개의 링크를 따라간 노드를 remove하는 과정을 한 노드만 남을때까지 반복. 
		# 주의: k개의 링크를 따라갈때 dummy노드도 방문될수 있다는 점
	node = L.head.next
	count = 1
	while True:
		if node.next == L.head and node.prev == L.head:
			break
		if node == L.head:
			node = L.head.next
			continue
		if count % k == 0:
			L.deleteNode(node)
		node = node.next
		count += 1
	# 남아 있는 노드의 key를 리턴
	return L.head.next.key

# n과 k를 입력
input_ = input()
n = int(input_.split(' ')[0])
k = int(input_.split(' ')[1])
# n과 k에 대해서 Josephus함수 호출에서 리턴값을 출력
print(josephus(n,k))

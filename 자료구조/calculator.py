class Stack:
	def __init__(self):
		self.items = []
	def push(self, val):
		self.items.append(val)
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
	def __len__(self):
		return len(self.items)
	def isEmpty(self):
		return self.__len__() == 0
	
def get_token_list(expr):
	token_list = []
	start = 0
	end = 0
	expr += '+'
	for n in range(len(expr)):
		if expr[n] == '(':
			token_list.append(expr[n])
			start = n+1
		elif expr[n] in '+-*/^)':
			end = n
			if start != end:
				token_list.append((expr[start:end]))
			token_list.append(expr[n])
			start = n+1
	token_list.pop()
	return token_list
	
def infix_to_postfix(token_list):
	opstack = Stack()
	outstack = []
	#token_list = infix.split(' ')
	# 연산자의 우선순위 설정
	prec = {}
	prec['('] = 0
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 3

	for token in token_list:
		if token == '(':
			opstack.push(token) # ...?
		elif token == ')': # ...?
			while True:
				if opstack.top() == '(':
					opstack.pop()
					break
				else:
					outstack.append(opstack.pop())
		elif token in '+-/*^':
			while not opstack.isEmpty():
				if prec[token] <= prec[opstack.top()]:
					outstack.append(opstack.pop())
				else:
					break
			opstack.push(token)
		else: # operand일 때
			outstack.append(token)
	# opstack 에 남은 모든 연산자를 pop 후 outstack에 append
		# ... ... ...
	while len(opstack) != 0:
		 outstack.append(opstack.pop())	# ... ... ...

	return " ".join(outstack)
	
def calculate(h,op,t):
	if op == '+':
		return h + t
	elif op == '-':
		return h - t
	elif op == '*':
		return h*t
	elif op == '/':
		return h/t
	elif op =="^":
		return h**t
	
def compute_postfix(postfix):
	numlist = Stack()
	token_list = postfix.split(' ')
	for token in token_list:
		if len(token) == 0:
			continue
		elif token in '+-*/^':
			t = float(numlist.pop())
			h = float(numlist.pop())
			numlist.push(calculate(h,token,t))
		else:
			numlist.push(token)
	return numlist.top()
	
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
class deque:
    def __init__(self,s):
        self.item = s
    def append(self,c):
        self.item += c
    def appendleft(self,c):
        self.item = c + self.item
    def pop(self):
        return self.item.pop(-1)
    def popleft(self):
        return self.item.pop(0)
    def __len__(self):
        return len(self.item)
    def right(self):
        return self.item[-1]
    def left(self):
        return self.item[0]

def PalindromeCheck(s):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
    return palindrome

print(PalindromeCheck(input()))
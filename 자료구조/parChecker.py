class stack:
    def __init__(self):
        self.item = []
    def push(self, val):
        self.item.append(val)
    def pop(self):
        try:
            return self.item.pop()
        except IndexError:
            print("Stack i empty")
    def top(self):
        try:
            return self.item[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):
        return len(self.item)

def parChecker(parSeq):
    S = stack()
    for par in parSeq:
        if par == "(":
            S.push(par)
        else:
            try:
                S.pop()
            except IndexError:
                return False
    if len(S) == 0:
        return True
    else:
        return False

        


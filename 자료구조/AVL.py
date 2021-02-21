class Node:
  def __init__(self, key):
    self.key = key
    self.parent = self.left = self.right = None
    self.height = 0
  def __str__(self):
    return str(self.key)
  
class BST:
  def __init__(self):
    self.root = None
    self.size = 0
  def __len__(self):
    return self.size

  def preorder(self, v):
    if v != None:
      print(v.key, end=' ')
      self.preorder(v.left)
      self.preorder(v.right)

  def inorder(self, v):
    if v != None:
      self.inorder(v.left)
      print(v.key, "" ,end = '')
      self.inorder(v.right)

  def postorder(self, v):
    if v != None:
      self.postorder(v.left)
      self.postorder(v.right)
      print(v.key, "" ,end = '')

  def find_loc(self, key):
    if self.size == 0:
      return None
    p = None
    v = self.root
    while v:
      if v.key == key:
        return v
      else:
        if v.key < key:
          p = v
          v = v.right
        else:	# v.key > key
          p = v
          v = v.left
    return p

  def search(self, key):
    p = self.find_loc(key)
    if p and p.key == key:
      return p
    else:
      return None

  def insert(self, key):
    # key가 이미 트리에 있다면 에러 출력없이 None만 리턴!
    v = Node(key)
    if self.size == 0:
      self.root = v
    else:
      p = self.find_loc(key)
      if p and p.key != key:
        if p.key < key:
          p.right = v
        else:
          p.left = v
        v.parent = p
      else:
        return None
    self.size += 1
    temp = v
    while temp != self.root:
      temp.height = max(self.height(temp.left), self.height(temp.right)) + 1
      temp = temp.parent
    self.root.height = max(self.height(self.root.left), self.height(self.root.right)) + 1
    return v

  def heightUpdate(self,v):
    if v != None:
      self.heightUpdate(v.left)
      self.heightUpdate(v.right)
      v.height = max(self.height(v.left), self.height(v.right)) + 1
      
  def deleteByMerging(self, x):
    # 노드들의 height 정보 update 필요
    if x == None:
      return None
    a, b, pt = x.left, x.right, x.parent
    if a == None:
      c = b
    else: # a != None
      c = m = a
      # find the largest leaf m in the subtree of a
      while m.right:
        m = m.right
      m.right = b
      if b:
        b.parent = m

    if self.root == x: # c becomes a new root
      if c:
        c.parent = None
      self.root = c
    else: # c becomes a child of pt of x
      if pt.left == x:
        pt.left = c
      else:
        pt.right = c
      if c:
        c.parent = pt
    self.size -= 1
    self.heightUpdate(self.root)

  def deleteByCopying(self, x):
    # 노드들의 height 정보 update 필요
    if x == None:
      return None
    xl, xr = x.left, x.right
    if xl != None:	#left존재
      search = xl
      while search != None:
        y = search
        search = search.right
      temp = y.key
      if y == x.left:
        x.left = y.left
        if y.left != None:
          y.left.parent = x
        leap = x
      elif y.left != None:
        y.parent.right, y.left.parent = y.left, y.parent
        leap = y.left
      else:
        y.parent.right = None
        leap = y.parent
      x.key = temp
    elif xr != None:	#left는 없지만 right가 있음
      search = xr
      while search != None:
        y = search
        search = search.left
      temp = y.key
      if y == x.right:
        x.right = y.right
        leap = x
        if y.right != None:
          y.right.parent = x
          leap = y
      elif y.right != None:
        y.parent.left, y.right.parent = y.right, y.parent
        leap = y.right
      else:
        y.parent.left = None
        leap = y.parent
      x.key = temp
    else:		#left right 둘다 없음
      leap = x.parent
      if x == self.root:
        self.root = None
      elif x.parent.left == x:
        x.parent.left = None
        x.parent = None
      else:
        x.parent.right = None
        x.parent = None
      
    self.size -= 1
    if self.size == 0:
      self.root = None
    self.heightUpdate(self.root)
    return leap

  def height(self, x): # 노드 x의 height 값을 리턴
    if x == None:
      return -1
    else:
      return x.height

  def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
    # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
    if x == None:
      return None
    temp = x
    if x.right == None:
      if x.parent == None:
        return None
      else:
        while True:
          if temp.parent == None:
            return None
          elif temp.key > temp.parent.key:
            temp = temp.parent
          else:
            return temp.parent
    else:
      temp1, temp2 = x, x.right
      while True:
        if temp1.parent == None:
          temp1 = None
          break
        elif temp1.key > temp1.parent.key:
          temp1 = temp1.parent
        else:
          temp1 = temp1.parent
          break
      while True:
        if temp2.left == None:
          break
        else:
          temp2 = temp2.left
      if temp1 == None:
        return temp2
      elif temp1.key > temp2.key:
        return temp2
      else:
        return temp1

  def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
    # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
    if x == None:
      return None
    temp = x
    temp2 = x.left
    while temp2 != None and temp2.right != None:
      temp2 = temp2.right
    while temp != None:
      if temp.parent != None and temp.parent.key > temp.key:
        temp = temp.parent
      else:
        temp = temp.parent
        break
    if temp == None and temp2 == None:
      return None
    elif temp == None:
      return temp2
    else:
      return temp

  def rotateLeft(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
    if z == None:
      return
    x = z.right
    if x == None:
      return
    xl = x.left
    x.parent = z.parent
    if z.parent != None:
      if z.parent.key > z.key:
        z.parent.left = x
      else:
        z.parent.right = x
    x.left, z.parent, z.right = z, x, xl
    if xl != None:
      xl.parent = z
    
    if z == self.root:
      self.root = x
    self.heightUpdate(self.root)
    
  def rotateRight(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
    if z == None:
      return
    x = z.left
    if x == None:
      return
    xr = x.right
    x.parent = z.parent
    if z.parent != None:
      if z.parent.key > z.key:
        z.parent.left = x
      else:
        z.parent.right = x
    x.right, z.parent, z.left = z, x, xr
    if xr != None:
      xr.parent = z
    
    if z == self.root:
      self.root = x

    self.heightUpdate(self.root)

class AVL(BST):
  def __init__(self):
    self.root = None
    self.size = 0
  
  def rebalance(self, x, y, z):
    # assure that x, y, z != None
    # return the new 'top' node after rotations
    # z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음
    if z.left == y:
      if y.left == x:
        if self.root == z:
          self.root = y
        self.rotateRight(z)
        return y
      else: #y.right == x
        if self.root == z:
          self.root = x
        self.rotateLeft(y)
        self.rotateRight(z)
        return x
    else: #z.right == y
      if y.left == x:
        if self.root == z:
          self.root = x
        self.rotateRight(y)
        self.rotateLeft(z)
        return x
      else: #y.right == x
        if self.root == z:
          self.root = y
        self.rotateLeft(z)
        return y

  def insert(self, key):
    # BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 
    # super(class_name, instance_name).method()으로 호출
    v = super(AVL, self).insert(key)
    # x, y, z를 찾아 rebalance(x, y, z)를 호출
    z, y, x = v.parent, v, None
    while z != None:               
      z, y, x = z.parent, z, y
      if z == None:
        break
      if abs(self.height(z.left) - self.height(z.right)) > 1:
        self.rebalance(x,y,z)
        break
    return v
        
  def delete(self, u): # delete the node u
    v = self.deleteByCopying(u) # 또는 self.deleteByMerging을 호출
    # height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장
    #self.heightUpdate(self.root)
    temp = v
    while temp:
      temp.height = max(self.height(temp.left), self.height(temp.right)) + 1
      temp = temp.parent
    while v:
      if abs(self.height(v.left) - self.height(v.right)) > 1: #균형이 깨졌다면
        z = v
        if self.height(z.left) >= self.height(z.right):
          y = z.left
        else:
          y = z.right
        if self.height(y.left) >= self.height(y.right):
          x = y.left
        else:
          x = y.right
        self.rebalance(x,y,z)
      # v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
      # z - y - x를 정한 후, rebalance(x, y, z)을 호출
      v = v.parent


T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
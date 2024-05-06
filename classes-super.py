class C1:
  def __init__(self):    #constructor
    self.i = 1

class C2():
  def __init__(self):
    super().__init__()  #super -refers to parent
    self.i = 1

class C3():
  def __init__(self):
    super(C3, self).__init__()
    self.i = 1

a = C1()
b = C2()
c = C3()
print(a.i, b.i, c.i)

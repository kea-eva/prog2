class First(object):
  def __init__(self):
    print("First")
    super().__init__()
  def f(self):
    print('f() in First')

class Second(object):
  def __init__(self):
    print("Second")
    super().__init__()
  def f(self):
    print('f() in Second')

class Third(First, Second):
  def __init__(self):
    print("Third")
    super().__init__()
  def g(self):
    print('g() in Third')
    print('calls f() in Second')
    Second.f(self)

a = Third()
a.f()
a.g()

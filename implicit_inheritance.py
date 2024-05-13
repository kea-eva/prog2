class Parent(object):

    def implicit(self):
        print("\n PARENT implicit()\n")

class Child(Parent):    # inheritance from Parent class
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

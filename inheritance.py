class Student:
  def __init__(self, fnavn, enavn):
    self.firstname = fnavn
    self.lastname = enavn

  def printname(self):      # print studentnavn
    print(self.firstname, self.lastname)

# børn arver fra førœlder klass: Student
class IT_student(Student):
  pass

class Design_student(Student):
  pass

#  opret student objekt, bruger printname method:
x = IT_student("Emil", "Olsen")
x.printname()
y = Design_student("Sofie", "Nilsen")
y.printname()

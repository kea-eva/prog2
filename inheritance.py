class Student:
  def __init__(self, fnavn, enavn): # konstruktør
    self.fnavn = fnavn
    self.enavn = enavn

  def printname(self):      # print studentnavn metode
    print(self.fnavn, self.enavn)

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

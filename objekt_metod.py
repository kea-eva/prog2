# objektet har en metode, "sensorfunction()"

class Sensor:
  def __init__(self, navn, vœrdi):     # __init__ funktionen bruges for at skabe vœrdier for objekterne
    self.navn = navn
    self.vœrdi = vœrdi

  def sensorfunction(self):
    print("\n", "Sensorn " + self.navn, " har et vœrdi af", self.vœrdi, "\n")

s1 = Sensor("Temp", 21)     # skaber et objekt
s1.vœrdi = 22               # skift vœrdi af sensor
s1.sensorfunction()         # kører funktionen på s1 objektet

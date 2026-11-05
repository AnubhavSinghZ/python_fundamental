# __init__ Function

class Person:
  def __init__(self, name, age):  #__init__ method
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
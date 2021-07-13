import time
import Person

number=[10,20,30]
print(dir(number))

p=Person.Person('Kang', 45)
print(p.age)
print(p.name)
print(p.getAge())
print(p.total)

john=Person.Person("Jonh Doe", 35)
print(john.name)
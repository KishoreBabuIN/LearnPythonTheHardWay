#Exercise 45: Is-A, Has-A, Objects and Classes
##Animal is-a object 
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ##Dog has-a name
        self.name = name

##Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ##Cat has-a name
        self.name = name

##
class Person(object):
    def __init__(self, name):
        ##Person has-a name
        self.name = name
        
        ##Person has-a pet of some kind
        self.pet = None

##Employee is-a Person
class Employee(Person):
    def __init_(self, name, salary):
        super(Employee, self).__init__(name)
        ##Employee has-a salary
        self.salary = salary

##Fish is-a object
class Fish(object):
    pass

##Salmon is-a Fish
class Salmon(Fish):
    pass

##Halibut is-a Fish
class Halibut(Fish):
    pass

##Rover is-a dog
rover = Dog("Rover")

##Satan is-a Cat
satan = Cat("Satan")

##Mary is-a Person
mary = Person("Mary")

##Frank is-a Employee
frank = Employee("Frank", 120000)

##Frank has-a pet - Rover
frank.pet = rover

##Flipper is-a Fish
flipper = Fish()

##Crouse is-a Salmon
crouse = Salmon()

##Harry is-a Halibut
harry = Halibut()
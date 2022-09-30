"""class Human:
    def __init__(self, name, location):
        self.name = name
        self.Location = location

    def hello(self):
        print("Hello World")
        print("My self ", self.name)
        print("I am from ", self.location)

    def compare(self, others):
        if self.name == others.name:
            return True
        else:
            return False


human = Human("Arun", "Hyderabad")
human1 = Human("Sama", "India")

if human1.compare(human):
    print("They are same")
else:
    print("They are different")

human.hello()
human1.hello()"""

class Car:
    wheels = 4

    # instance Method
    def __init__(self, com, mile):
        self.com = com
        self.mile = mile

    @classmethod
    def info(cls):
        print(f"The car has {Car.wheels} Wheels")


c1 = Car(com="BMW", mile=15)
c2 = Car("AUDI", 10)

Car.wheels = 5
Car.info()

print(f"The {c1.com} car is giving {c1.mile} mileage and having {Car.wheels} Wheels")
print(f"The {c2.com} car is giving {c2.mile} mileage and having {Car.wheels} Wheels")

'''class School:
    name = "'Arun High School'"

    def __init__(self, student, clas):
        self.student = student
        self.clas = clas


school = School("Sama", "9th", "SKODA", 15)
School.name = "Delhi Public School"
school1 = School("'Arun'", "'9th'", "Ford", 20)
print(f"My self {school.student},I am studying in {school.clas} class in the {School.name}")
print(f"My self {school1.student},I am studying in {school1.clas} class in the {School.name}")'''

# Duck typing
'''class Vehicle:

    def speed(self):
        print("The BMW speed is 100km/ph")
        print("The AUDI speed is 150km/ph")



class Car:

    def engine(self, mileage):
        mileage.speed()


mileage = Vehicle()
car1 = Car()
car1.engine(mileage)'''

'''x = 7
y = 8

print(int.__add__(x, y))'''

'''print("Sathi Reddy")'''



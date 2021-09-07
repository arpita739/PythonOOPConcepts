#This Python Object Oriented Tutorial is meant for beginners who have experience with OOP in other programming language and who don't want to exactly read a lot of articles and watch tons of tutorial series but directly, want to dive into programming with Object Oriented Programming

#Class: You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. When a new class instance is created, the instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object.
"""
class Dog:
    species ="husky"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
buddy= Dog("Buddy",9)
print(f"Name of the dog is {buddy.name}")
print(f"Age of the dog is {buddy.age}")
"""

"""class Dog:
    species ="husky"
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.count +=1 #use of class name to call global variable of class Dog
        
    def decription(self):
        return f"Name of dog {self.name} and age is {self.age}"
    def speak(self,sound):
        return f"Sound of dog {sound}"
    
buddy = Dog("Buddy",16)
print(buddy.decription())
print(buddy.speak("wow"))
print (f"The count is {Dog.count}")
"""
"""
class Jackass(Dog):
    def speak(self,sound="bhow"):
        return f"Sound of dog {sound}"

print(buddy.speak())
print(Jack.speak())
"""
#DESTRUCTOR EXAMPLE

"""class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print (class_name,"destroyed")
p1=Point()
p2=p1
p3=p1
print (id (p1),
id(p2),
id(p3))
del p1
del p2
del p3
"""
"""Class Inheritance

class Parot:
    def __init__(self):
        print("Bird is ready")
    def who(self):
        print("Bird")
    def swim(self):
        print("swim")
class Penguin(Parot):
    def __init__(self):
        super().__init__()
        print("penguine parot")
    def whoisThis(self):
        print("Penguine")
    def run(self):
        print("faast")
p1=Penguin()
p1.who()
p1.swim()
p1.run()
p1.whoisThis() """

#Polymorphism
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def fly_test(bird):
    bird.fly()
def swim_test(s):
    s.swim()
#instantiate objects
p1= Parrot()
p2= Penguin()
s1=Parrot()
s2=Penguin()
#passing the object
fly_test(p1)
fly_test(p2)
swim_test(s1)
swim_test(s2)
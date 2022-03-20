'''1. create inheritance using animal Dog relation.


```
for example,
    Animal and Dog both has same habitat so create a method for habitat
```

2. use super() constructor for calling parent constructor.

```
class Animal:
    #code

class Dog(Animal):
    super()-it refers Animal class,now you can call Animal's methods.'''
'''class animals:
    def __init__(self,habitat):
        self.habitat=habitat
    def habitat(self):
        print("lives in amazon")
        print("eat anything")
class dog(animals):
    def habitat(self):
        print("lives in domestic")
        print("friendly with human")
        super(animals)
obj1=animals()
obj2=dog()
#obj2.animal()
obj2.habitat()'''
class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("Woof woof!")


x = Dog()
x.print_habitat()
x.sound()

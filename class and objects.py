'''1. Create a sample class named Employee with two attributes id and name

```
employee :
    id
    name
```
object initializes id and name dynamically for every Employee object created.

```
emp = Employee(1, "coder")
```

2. Use del property to first delete id attribute and then the entire object'''

'''class employe:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def details(self):
        print("employ id:",self.id)
        print("employe name:",self.name)


e1=employe(1,'vijay')
e2=employe(2,'arun')
e3=employe(3,'suja')
e1.details()
e2.details()
e3.details()
del e1.id
try:
    print(e1.id)
except AttributeError:
    print("emp id ot defined")
del e1
try:
    print(e1.name)
except NameError:
    print("emp name deleted")'''


'''1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
```
area = (1/2)*base*height
```

2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
```
rectangle area=length*width
```
If no shape is supplied then it should take triangle as a default shape'''
'''def calculate_area():
    b=int(input("enter base val:"))
    h=int(input("enter height val:"))
    s=input("enter shape:")
    if s=='triangle':
       print('area of triangle is:',(1/2)*b*h)
    elif s=='rectangle':
        print('area of rectangle is:',b*h)
    else:
        print(' default area of triangle is:', (1 / 2) * b * h)
calculate_area()'''
#===========================================================================================================================
'''3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
```
*
**
***
```'''
'''def patter(num):
    for i in range(num):
        for j in range(1+i):
            print(         "*","*"*(num*2),end="")
            
        print("")

patter(4)'''


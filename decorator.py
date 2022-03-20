'''1. Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

2. Create a factorial function which finds the factorial of a number.

3. Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.
```
example:

    factorial(1.354) : raise Exception or print error message
    factorial(-1) : raise Exception or print error message
    factorial(5) : 60'''

def check(f):
    def help(x):
          if x<0:
               print('invalid input')
          else:
               #print("factorial of number:")
               return f(x)
    return help
@check
def factorial(num):
    fact=1
    if num==1:
        return fact
    else:
       return num*factorial(num-1)

res=factorial(4)
print("factorial of number:",res)
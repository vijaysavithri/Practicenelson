'''1. Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.

Example :
```
    integer = [0, 1, 2, 3, 4]
    binary = ["0", "1", "10", "11", "100"]
    binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}'''
'''integer=[1,2,3,4,5]
binary=['1','10','11','100','101']
#dicts=list(zip(integer,binary))
#a= ":".join((dicts))
#print(dicts)
bin_dict={k:v for (k,v) in zip(integer,binary)}
print(bin_dict)'''
#========================================================================================================================================================
'''2. Create a List which contains additive inverse of a given integer list. 
An additive inverse `a` for an integer `i` is a number such that:
```
a + i = 0
```
Example:
```
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1, 1, -2, -3, -5, 0, 7]'''
'''integer = [1, -1, 2, 3, 5, 0, -7]
aditive_inverse=[-1*i for i in integer]
print(aditive_inverse)'''
#======================================================================================================================================================
'''3. Create a set which only contains unique sqaures from a given a integer list.
```
integer = [1, -1, 2, -2, 3, -3]
sq_set = {1, 4, 9}'''
'''integer = [1, -1, 2, -2, 3, -3]
sq_set={i*i for i in integer}
print(sq_set)'''
#===============================================================================================================================================
'''set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
res=set1.difference(set2)
print(res)'''
#======================================================================================================

'''1. Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this'''
'''month=['jan','feb','march','april','may']
exp=[2200,2350,2600,2130,2190]
print(exp[1]-exp[0])
print(sum(exp[0:2]))
print(2000 in exp)
exp.append(1980)
print(exp)
exp[3]=2130+200
print(exp)'''
#--------------------------------------------------------------------------------------------------------------------
''' You have a list of your favourite marvel super heros.
```
heros=['spider man','thor','hulk','iron man','captain america']
```

Using this find out,

    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
       so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
       So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       Do that with one line of code.
    5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)'''
'''heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
print(heros)
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['black panther']
#heros=list(map(lambda x:x.replace('thor','doctor strange'),heros))
#heros.remove('hulk')
print(heros)
heros.sort()
print(heros)'''
#=====================================================================================================
'''3.use filter fuction to find only in int values'''

'''num=[1,2,'3','trg','rrt',3,4]
result=list(filter(lambda x:isinstance(x,int),num))
print(result)'''


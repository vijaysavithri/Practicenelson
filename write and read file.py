#import pandas as pd
'''## Exercise: Python Read Write File
1. [poem.txt](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/poem.txt)
contains famous poem "Road not taken" by poet Robert Frost.
 You have to read this file in your python program and find out words with maximum occurance.'''

#import os
#os.getcwd()
#os.chdir('C:\\Users\\Admin\\Desktop\\networking\\python exersice\\py-master\\Basics\\Exercise\\13_read_write_files\\poem.txt')
'''word={}
with open("poem.txt",'r') as f:
    #text=f.read()
    #print(text)
    for line in f:
        splt=line.split(" ")
        #print(splt)
        for words in splt:
            if words in word:
                word[words]+=1
            else:
                word[words]=1
    #print(word)
#for k,v in word.items():
max_count=max(word.values())
for k,v in word.items():
    if v==max_count:
        print("maximum occarance of word is:==>",k,'==>the count is:',max_count)'''
#==========================================================================================================================

''' [stocks.csv](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/stocks.csv)
 contains stock price, earnings per share and book value. 
 You are writing a stock market application that will process this file and create a new file
with financial metrics such as pe ratio and price to book ratio. These are calculated as,
```
pe ratio = price / earnings per share
price to book ratio = price / book value'''

'''with open("stocks.csv","r") as f,open("output.csv","w") as out:
    out.write("company name,pe ratio,pb ratio\n")
    next(f)
    for line in f:
        tokens=line.split(",")
        #print(tokens)
        stocks=tokens[0]
        price=float(tokens[1])
        erns=float(tokens[2])
        book=float(tokens[3])
        pe_ratio=round(price/erns,2)
        pb_ratio=round(price/book,2)
        out.write(f"{stocks},{pe_ratio},{pb_ratio} \n")
with open("output.csv","r") as o:
         file=o.read()
         print(file)'''









'''num = int(input("enter the the number:"))
word=['zero','one','two','three','four','five','six','seven','eight','nine']
for i in str(num):
    print(word[int(i)])'''
import pandas as pd
df=pd.read_csv("stocks.csv")
print(df)
'''We have following information on countries and their population (population is in crores),

    |Country|Population|
    |-------|----------|
    |China|143|
    |India|136|
    |USA|32|
    |Pakistan|21|
    1. Using above create a dictionary of countries and its population
    2. Write a program that asks user for three type of inputs,
        1. print: if user enter print then it should print all countries with their population in this format,
            ```
            china==>143
            india==>136
            usa==>32
            pakistan==>21
            ```
        1. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
        2. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
        3. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.'''


'''population={'china':143,'india':136,'usa':32,'pakistan':21}
pr=input('enter choice:')
if pr=='print':
    for i in tuple(population):
         print(i,'==>',population[i])
if pr=='add':
    country=input("enter country:")
    peoples=input("enter population:")
    if country in list(population):
        print('already exist')
    else:
        population[country]=peoples
        for i in tuple(population):
            print(i, '==>', population[i])
        #print(population)
if pr=='remove':
    country = input("enter country:")
    if country in population:
        del population[country]
        print(population)
    else:
        print('does not exist')
if pr=='query':
    country=input("query for:")
    print("population of",country,"is",population[country])'''
#===================================================================================================

'''2. You are given following list of stocks and their prices in last 3 days,

    |Stock|Prices|
    |-------|----------|
    |info|[600,630,620]|
    |ril|[1430,1490,1567]|
    |mtl|[234,180,160]|

    1. Write a program that asks user for operation. Value of operations could be,
        1. print: When user enters print it should print following,
            ```
            info ==> [600, 630, 620] ==> avg:  616.67
            ril ==> [1430, 1490, 1567] ==> avg:  1495.67
            mtl ==> [234, 180, 160] ==> avg:  191.33
            ```
        2. add: When user enters 'add', it asks for stock ticker and price. 
        If stock already exist in your list (like info, ril etc) then it will append the price to the list. 
        Otherwise it will create new entry in your dictionary.
        For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks'''
'''sp={'info':[600,630,620],'ril':[1430,1490,1567],'mtl':[234,180,160]}
inp=input("enter input:")
if inp=='value':
    for i in list(sp):
        print(i,"==>",sp[i],"==>","avg:",sum(sp[i])//len(sp[i]))
if inp=='add':
    stk=input("enter stock ticker:")
    price=(input("enter price:"))
    if stk in sp:
        sp[stk].append(price)
        print(sp)
    else:
        sp[stk]=[price]
        print(sp)'''













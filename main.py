
tupleOne = (1,2,3,4,5)
tupleTwo = (1,4,3,7,5)
res = False
checker = 0
for i in tupleOne:
    checker = 0
    for j in tupleTwo:
        checker+=1
        if(checker == 2):
            continue
        if(j == i):
            print(j)

counter = 0
fruits = ('banana','apple','orange','bananaorange')
fruit = input('enter your fruit name')
for i in fruits:
    if fruit == i:
        counter+=1
print(counter)
counter=0
for i in fruits:
    if fruit in i:
        counter+=1
print(counter)

cars = ('bmw','lada','audi','audi','audi')
list_cars = list(cars)
new_tuple = list()
car = input('enter your car')
change_word = input('enter the word for replacement')
for i in list_cars:
        if i != car:
            new_tuple.append(i)
        if i == car:
            i = change_word
            new_tuple.append(i)
cars = tuple(new_tuple)
print(cars)

nums = (1,2,3,11,22,33,44,111,222,333,444,555)
for
















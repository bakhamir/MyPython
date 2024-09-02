
# print(f"+ = {a + b}\n- = {a - b}\n* = {a * b}")

# print(f'{a} {b} = {c}!')
# sum = 0
# beginning = int(input())
# end = int(input())
# itr=  0
# for i  in range (beginning,end):
#    if i % 2 == 0:
#       continue
#    print(i)


# for i  in range (beginning,end + 1):
#    sum += i
#    itr+=1
# print(sum,sum / itr )
#
import array
from re import match




num = int(input('enter the num'))

fac = 1
sum = 0
print(num)

#for i in range(1,num + 1):
#    fac = fac * i
#     sum += fac
#print(sum)

#for i in range(1,num + 1):
#    for j in range(1,i + 1):
#        print(j,end="")
#    print()
#length = int(input('vvedite dlinu'))
#arr1 = array.array('i',[])
#for i in range(0,length):
#   n = int(input())
#   arr1.append(n)


#for i in arr1:
#    if any(i != j for j in range(0, arr1[0])):
#        print(i)

for i in range(1,10):
    if i * i > num:
        break
    print(i * i)


#char = input('enter the char')

#for i in range(num):
#   print("*",end="")
#print('')

#for i in range(num):
#   print(char,end="")

# while True:
#    money = int(input('vvedite summu deneg'))

#    print('welcome to the money converter')

 #   print('1 - rubl')
 #   print('2 - usd')
 #   print('any other - exit')
 #   choice = int(input('vvedite svoi vybor'))
 #   match choice:
 #       case 1:
 #           print(money * 5,'rub')
 #      case 2:
 #           print(money * 480,'usd')
 #       case _:
 #          break













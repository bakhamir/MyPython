
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
from re import match


def facrec(a):
    if a == 0 or a == 1:
        return 1
    return a * facrec(a - 1)

print(facrec(5))


#num = int(input('enter the num'))

#fac = 0
#for i in range(1, num + 1):
#    fac = fac * i
#print(fac)
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

num1 = int(input('enter the first num'))
num2 = int(input('enter the second num'))
choice = 0
win = False

choice = int(input('your guess?'))
for i in range(num1, num2 + 1):
        if (choice == i):
            print( "!"  + str(i) + '!', end=" ")
            continue

        print(i,end=" ")







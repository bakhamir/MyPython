# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

 # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#print('task 1')
#print('Nothing\nwill work\nunless you do')

#print('task 2')
#print('Anyone who\n stops\n    learning is old\n        whether twenty or eighty')

#print('task 3')
#a = int(input('input the first number'))
#b = int(input('input the second number'))
#print("+ =", a + b, "\n- =", a - b, "\n* =", a * b)
from re import match

number = int(input('vvedite pervoe chislo'))
procent = int(input('vvedite procent chtoby otnyat'))
print(number - ((number/100) * procent))

width = int(input('vvedite shirinu'))
height = int(input('vvedite visotu'))
print('ploshad pryamougolnika =>', width * height)

oddOrEven = int(input('proverka na chetnost'))
if(oddOrEven % 2 == 0):
    print(oddOrEven, 'is even')
else:
    print(oddOrEven, 'is odd')

multipleSeven = int(input('proverka na kratnost 7'))
if(multipleSeven % 7 == 0):
    print(multipleSeven, "is multiple 7")
else:
    print(multipleSeven, "is not multiple 7")

firstNum = int(input('vvedite pervoe chislo'))
secondNum = int(input('vvedite vtoroe chislo'))
if(firstNum > secondNum):
    print(firstNum, 'max')
else:
    print(secondNum,'max')
if (firstNum > secondNum):
    print(secondNum, 'min')
else:
    print(firstNum, 'min')

choice = input('select an action')

match choice:
    case '+':
        print(firstNum + secondNum)
    case '-':
        print(firstNum - secondNum)
    case 'mid':
        print((firstNum + secondNum) / 2)
    case '*':
        print(firstNum * secondNum)
    case _:
        print('invalid statement')


#print(f"+ = {a + b}\n- = {a - b}\n* = {a * b}")

#print(f'{a} {b} = {c}!')
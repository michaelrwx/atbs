import sys

def collatz(x):
    if (x%2 == 0):
        x = x // 2
        return(x)
    elif (x%2 == 1):
        x = 3 * x + 1
        return(x)

print('Enter number: ')
number = input()

while(number != 1):
    collatz(int(number))
    print(number)

if(number == 1):
   print('1 acquired')
   sys.exit()








def collatz(x):

    if x % 2 == 0:
        print(x // 2)
        return(x // 2)
    
    elif x % 2 == 1:
        result = 3 * x + 1
        print(result)
        return(result)

number = input("Enter a number: ")
while number != 1:
    number = collatz(int(number)) 

#You pretty much had the program, you just forgot to have this variable change within the variable.

#The program defines the collatz definition. The function is used to print each number.









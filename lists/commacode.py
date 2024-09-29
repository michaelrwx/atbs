#Comma Code
#Write a function that takes a list value as an argument and returns them with all the items separated by a comma and  a space with 'and" inserted before the last item.

spam = ['apples', 'bananas', 'tofu', 'cats']

def commaMaker(stuff):
    for i in range(len(stuff) - 1): #For loop measuring the entire array, -1 to account for it being a list
        print(stuff[i] + ', ', end='')
    print('and ' + stuff[-1])

commaMaker(spam)




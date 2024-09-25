import random #Will be used later! :)

#Lists
#A list is a value that contains multiple values in an ordered sequence.

#animal = ['cat','bat','rat','elephant']

#Values inside the list are called items

#Notating the list above is simple. lets see it in action:

animal = ['cat','bat','rat','elephant']
print(animal[1], animal[3], animal[2], animal[0]) #This will print "bat elephant rat cat"

#Attempting to print "animal[1000]" will result in an IndexError since it is not in range
#Indexes can't be floats

#Lists can have other list values!
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0][1]) # This will print bat....

#an index of -1 is the last value in the list. The -2 is the second to last, and so on.

print(len(spam)) #the len function gives you the length of a list!

#A for loop with a list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i]) #reminder: that i is constantly increasing within the for loop!

#in and not operators are booleans that can let you know if a value is IN or NOT regarding a list

print("=============================================")

#The enumerate function lets you go through the list without having to iterate an i variable over and over
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

#random choice module lets you choose something...at random! Each output of this will be different :)

print(random.choice(supplies))

#Augmented operators
example = 2

#Instead of this bullshit:
example = example + 1
print("This " + str(example) + " fucking sucks because it's lame")
#We do this
example += 1
print("This " + str(example) + " is cool as fuck because it was acquired in a more efficient way!")
# -= subtraction, *= multiplication, /= division, %= modular




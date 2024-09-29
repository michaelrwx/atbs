# Dictionaries!!

#A dictionary is typed with braces {}

myDog = {'size': 'tiny', 'color': 'black', 'disposition': 'chill'}
print(myDog['color'])

#Dictionaries are NOT ordered!

#Dictionary methods

#values() 

for v in myDog.values():
    print(v)

#keys()
for k in myDog.keys():
    print(k)

#items()
for i in myDog.items():
    print(i)


#in or not in can check if something is in a dictionary or not!
print('huge' in myDog.values()) #This generates a false since my dog isn't huge
print('huge' not in myDog.values()) #This generates a true



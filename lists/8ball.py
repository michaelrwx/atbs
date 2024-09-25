import random

messages = ['It is decidedly so', 'Yes, definitely', 'Reply hazy, please try again', 'Ask again later', 'Concentrate and ask again', 'No', 'Outlook not great', 'Very doubtful', 'Joever']

print("What do you need to know?")
q = input()
print(messages[random.randint(0, len(messages) - 1)])



# Computer greeting someone

# Getting the Name
print("Hello, world!")
print("Hello, what is your name?")
myName = input()
print("It's good to meet you," + myName)

# asking how the person is doing
print("Tell me, how has your day been going on a scale of one to five?")
day_rating = int(input())

# Responses
def getAnswer(getNumber):  # answers vary with number
    if getNumber == 1:  # lowest Value
        print('I am sorry to hear that. Hopefully things get better.')
    elif getNumber == 2:
        print('I am sorry to hear that. Hopefully things get better.')
    elif getNumber == 3:
        print('I hope the rest of your day is better.')
    elif getNumber == 4:
        print('Glad to hear that! Keep it up.')
    elif getNumber == 5:  # highest Value
        print('That\'s great to hear! Keep enjoying your day.')

# Way of getting responses 1-5
getAnswer(day_rating)

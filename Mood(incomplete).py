# Computer greeting someone

# Getting the Name
print("Hello, world!")
print("Hello, what is your name?")
myName = input()
print("It's good to meet you," + myName)

# Asking how the person is doing
print("Tell me, how has your day been going on a scale of one to five")
day_rating = int(input())

# Values
terrible = 1
bad = 2
okay = 3
good = 4
great = 5

# Responses
def getAnswer(getNumber):  # answers vary with number
    if getNumber == 1:  # lowest Value
        print('I am sorry to hear that. Hopefully things get better.')
    elif getNumber == 2:
        print('That sounds like a rough day. I hope it gets better.')
    elif getNumber == 3:
        print('I am glad to hear it has been okay.')
    elif getNumber == 4:
        print('That sounds like a good day!')
    elif getNumber == 5:  # highest Value
        print('Wow! I am glad to hear it has been great.')

# Get responses 1-5
getAnswer(day_rating)

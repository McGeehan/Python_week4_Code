# Computer greeting someone

# Getting the Name
print("Hello, world!")
print("Hello, what is your name?")
myName = input()
print("it's good to meet you," + myName)

# asking how the person is doing
print("tell me, how has your day been going on a scale of one to five")
saved_dayinput = input()

# Values
terrible = 1
bad = 2
okay = 3
good = 4
great = 5


# Responses
def getAnswer(getNumber):  # answers vary with number
    if getNumber == 1:  # lowest Value
        print  ('I am sorry to hear that. hopefully things get better.')
    elif getNumber == 2:
        print('I am sorry to hear that. hopefully things get better.')
    elif getNumber == 3:
        print  ('I am sorry to hear that. hopefully things get better.')
    elif getNumber == 4:
        print('I am sorry to hear that. hopefully things get better.')
    elif getNumber == 5:  # highest Value
        print('I am sorry to hear that. hopefully things get better.')


# Way of getting responses 1-5
input(getAnswer)

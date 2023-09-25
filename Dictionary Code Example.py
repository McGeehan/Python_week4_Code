#BIRTHDAY DATABASE 
birthdays = {'Alice': 'April 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} #Dictonary unordered

while True:#While loop Check If conditions are True
    print('Enter a name: (blank to quit)') #Please give a name
    name = input() #Accept name 
    if name == '': #if left Blank then stop
        break
    
    if name in birthdays: #Is this name in the Bday dictionary? 
        print(birthdays[name] + 'is the birthday of' + name)#print the name with the Bday
    else:
        print('I do not have birthday information for ' + name)#If name isn't recognized
        print('what is their birthday?')#What is their birthday for unrecognized name 
        Bday = input()#Accept DOB
        birthdays[name] = Bday #update name in dictionary with Bday variable
        print('birthday database updated')
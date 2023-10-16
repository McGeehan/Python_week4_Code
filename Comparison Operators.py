def find_largest(numbers):
    # start with the first number as the largest
    largest = numbers[0]
    #loop through or iterate through the rest of the numbers
    for num in numbers[1:]:
        #compare each number with the largest number
        if num > largest:
            #if the number is greater, update the largest
            largest = num
    return largest

def find_smallest(numbers): #start with the first number as the smallest
    smallest = numbers[0]
    #loop through the rest of the numbers
    for num in numbers[1:]:
        #compare each number with the smallest number
        if num < smallest:
            #if it's smaller, then update the smallest
            smallest = num
    return smallest

numbers = [55, 2, 69, 23, 202, 596, 33, 11, 7, 83, 78]

largest = find_largest(numbers)
print("the largest number is: ", largest)

smallest = find_smallest(numbers)
print("the smallest number is: ", smallest)
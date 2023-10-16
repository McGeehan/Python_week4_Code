def get_average(scores):  # getting average of the scores
    global score
    total = 0  # variable of total and set to 0
    for score in scores:  # for each score in scores 
        total += score  # count the total and set equal to variable
    average = total / len(scores)  # should be plural # creates an average variable 
    return average  # should return 70


scores = [90, 80, 70, 60, 50]
print('the average score is', get_average(scores))  # should be plural
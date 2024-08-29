"""Given the student's score sheet for sports day, 
you are required to find the runner-up score. You are given scores. 
Store them in a list and find the score of the runner-up.

Input Format
-------------
The input (Enter Number:) should be an array of integers each separated by a space."""

score = input('Enter Number: ').split(" ")


def runnar_up(data):
    array = []
    for i in data:
        array.append(int(i))
    ordered = sorted(array, reverse=True)
    second_position = ordered[1]
    return second_position


print(f"Runnar up score: {runnar_up(score)}")

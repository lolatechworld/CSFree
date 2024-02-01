#!/usr/bin/python3

#How to get access to elements in the score list
goals = [75, 69, 85, 70]

for goal in goals:
    print(f"Before: {goal}")
    #for any goal less than 90, add 10 marks
    if goal < 80:
        goal = goal +10
        goal += 10
print(goal)
#!/usr/bin/python3

#How to get access to elements in the score list
#goals = [75, 69, 85, 70]

#for goal in goals:
#   print(f"Before: {goal}")
    #for any goal less than 90, add 10 marks
#   if goal < 80:
#       goal += 10
#        print(f"After: {goal}")
        

#How to get access to elements in the score list
goals = [75, 69, 85, 70]

#len(goals)
#range(len(goals));
for i in range (len(goals)):#will print the index of the number
    print(f"{i} = {goals[i]}")    
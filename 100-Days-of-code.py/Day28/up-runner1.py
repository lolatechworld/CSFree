#Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#Runner up score is the second highest number in the list
#psudocode
#It receives input and uses the while loop as a seperator
#We are working with a list
#We will be using a sorted function 
#We will output the second number of the list

list = []

while True:
    total_score = input("input total score for each team: ")
    if total_score.lower() == "done":
        break
    print(total_score) 
    list.append(int(total_score))
list.sort()

runner_up = list[-2]
print(f"Our runner_up is {runner_up}")
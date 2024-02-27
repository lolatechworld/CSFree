#Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#Runner up score is the second highest number in the list

list_num = []
num = input("Enter the scores: ").split(" ")
for i in num:
    int(i)
    list_num.append(i)
print(list_num)
max_num = max(list_num)
list_num.remove(max_num)
print(max(list_num))

list = []
max_num = max(list_num)
list_num.remove(max_num)
print(max(list_num))
 Whole Foods Market Tip Distribution Project
# Ergi Masati 
# 8/1/2019 – 11/5/2019 

#-- GOAL --#   
# To develop an algorithm using Python to increase efficiency, improve accuracy, 
# and simplify the Whole Foods Restaurant tip distribution to employees.

ans = "" 
total_hours = 0
name = None
hours = None       # Initializing key variables
list1 = []
list2 = []
i=0

total_tips = int(input("Enter total amount of tips made today: "))
print("Please enter employee names, when done, enter 'DONE'")
while name is None:
    input_value = input("Please enter the employee name: ")
    if input_value == "DONE":                 
        break                # Constructing a list with all employees 
                             # names that appear on Tip Sign-In Sheet
    else:
        list1.append(input_value)
    
while hours is None:
    if i == len(list1):
        break
    else:
        print("Please enter how many hours the indicated employee worked!")
        value = int(input("how many hours did " + list1[i] + " work? "))
        list2.append(value)
        i += 1                      # Constructing a corresponding list keeping
                                    # track of each employee's hours for the day
        total_hours += value

for emp in list1:             # Nested loop to figure out total tip amount of each employee
    for num_hours in list2:
        amount = (total_tips/total_hours) * num_hours
        ans += ("\n" + emp + " made a total of " + str(amount) + " in tips today. \n")
        del list2[0]
        break
    

print(ans)

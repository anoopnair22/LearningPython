#print avg marks in  Maths:
scorecard_dict = {}
#name = input("Enter student name: ")
#score = int(input(f" How much did {name} score in maths: "))
#print(f'{name} scored {score} in Maths')
#scorecard_dict[name] = score
#opt = input(f" Do you want to add another student's score? (Yes/No): ")
#total = score
#i = 1
opt = "Yes"
while opt == "Yes":
    name = input("Enter student name: ")
    score = int(input(f" How much did {name} score in maths: "))
    print(f'{name} scored {score} in Maths')
    opt = input(f" Do you want to add another student's score? (Yes/No): ")
    scorecard_dict[name] = score
#    total = score + total
#    i = i + 1

total = sum(scorecard_dict.values())
avg = total / len(scorecard_dict)
print(f'Average marks in maths for this class is {avg}')




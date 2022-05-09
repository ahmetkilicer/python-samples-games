bill=input("Welcome to the tip calculator!\nWhat was the total bill?\n")
per=input("How much tip would you like to give? 10, 12, or 15?\n")
people=input("How many people to split the bill?\n")
per=int(per)/100+1
result=(float(bill)/int(people))*per
result= round(result,2)
print(f"Each person shoul pay: ${result}")
#If the bill was $150.00, split between 5 people, with 12% tip.
#Format the result to 2 decimal places = 33.60


print(f"*******Welcome to Bill Spliter********\n")
Total_Bill = int(input("Enter the total bill : "))
No_of_people = int(input("Enter the No. of people to be included for Split : "))
Tip_Percentage = (int(input("Enter the tip percentage : "))) / 100

Bill_per_Person = (Total_Bill + (Total_Bill * Tip_Percentage)) / No_of_people

print(f"The Bill per person is ${round(Bill_per_Person, 2)}")







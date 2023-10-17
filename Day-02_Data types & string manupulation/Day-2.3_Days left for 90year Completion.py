'''Create a program using maths and f-Strings that tells us how many days, weeks, months
 we have left if we live until 90 years old.'''


#Code

Age = int(input("Enter your Age : "))
Years_left = 90 - Age
Months_left = Years_left * 12
Weeks_left = Years_left * 52
Days_left = 365 * Years_left

print(f"You have {Days_left} days, {Weeks_left} weeks, and {Months_left} months left.")













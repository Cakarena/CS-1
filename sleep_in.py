## Write a program to accept Weekday and Vacation values.##
## Weekday is True if it is a weekday, and the vacation is True if we are on vacation.## 
## We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.##
print ("This program tells you whether it's appropriate to sleep in or not. Your working week is Monday to Friday.")
print ("Any day from Monday to Friday is a 'weekday'")
x=input("Type 0 if tomorrow is a weekday, 1 if it's the weekend: ")
x=int(x)
y=input("Type 0 if you're not on vacation, 1 if you are on vacation: ")
y=int(y)
sum = (x) + (y)
if sum >= 1:
    print ("Sleep in")
elif sum ==0:
    print ("Don't sleep in")   
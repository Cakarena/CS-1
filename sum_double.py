##Given two int values, return their sum. ##
##Unless the two values are the same, then return double their sum.##

x= input("Enter a number: ")
y= input("Enter a number: ")
x=int(x)
y=int(y)
if x == y:
    sum = (x + y) * 2
    print (sum)   
elif x != y:
    sum = (x + y)
    print (sum)
    
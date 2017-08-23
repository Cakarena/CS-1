## Write a program. We have two monkeys, a an b.##
## Accept the input telling if each is smiling. We are in trouble if both or neither are smiling.## 
## Return True if we are in trouble.##
print ("This program tells you whether we have monkey trouble. If both monkeys A and B are smiling at the same time,")
print ("we have trouble. If both monkeys are not smiling at the same time, we also have trouble'")
x=input("Is Monkey A smiling? Type 0 if she is, type 1 if she is not: ")
x=int(x)
y=input("Is Monkey B smiling? Type 0 if he is, type 1 if he is not: ")
y=int(y)
print ("Do we have monkey trouble?")
sum = (x) + (y)
if sum == 1:
    print ("No, we do not.")
elif sum != 1:
    print ("Yes, we have monkey trouble.")
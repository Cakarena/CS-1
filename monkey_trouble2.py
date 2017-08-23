##We have two monkeys, a and b. Accept the input telling if each is smiling.## 
##We are in trouble if they are both smiling or if neither of them is smiling## 
##Return True if we are in trouble.##
## So this is a correction over monkey_trouble.py##

monkeyA = input('Is Monkey A smiling?').lower()
monkeyB = input('Is Monkey B smiling?').lower()

if monkeyA == "false" and monkeyB == "true":
    print ('False - We have no monkey trouble')
elif monkeyA =="true" and monkeyB == "false":
	print ('False - We have no monkey trouble')
elif monkeyA =="true" and monkeyB == "true":
	print ('True - We have monkey trouble')
elif monkeyA =="false" and monkeyB == "false":
	print ('True - We have monkey trouble') 

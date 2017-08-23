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
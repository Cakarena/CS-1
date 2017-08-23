##Write a program to accept Weekday and Vacation values.##
##Weekday is True if it is a weekday, and the vacation is True if we are on vacation.##
##We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.## 

weekdayFlag = input('Is it weekday?').lower()
vacationFlag = input('Is it vacation?').lower()

if weekdayFlag == "false" or vacationFlag == "true":
    print ('True - Sleep in')
elif weekdayFlag == "true" or vacationFlag == "false":
    print ('False - Dont sleep in')
elif weekdayFlag =="true" or vacationFlag == "true":
	print ("True - Sleep in")
elif weekdayFlag =="false" or vacationFlag == "false":
	print ("True - Sleep in") 
else:
    print ('Incorrect choice, please state either True or False')    
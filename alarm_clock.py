## Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,##
##  and a boolean indicating if we are on vacation, return a string of the form "7:00"##
##  indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00"##
##  and on the weekend it should be "10:00". Unless we are on vacation ##
## -- then on weekdays it should be "10:00" and weekends it should be "off".## 
def vacation_alarm (vacation, day):
    if vacation =="false":
        if day >=1 and day <=5:
            print ("alarm rings at 07.00")
        elif day == 0 or day == 6:
            print ("alarm rings at 10:00")
    elif vacation =="true":
        if day == 0 or day ==6:
            print ("the alarm is off")
        if day >=1 and day <=5:
            print ("alarm rings at 10:00")

v = input("Are you on vacation (True/False)?: ")
d = input("What day is it?: ")
vacation =(v)
day =int(d)
vacation_alarm (vacation, day)  
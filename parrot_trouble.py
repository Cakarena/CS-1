## We have a loud talking parrot. The "hour" input is the current hour time in the range 0..23.##
## We are in trouble if the parrot is talking and the hour is before 7 or after 20.## 
## Return True if we are in trouble.##

print ("The parrot can not be talking between 7 and 20 hours i.e. 7 am and 8pm.")
print ("Let's see if the parrot is in trouble. When time is asked enter military time 0 to 23.59")
parrot_talk = input("Is the parrot talking: ").lower()
hour=input("What time is it now?: ")
hour=float(hour)
if (hour < 23 or hour > 0) and parrot_talk == "false":
    print ("False - not in trouble")
elif (hour < 7 or hour > 20) and parrot_talk == "true": 
    print ("True - in trouble")
else: 
    print ("False - not in trouble")
## You are driving a little too fast, and a police officer stops you.##
## Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.##
##  If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.##
##  If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day,##
##  your speed can be 5 higher in all cases.## 

def caught_speeding(is_birthday,speed):

    if is_birthday == "false":
        if speed <=cau60:
            return ("Result 0 - No ticket F")
        elif speed >= 61 and speed <= 80:
            return ("Result 1 -Small ticket F")           
        elif speed >= 81:
            return ("Result 2 -Big ticket F") 

    elif is_birthday == "true":
        if speed <65:
            return ("Result 0 - No ticket T")
        elif speed >= 65 and speed <= 85:
            return ("Result 1 - Small ticket T")
        elif speed >= 86:
            return ("Result 2 - Big ticket T")     

b = input("Is it your birthday (true/false)?: ").lower()
s = input("How fast are you going: ")
speed =int(s)
is_birthday =(b)
ticket = caught_speeding(is_birthday,speed)
print ("Ticket",ticket)

   
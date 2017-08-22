def nolicense ():
    print("No license to be issued")
def license ():
    print("You have passed your provisional license")   

a=input("Enter your age, use integers: ")
a=float(a)
if a < 16 :
     nolicense ()
if a >= 16 :
    print("Great")
    h=input("Enter the total number of practices hours: ") 
    h=float(h)
    if h < 200 :
        nolicense ()
    if h >= 200:
        license ()      
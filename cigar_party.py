## When squirrels get together for a party, they like to have cigars.##
## A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.##
## Unless it is the weekend, in which case there is no upper bound on the number of cigars.##
## Return True if the party with the given values is successful, or False otherwise ##

weeknd = input("Is it the weekend?: ").lower()
cigars = input("How many cigars are there?: ")
cigars=int(cigars)

if weeknd == "false" and (cigars <= 39): 
    print ("False")
elif weeknd =="false" and (cigars >= 40 and cigars <= 60):
	print ("True")
elif weeknd == "false" and (cigars >= 61):
    print ("False")

elif (cigars <= 39) and weeknd == "true":
    print ("False")
elif (cigars >= 40) and weeknd =="true":
    print ("True")
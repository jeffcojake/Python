## Ask user for age
while True:
    try:    
        age = int(raw_input('Please enter your age.(numerical value)\n'))
        break
    except ValueError:
        print('that was not an integer; try again...\n')
## If age is less than 18 then tell them they are too young
if age < 18:
	print (" Access denied. Sorry, you are not old enough.\n")
## If the user is 18 then grant them access	
elif age == 18:
	print ("Acess granted. You are just old enough to use this program!")
## If user is any age above 18 then grant them access
else:
	print ("Access granted.")

#-----------------------------------------------------------------------
#Written by FrostGW Version 1.0
#This program will ask for a color, then see if you choose the correct color.
#Start Program 
import random
color = (input('What is your color Red, Blue or Green: '))
print('Hello this is a Test of Color')
#Note range of numbers starting from 0. example 0,3 is 0 and 1 and 3.
if random.randrange(0,3)== 0:
    print('Red is it')
elif random.randrange(0,3)== 1:
    print('Blue is it')
else:
	print('Green is it')
print('Thank you for playing. ')
#End Program    
#-----------------------------------------------------------------------
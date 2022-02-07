 
#This program writes a series of random numbers to a file
import random

#create and open the file to write the random numbers
r_file = open(r"C:\Users\psanthi\Downloads\ass-3\auto-random-output.txt", "w" )

#exception handling block, which will avoids non integer input from the user 
try:
    for i in range(int(input('Please enter how many random numbers you want to geenerate?: '))):
        line = str (random.randint (1, 500)) #condition to generate the numbers between 1 to 500
        r_file.write(line) # writes the seris of numbers
        #print(line)
except ValueError:
    print ("Please enter valid integer numbers")

#close the file once the writing is completed
r_file.close() 

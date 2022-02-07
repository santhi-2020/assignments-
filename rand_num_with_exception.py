try:
    r_file = open("D:/ass-3/auto-random-output.txt", 'r')
     
    # This below is the program to read the file 
    sumof_ran_numbers = 0
    count_ran_numbers = 0
    
    for numbers_line in r_file.readlines():
        sumof_ran_numbers += int(numbers_line) #read each line and typecast to int and calulate the sum
        count_ran_numbers += 1 #counter to get the number of random numbers in the file
        line = r_file.readline().rstrip("\n")
    
    #print the results 
    print("The total of the numbers: " + str(count_ran_numbers))
    print("The number of random numbers read from the file: " + str(sumof_ran_numbers))
    
    #close the file once the reading is completed
    r_file.close()     
#exception handling for file not found or file already opened
except IOError as e:
    print ("please close the opened file or please check the file is not exist %s", e)
#exception handling for type casting invalid data to the integer please check  
except ValueError:
    print ("Could not convert data to an integer.")

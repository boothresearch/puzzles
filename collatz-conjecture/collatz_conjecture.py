# This file was edited by Fabio da Silva Soares on 09/18/2019
# For more information, please contact fabio.dasilvasoares@chicagobooth.edu
# 
# This program counts the steps for a number inputted by the user to reach the number 1 following collatz conjecture procedure. 
# 

def steps(number):
    
    try:
        
        i = 0 # Variable that will count the number of steps to reach 1
        x = int(number) # Variable that will store the values of our divisions and multiplications (basically, the operations results)
    
    # Here, we will test whether the input is valid
        
        if x <= 0:
            raise ValueError
        
        # The idea here is to keep the operations going until we reach our desired output: 1
        # So, we will create a while loop that won't end until x == 1
        
            while x != 1:
                i = i + 1 # Each time we repeat the loop, we must add one interaction to the number of steps

                # If x is even, we divide by two and repeat the process
                if x % 2 == 0: 
                    x = x / 2

                # If x is odd, we multiply by 3, add 1, and repeat the procedure
                else:
                    x = 3*x+1

            return "The number of steps required for " +str(number)+ " to reach 1 is: " + str(i)

    except ValueError:
        print(" Ooops, that's not a valid input!\n Your input should be an INTEGER GREATER THAN 0")
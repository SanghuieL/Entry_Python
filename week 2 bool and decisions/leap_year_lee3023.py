"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 2.1 - Leap Year
Date: 09/13/2021

Description:
    This program takes a user input of a year and determines whether that is a leap year. 
    After deterining whether it is a leap year or not, it will output the number of days in February.

Contributors:
    n/a

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""


def main():
    #year input
    year = int(input("Please input a year: "))
    #initial days in february value
    feb = 28

    #check if a multiple of 100 and 400
    if (year % 100 == 0):
        if(year % 400 == 0):
            feb = 29
        else:
            feb = 28

    #check if a multiple of 4
    elif (year % 4 == 0):
        feb = 29
    
    #make sure nothing changed
    else:
        feb = 28
    
    #print number of days statement
    print(f"In the year {year}, February has {feb} days.")
    return


if __name__ == '__main__':
    main()

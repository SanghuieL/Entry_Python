"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 2.3 - Roulette Colors
Date: 09/20/2021

Description:
    The program takes in a user's choice of a pocket from 0-36 in roulette. 
    The program will return the color of the choice of pocket.

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
    #user input pocket number
    pocket = int(input("Please choose a pocket number: "))

    #determine color of pocket
    if (pocket > 36 or pocket < 0):
        print("  Invalid Input!")
        return
    elif (pocket == 0):
        color = "green"
    #1-10 and #19-28
    elif (pocket < 11) or ((pocket >= 19) and (pocket <= 28)):
        if(pocket % 2): #0 = false i.e. not even
            color = "red"
        else:
            color = "black"
    #11-18 and #29-36
    elif (pocket < 19) or ((pocket >= 29) and (pocket <= 36)):
        if (pocket % 2):
            color = "black"
        else:
            color = "red"
    else:
        print ("something wrong")
    '''
    elif (pocket < 29):
        if (pocket % 2):
            color = "red"
        else:
            color = "black"
    
    elif (pocket <= 36):
        if (pocket % 2):
            color = "black"
        else:
            color = "red"
    '''


    #print final statement:
    print(f"  Pocket number {pocket} is {color}.")
    return

if __name__ == '__main__':
    main()

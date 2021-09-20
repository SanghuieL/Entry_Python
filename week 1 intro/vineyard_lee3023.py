"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 1.1 - Vineyard
Date: 08/30/2021

Description:

This program will make a specific calculation for the vineyard owner. 
It will calculate the number of grapevines that will fit in a row given certain parameters.
These parameters are: 
    The amount of space between the vines, in meters
    The amount of space used by an end-post assembly, in meters
    The length of the given row, in meters.

The calculation is already given by the equation V = (R-2E)/S.

The resulting output will be an integer. 

Contributors:
    N/A

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
    #Asking for the user's parameters for the vineyard row.
    print("Enter each of the following quantities in meters.")
    S = float(input("  How much space should be between the vines? "))
    E = float(input("  How wide is the end-post assembly? "))
    R = float(input("  How long is this row? "))

    num = R - 2*E   #Calulation for parentheses
    V = num / S     #full equation calculation

    #Output printed
    print(f"\nThis row has enough space for {int(V)} vine(s).")


if __name__ == '__main__':
    main()

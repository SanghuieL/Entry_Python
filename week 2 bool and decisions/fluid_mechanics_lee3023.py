"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 2.5 - Fluid Mechanics
Date: 09/20/2021

Description:
    This program will find the reynold's number for water flow through a pipe given user parameters.
    It will ask for the velocity of water, diameter of the pipe and a water temperature from 3 options. 
    Using the equation Re = Vd/v, we will calculate the number.

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

    #user parameters
    T = float(input("Enter the temperature in °C as 5, 10, or 15: "))
    if (T == 5 or T == 10 or T == 15):
        pass
    else:
        print("Invalid Input!")
        return
    V = float(input("Enter the velocity of water in the pipe: "))
    d = float(input("Enter the pipe's diameter: "))

    #determine kinetic viscosity and Reynold's number
    v = KV(T)
    R = (V*d) / v

    #print statement
    print (f'At {T:.1f}\u00B0C, the Reynolds number for flow at {V:.1f} m/s in a {d:.1f} m diameter pipe is {R:.2e}.')
    return

def KV(T):
    switch={
        5: float("1.49e-6"),
        10: float("1.31e-6"),
        15: float("1.15e-6")
    }
    return switch.get(T)


if __name__ == '__main__':
    main()

"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 1.3 - Cookie Recipe
Date: 09/06/2021

Description:
    The program will determine how much of each ingredient will be necessary to create the number of cookies a user wants based on a set recipie
    The recipie is based of a 48 cookie recipie, so it will divide the desired number by 48 and multiply each ingredient by that number.

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

    #Asking for the user's parameters for the starting values.
    num = float(input("How many cookies do you want to make? "))
    print(f"To make {num:.0f} cookies, you will need:")

    #calculate the amounts of ingredients
    num /= 48 #make sure this is the multiplier per batch
    sugar = num * 1.75
    butter = num
    flour = 2.5 * num
    #fix spacing error
    #space = 3;
    #if(flour >= 10):
    #    space = 2;


    print(f"   {sugar:.2f} cups of sugar")
    print(f"   {butter:.2f} cups of butter")
    #print(' ' * space + f"{flour:2.2f} cups of flour")
    print(f"{flour:>7.2f} cups of flour") #right align result


if __name__ == '__main__':
    main()

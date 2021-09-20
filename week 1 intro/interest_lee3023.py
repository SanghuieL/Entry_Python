"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 1.2 - Interest
Date: 08/31/2021

Description:
    This program will calculate the value of compond interest.
    By asking the user for the Principal, 
                            annual interest rate, 
                            number of times compounded, 
                            and the length of time, 
    we can calculate the final value of the account.
    The user will enter the interest rate in percent, so the program will divide by 100 to calculate the actual interest.
    The final value will be formatted with commas if it is over 999.


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
    print("Please enter the following quantities.")
    P = float(input("  How much is the initial deposit? "))
    r = float(input("  What is the annual interest rate in percent? "))
    r /= 100
    n = float(input("  How many times per year is the interest compounded? "))
    t = float(input("  How many years will the account earn interest? "))

    div = r/n #fraction calculation
    #print(div)
    num = 1 + div  #Calulation for parentheses
    #print(num)
    exp = num ** (n*t) #parentheses exponent
    #print(exp)
    FV = P * exp     #full equation calculation
    
    #Output printed
    print(f"\nAt the end of {t:.1F} years, this account will be worth ${FV:,.2f}.")


if __name__ == '__main__':
    main()

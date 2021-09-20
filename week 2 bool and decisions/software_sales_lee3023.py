"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 2.2 - Software Sales
Date: 09/20/2021

Description:
    This program takes a user input of the number of packages purchased to calculate the amount of discount one would get with that purchase amount.
    It will also display the total cost after discount. The discount amounts are given by a table.

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
    #user input on number of packages
    package = int(input("How many packages will be purchased: "))
    #switch(package)
    #initial discount value
    discount = 0;
    
    #FInding the amount of discount applied
    if (package < 0):
        print("  Invalid Input!")
        return
    elif (package < 5):
        discount = 0;
        print ("  No discount applied.")
    elif (package < 25):
        discount = 10;
        print (f"  {discount}% discount applied.")
    elif (package < 50):
        discount = 20;
        print (f"  {discount}% discount applied.")
    elif (package < 100):
        discount = 30;
        print (f"  {discount}% discount applied.")
    else :
        discount = 45;
        print (f"  {discount}% discount applied.")
    
    #calulate price total
    total = (100.0 - discount) / 100.0;
    price = (79 * package) * total;
    
    #print price total
    print(f'  The total price for purchasing {package} packages is ${price:,.2f}.')
          
    return
        

"""
#non working switch
def switch(package):
    switch = {
        'no': "No discount applied.",
        'ten': "10%",
        'twenty': "20 %",
        'thirty': "30 %",
        'fourfive': "45 %",
    }
    return switch.get(discount(package), "Invalid Input!")

def discount(n):
    if (n < 0):
        return ""
    if (n < 5):
        return 'no'
    if (n < 25):
        return 'ten'
    if (n < 50):
        return 'twenty'
    if (n < 100):
        return 'thirty'
    else:
        return 'fourfive'
"""
if __name__ == '__main__':
    main()

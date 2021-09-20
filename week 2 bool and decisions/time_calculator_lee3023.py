"""
Author: Seth Lee, lee3023@purdue.edu
Assignment: 2.4 - Time Calculator
Date: 09/20/2021

Description:
    This program takes in a user defined number of seconds and translates it into days, hours, minutes, and seconds. 

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
    #user input time amount
    time = int(input("Please enter a time in seconds: "))

    #calculations number of seconds
    sec = time % 60
    sec_str = f'{sec} second(s)'

    #take out seconds and find minutes
    min = time // 60
    hour = min //60
    min %= 60
    min_str = f'{min} minute(s)'

    #take out hours find days
    day = hour // 24
    hour %= 24
    hour_str = f'{hour} hour(s)'
    day_str = f'{day} day(s)'

    #see which string to use
    if(day == 0):
        set_day = 0
    else:
        set_day = 8
    if(hour == 0):
        set_hour = 0
    else:
        set_hour = 4
    if(min == 0):
        set_min = 0
    else:
        set_min = 2
    if (sec == 0):
        set_sec = 0
    else:
        set_sec = 1
    strings = set_day + set_hour + set_min + set_sec

    print(calc(strings, time, sec_str, min_str, hour_str, day_str))
    return

def calc(strings, time, sec_str, min_str, hour_str, day_str):
    switch = {
        0: 'Immediate.',
        1: f'  {time} seconds is less than one minute.',
        2: f'  {time:,} seconds is: {min_str}.',
        3: f'  {time:,} seconds is: {min_str} and {sec_str}.',
        4: f'  {time:,} seconds is: {hour_str}.',
        5: f'  {time:,} seconds is: {hour_str} and {sec_str}.',
        6: f'  {time:,} seconds is: {hour_str} and {min_str}.',
        7: f'  {time:,} seconds is: {hour_str}, {min_str} and {sec_str}.',
        8: f'  {time:,} seconds is: {day_str}.',
        9: f'  {time:,} seconds is: {day_str} and {sec_str}.',
        10: f'  {time:,} seconds is: {day_str} and {min_str}.',
        11: f'  {time:,} seconds is: {day_str}, {min_str} and {sec_str}.',
        12: f'  {time:,} seconds is: {day_str} and {hour_str}.',
        13: f'  {time:,} seconds is: {day_str}, {hour_str} and {sec_str}.',
        14: f'  {time:,} seconds is: {day_str}, {hour_str} and {min_str}.',
        15: f'  {time:,} seconds is: {day_str}, {hour_str}, {min_str} and {sec_str}.',
    }
    return switch.get(strings)


if __name__ == '__main__':
    main()

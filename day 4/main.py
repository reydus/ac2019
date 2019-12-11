'''
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?
'''

start = 264793
end = 803935

def doublelise(input):
    input = str(input)
    input[-1] = input[-2]
    input = int(input)
    return input

def decreaser(input):
    input = str(input)
    for i in range(0, len(input)-1):
        if int(input[i]) < int(input[i+1])
            input[i+1] = input[i]
    input = int(input)
    return input

start = str(start)


marker = 0
for i in range(0, len(start)-1):
    
    if start[i] == start[i+1]:
        marker = 1
    


        
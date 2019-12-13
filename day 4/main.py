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

startNumber = 264793
endNumber = 803935

def doubleFind(series):
    filtered = []
    for i in series:
        i = str(i)
        for k in range(0, len(i)-1):
            if i[k] == i[k+1]:
                filtered.append(int(i))
                break
    return filtered

def decreased(series):
    filtered = []
    for i in series:
        i = str(i)
        stopFlag = 0
        for k in range(0, len(i)-1):
            if i[k] > i[k+1]:
                #print(i+" is not an option!")
                stopFlag = 1
                break
        if stopFlag == 0:
            filtered.append(int(i))
    return filtered

if __name__ == "__main__":
    combinations = list(range(0, 999999))
    ranged = []
    for i in combinations:
        if i >= startNumber and i <= endNumber:
            ranged.append(i)
    
    doubles = doubleFind(ranged)
    decreas = decreased(doubles)

    print("possible combinations are: "+str(decreas)+"\n")
    print("n = "+str(len(decreas)))
    
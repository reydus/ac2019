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

def noMoreDoubles(series):
    filtered = []
    for i in series:
        i = str(i)
        for k in range(0, len(i)-1):
            if k == 0:
                if i[k] == i[k+1] and not i[k] == i[k+2]:
                    filtered.append(int(i))
                    break
            elif k == len(i)-1:
                if i[k] == i[k-1] and not i[k] == i[k-2]:
                    filtered.append(int(i))
                    break
            else:
                front, back = 0, 0
                if i[k] == i[k+1]:
                    if k <= len(i)-3:
                        if i[k] != i[k+2]:
                            front = 1
                    else:
                        front = 1
                if i[k] == i[k-1]:
                    if k >= 2:
                        if i[k] != i[k-2]:
                            back = 1
                    else:
                        back = 1
                if front+back == 1:
                    filtered.append(int(i))
                    break
    return filtered
'''
        back, front = 0, 0
        for k in range(1, len(i)-1):
            if i[k] == i[k-1]:
                back = 1
            if i[k] == i[k+1]:    
                front = 1
            if back+front == 1:
                filtered.append(int(i))
                break
                   ''' 

'''
    for i in series:
        i = str(i)
        couples = []
        passed = 0
        for k in range(0, len(i)-1):
            if i[k] == i[k+1]:          # check if the next digit is the same (couple)
                if k <= len(i)-3:       # is there enough space leftover for a triplet?
                    if i[k] != i[k+2] and i[k-1] != i[k]:   # is that space taken by a triplet indeed? 
                        passed = 1
                elif k > 0:             # check if there is space for a similar digit behind
                    if i[k] != i[k-1]:  # is it identical to it?
                        passed = 1
        if passed == 1 and not (i[k-1] == i[k] and i[k] == i[k+1]):
            filtered.append(int(i))
            passed = 0
    '''


if __name__ == "__main__":
    print(noMoreDoubles([112233,123444,111122]))
    combinations = list(range(0, 999999))
    ranged = []
    for i in combinations:
        if i >= startNumber and i <= endNumber:
            ranged.append(i)
    
    doubles = doubleFind(ranged)
    decreas = decreased(doubles)
    print("Between "+str(startNumber)+" and "+str(endNumber))
    print("possible combinations are: "+str(decreas[0:5])+"..."+str(decreas[-5:])+"\n") # truncate.
    print("n = "+str(len(decreas))) # no. of possible combinations
    
    print("Part 2...\n")

    noDoubleDoubles = noMoreDoubles(decreas)
    print("possible combinations are: "+str(noDoubleDoubles[0:5])+"..."+str(noDoubleDoubles[-5:])+"\n") # truncate.
    print("n = "+str(len(noDoubleDoubles))) # no. of possible combinations
    
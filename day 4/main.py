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
        length = [0] * len(i)
        skipper = []
        for k in  range(0, len(i)):
            j = 1
            count = 1
            if not k in skipper:
                out = 0
                while k+j <= len(i)-1 and out ==0:
                        if i[k] == i[k+j]:
                            skipper.append(k+j)
                            j += 1
                            count += 1
                        else:
                            out = 1
                if count == 2:
                    filtered.append(int(i))
                    break
    return filtered

def main():
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

if __name__ == "__main__":
    main()
    
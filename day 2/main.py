# opcode program

# three things can be done, starting at index n.
# When n = 1, (n+1) and (n+2) get added and written to (n+3)
# When n = 2, (n+1) and (n+2) get multiplied together and written to (n+3)
# When n = 99, the program halts.

#input
#order = [1,9,10,3,2,3,11,0,99,30,40,50] # 3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50
#order = [1,1,1,4,99,5,6,0,99] # 30,1,1,4,2,5,6,0,99
#order = [2,4,4,5,99,0] # 2,4,4,5,99,9801
#order = [2,3,0,3,99] # 2,3,0,6,99
#order = [1,0,0,0,99] # 2,0,0,0,99
order = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0]
order = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0]

place = 0

while place <= (len(order)-1):
    if order[place] == 1:
        print("Now adding "+str(order[order[place+1]])+" and "+str(order[order[place+2]])+" (indexes "+str(order[place+1])+" and "+str(order[place+2])+" respectively) to index "+str(order[place+3]))
        order[order[place+3]] = order[order[place+1]] + order[order[place+2]]
        place += 4
    elif order[place] == 2:
        print("Now multiplying "+str(order[order[place+1]])+" and "+str(order[order[place+2]])+" (indexes "+str(order[place+1])+" and "+str(order[place+2])+" respectively) to index "+str(order[place+3]))
        order[order[place+3]] = order[order[place+1]] * order[order[place+2]]
        place += 4
    elif order[place] == 99:
        print("Halting process after finding 99 in index "+str(place))
        break
    else:
        print("Heck! I did not understand the input!")
        print("Number "+str(order[place])+" found at index no. "+str(place))
        exit()

print("Success! Completed sequence is "+str(order))
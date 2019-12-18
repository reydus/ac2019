import math

def processInput():
    with open("day 14\\input.txt") as file:
            reactions = file.read()
            reactions = reactions.split("\n")
    react = {}
    for i in reactions:
        i= i.split()
        react[i[-1]] = {"yields": int(i[-2]), "input":0}
        inputt = i[:]   # makes sure that Python doesn't just reference the same object i points at
        inputt.pop(-1)
        inputt.pop(-1)
        inputt.pop(-1)
        outed = {}
        for k in range(0, len(inputt)):
            try:
                int(inputt[k])
            except:
                parsed = []
                for j in inputt[k]:
                    if j != ",":
                        parsed.append(j)
                inputt[k] = "".join(parsed)
                outed[inputt[k]] = int(inputt[k-1])
        react[i[-1]]["input"] = outed
    return react
                

def processReactions(wastebin, reactions, material, no,orecount):
    for i in reactions[material]["input"]:
        needed = reactions[material]["input"][i] * no
        if i != "ORE":
            noReactions = math.ceil(needed/(reactions[i]["yields"]))
            surplus = (reactions[i]["yields"])*noReactions - needed

            if surplus != 0:
                if i in wastebin:
                    wastebin[i] += surplus
                else:
                    wastebin[i] = surplus
            
            wastebin, orecount = processReactions(wastebin, reactions, i, noReactions,orecount)
        else:
            orecount += needed
    return wastebin, orecount
def reclaim(wastebin,reactions):
    passer = 1
    byproducts = {}

    while passer == 1:
        if byproducts != {}:
            for i in byproducts:
                if i in wastebin:
                    wastebin[i] += byproducts[i]
                else:
                    wastebin[i] = byproducts[i]
            byproducts = {}
        passer = 0
        for i in wastebin:
            if reactions[i]["input"].keys() == {"ORE":0}.keys():
                pass
                #print("Tried breaking down "+i+" but it is already prime.")
            else:
                if reactions[i]["yields"] > wastebin[i]:
                    pass
                    #print("Tried breaking down "+i+" but the reverse-reaction isn't feasible with this amount.")
                elif reactions[i]["yields"] <= wastebin[i]:
                    noReactions = wastebin[i]//reactions[i]["yields"]
                    #print("Broke down "+i+" from "+str(wastebin[i])+" to "+str(wastebin[i] - (noReactions * reactions[i]["yields"])))
                    passer = 1
                    wastebin[i] -= noReactions * reactions[i]["yields"]
                    for k in reactions[i]["input"]:
                        if k in byproducts:
                            byproducts[k] += reactions[i]["input"][k] * noReactions
                        else:
                            byproducts[k] = reactions[i]["input"][k] * noReactions
    


    oreReclaimed = 0
    for i in wastebin:
        if wastebin[i] >= reactions[i]["yields"]:
            noReactions = wastebin[i]//reactions[i]["yields"]
            #print(wastebin)
            #print(i)
            oreReclaimed += reactions[i]["input"]["ORE"] * noReactions
            #print("Reclaimed "+str(reactions[i]["input"]["ORE"] * noReactions)+" ORE from "+str(reactions[i]["yields"] * noReactions)+" "+i)
            wastebin[i] -= reactions[i]["yields"] * noReactions
        
    dellist =[]
    for i in wastebin: # prune waste with 0 items
        if wastebin[i] == 0:
            dellist.append(i)
    for i in dellist:
        print("Pruning "+str(i))
        del wastebin[i]

    return wastebin, oreReclaimed

def runEverything(number):
    wastebin = {}
    reactions = processInput()
    orecount = 0
    wastebin,orecount = processReactions(wastebin,reactions,"FUEL",number,orecount)
    wastebin, oreReclaimed = reclaim(wastebin,reactions)
    total = orecount-oreReclaimed
    return total

def convergeAnswer(oreCapacity, initialGuess=5000000):
    totalA = runEverything(initialGuess)
    if totalA > oreCapacity:
        up = initialGuess
        bGuess = (initialGuess*0.5)//1
        totalB = runEverything(bGuess)
        while totalB > oreCapacity:
            bGuess = (initialGuess*0.5)//1
            totalB = runEverything(bGuess)
        down = bGuess
        print("Point A is "+str(initialGuess)+" (upper limit) Point B is "+str(bGuess)+" (bottom limit)")
    elif totalA < oreCapacity:
        down = initialGuess
        bGuess = (initialGuess*1.5)//1
        totalB = runEverything(bGuess)
        while totalB < oreCapacity:
            bGuess = (initialGuess*1.5)//1
            totalB = runEverything(bGuess)
        up = bGuess
        print("Point A is "+str(initialGuess)+" (bottom limit) Point B is "+str(bGuess)+" (upper limit)")

    # iterative that lower/raises points to narrow down to answer, yields a value that gives higher than a trillion, and a value just lower than a trillion.
    while True:
        newPoint = (up-down)//2
        # lift bottom point up, is it out-of-range?
        if runEverything(down+newPoint) < oreCapacity:
            down += newPoint
        # lower upper point down, is it out-of-range?
        elif runEverything(up-newPoint) > oreCapacity:
            up -= newPoint
        if newPoint == 1:
            print("Converged at (up, down) = FUEL("+str(up)+", "+str(down)+") which yields ORE("+str(runEverything(up))+", "+str(runEverything(down))+")")
            return down

def main():
    total = runEverything(1)        # How much ore for 1 fuel
    print("Total "+str(total))

    trillion = 1000000000000        
    initialGuess = trillion//total      # If <<total>> ore gives 1 fuel, then trillion//ore would certainly be closer to the right answer? (allowance for wastage and opportunities)

    convergeAnswer(trillion, initialGuess)

if __name__ == "__main__":
    main()

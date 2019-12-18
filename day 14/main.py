import math


def processInput():
    with open("day 14\input.txt") as file:
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

total = runEverything(1)

print("Total "+str(total))

trillion = 1000000000000
initialGuess = trillion//total
past = initialGuess*1.00
multiplier = 0.5
difference = 2
while difference > 1:
    total = runEverything(initialGuess)
    if total > trillion:
        multiplier *= multiplier
        past = initialGuess*1.00
        initialGuess *= multiplier
        difference = past/initialGuess
        print(initialGuess)
        print(multiplier)
    elif total < trillion:
        past = initialGuess*1.00
        initialGuess *= (1+multiplier)
        difference = past/initialGuess
        print(initialGuess)
        print(multiplier)
print(initialGuess)
#TODO: Difference is having problems due to var mutating when pointing at the same object?




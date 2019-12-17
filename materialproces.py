import math


wastebin = {}
orecount = 0
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
                

def processReactions(wastebin, reactions, material, no):
    global orecount
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
            
            processReactions(wastebin, reactions, i, noReactions)
        else:
            orecount += needed
    return wastebin
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
                print("Tried breaking down "+i+" but it is already prime.")
            else:
                if reactions[i]["yields"] > wastebin[i]:
                    print("Tried breaking down "+i+" but the reverse-reaction isn't feasible with this amount.")
                elif reactions[i]["yields"] <= wastebin[i]:
                    noReactions = wastebin[i]//reactions[i]["yields"]
                    print("Broke down "+i+" from "+str(wastebin[i])+" to "+str(wastebin[i] - (noReactions * reactions[i]["yields"])))
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
            print(wastebin)
            print(i)
            oreReclaimed += reactions[i]["input"]["ORE"] * noReactions
            print("Reclaimed "+str(reactions[i]["input"]["ORE"] * noReactions)+" ORE from "+str(reactions[i]["yields"] * noReactions)+" "+i)
            wastebin[i] -= reactions[i]["yields"] * noReactions
        
    dellist =[]
    for i in wastebin: # prune waste with 0 items
        if wastebin[i] == 0:
            dellist.append(i)
    for i in dellist:
        print("Pruning "+str(i))
        del wastebin[i]

    return wastebin, oreReclaimed

reactions = processInput()
wastebin = processReactions(wastebin,reactions,"FUEL",1)
print(wastebin)
print(orecount)

wastebin, oreReclaimed = reclaim(wastebin,reactions)
print(oreReclaimed)
print(".")
total = orecount-oreReclaimed
print("Total "+str(total))

#initialGuess = 1000000000000//total

#multiplier = 50 # the value is within 50% of the original value.





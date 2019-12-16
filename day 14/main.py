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
                
def compositeThruReact(reactions, material, no, inventory, depth, wastebin):        # material will probably be "FUEL"
    getOutput = reactions[material]
    fuelNo = int(getOutput["yields"])
    needs = getOutput["input"]
    oreCount = 0
    spacing = ["|"] * (depth-1)
    spacing.append("└")
    spacing = "".join(spacing)
    for k in needs:
        if k == "ORE":
            noReactions = math.ceil(no/reactions[material]["yields"])
            print(spacing + "Using "+str(needs["ORE"] * noReactions)+" ORE to make "+str(reactions[material]["yields"] * noReactions)+" "+str(material))
            surplus = reactions[material]["yields"] *noReactions - no
            if surplus != 0:
                if material in wastebin:
                    wastebin[material] += surplus
                else:
                    wastebin[material] = surplus

            if material in inventory:
                inventory[material] += reactions[material]["yields"] *noReactions

            else:
                inventory[material] = reactions[material]["yields"] *noReactions

        else:
            noReactions = math.ceil(no/reactions[material]["yields"])
            print(spacing + "Using "+str(needs[k]*noReactions)+" "+k+" to make "+str(reactions[material]["yields"])+" "+str(material))
            surplus = reactions[material]["yields"]*noReactions - no
            
            if surplus != 0:
                if material in wastebin:
                    wastebin[material] += surplus
                else:
                    wastebin[material] = surplus
            depth += 1

            inventory, wastebin = compositeThruReact(reactions, k, needs[k]*math.ceil(no/reactions[material]["yields"]), inventory, depth, wastebin)

    
    return inventory, wastebin
    
def sumOre(reactions, inventory, wastebin):
    sum = 0
    for prime in inventory:
        oreProduced = reactions[prime]["input"]["ORE"]
        noReactions = math.ceil(inventory[prime]/reactions[prime]["yields"])
        surplus = noReactions * reactions[prime]["yields"]
        if prime in wastebin:
            wastebin[prime] += surplus
        else:
            wastebin[prime] = surplus

        maximumProduct = noReactions * oreProduced
        sum += maximumProduct
    return sum, wastebin

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

def main():
    reactions = processInput()
    print(reactions)
    inventory = {}
    wastebin = {}
    inventory, wastebin = compositeThruReact(reactions, "FUEL", 1, inventory, 0, wastebin)
    wastebin, moreOre = reclaim(wastebin,reactions)
    
if __name__ == "__main__":
    main()


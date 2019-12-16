import math


def processInput():
    with open("day 14\input.txt") as file:
            reactions = file.read()
            reactions = reactions.split("\n")
    react = {}
    for i in reactions:
        #react = {}
        #react[reactions[-1]] = {"no": reactions[-2], "input"}
        i= i.split()
        react[i[-1]] = {"yields": int(i[-2]), "input":0}
        inputt = i[:]   # makes sure that Python doesn't just reference the same object i points at
        inputt.pop(-1)
        inputt.pop(-1)
        inputt.pop(-1)
        outed = {}
        #mix = i.split
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
                
def compositeThruReact(reactions, material, no, inventory):        # material will probably be "FUEL"
    getOutput = reactions[material]
    fuelNo = int(getOutput["yields"])
    needs = getOutput["input"]
    #for k in needs:
    #    needs[k] *= math.ceil(inventory[k]/reactions[k]["yields"])
    oreCount = 0
    for k in needs:
        #if k.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        if k == "ORE":
            #print(aaa)
            if material in inventory:
                inventory[material] += no
            else:
                inventory[material] = no
        else:
            inventory = compositeThruReact(reactions, k, needs[k]*math.ceil(no/reactions[material]["yields"]), inventory)

    
    return inventory
    
def sumOre(reactions, inventory):
    sum = 0
    for prime in inventory:
        oreProduced = reactions[prime]["input"]["ORE"]
        noReactions = math.ceil(inventory[prime]/reactions[prime]["yields"])
        maximumProduct = noReactions * oreProduced
        sum += maximumProduct
    return sum



def main():
    reactions = processInput()
    print(reactions)
    inventory = {}
    print(compositeThruReact(reactions, "FUEL", 1, inventory))
    print(sumOre(reactions, inventory))

if __name__ == "__main__":
    main()
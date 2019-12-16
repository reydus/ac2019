wastebin = {'VPVL': 2, 'RAM': 2, 'R': 3, 'AM': 1}
wastebin["FUEL"]=72
reactions = {'VPVL': {'yields': 3, 'input': {'ORE': 150}}, 'FUEL': {'yields': 1, 'input': {'VPVL': 7, 'RAM': 2}}, 'RAM': {'yields': 3, 'input': {'R': 2, 'AM': 3}}, 'R': {'yields': 5, 'input': {'ORE': 200}}, 'AM': {'yields': 2, 'input': {'ORE': 100}}}

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
print(reclaim(wastebin,reactions))
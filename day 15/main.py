
def processInput():
    with open("C:\\Users\\raymo\\Desktop\\code advent\\repo\\ac2019\\day 15\\input.txt") as file:
            reactions = file.read()
            reactions = reactions.split("\n")
    react = {}
    for i in reactions:
        #react = {}
        #react[reactions[-1]] = {"no": reactions[-2], "input"}
        i= i.split()
        react[i[-1]] = {"yields": i[-2], "input":0}
        inputt = i[:]   # makes sure that Python doesn't just reference the same object i points at
        inputt.pop(-1)
        inputt.pop(-1)
        inputt.pop(-1)
        for k in inputt:
            k.replace(",","")
        outed = {}
        #mix = i.split
        for k in range(0, len(inputt)):
            try:
                int(inputt[k])
            except:
                outed[inputt[k]] = int(inputt[k-1])
        react[i[-1]]["input"] = outed
    return react
                
def compositeThruReact():
    return None
    


def main():
    reactions = processInput()
    print(reactions)
    compositeThruReact()

if __name__ == "__main__":
    main()
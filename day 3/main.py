import sys,os

# temporarily disable my own prints to quieten functions
'''
# Disable
def block#print():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enable#print():
    sys.stdout = sys.__stdout__
'''

# inputs
alpha = "R995,U671,R852,U741,R347,U539,R324,U865,R839,U885,R924,D983,R865,D823,R457,U124,R807,U941,R900,U718,R896,D795,R714,D129,R465,U470,L625,U200,L707,U552,L447,D305,L351,D571,L346,D38,L609,U581,L98,D707,R535,D332,L23,D630,L66,U833,L699,D445,L981,D81,L627,U273,R226,D51,L177,D806,R459,D950,R627,U462,L382,D847,R335,D573,L902,D581,L375,D288,R26,U922,R710,D159,R481,U907,L852,U926,L905,D140,L581,U908,R158,D955,R349,U708,R196,D13,R628,D862,L899,U50,L56,D89,L506,U65,R664,D243,L701,D887,L552,U665,L674,U813,L433,U87,R951,D970,R914,D705,R79,U328,L107,D86,L307,U550,L872,U224,L595,D600,R442,D426,L139,U528,R680,U35,L951,D275,L78,U113,L509,U821,R150,U668,L981,U102,L632,D864,R636,D597,R385,U322,R464,U249,L286,D138,L993,U329,R874,D849,R6,D632,L751,U235,R817,D495,L152,D528,R872,D91,R973,D399,L14,D544,R20,U54,L793,U90,L756,D36,R668,D221,L286,D681,L901,U312,R290,D874,L155,U863,R35,D177,R900,D865,R250,D810,L448,D648,L358,U308,R986,D562,L112,D858,R77,D880,L12,U702,L987,D662,R771,U6,R643,U845,R54,U987,L994,D878,L934,U805,L85,D760,L775,D578,L557,U544,L522,U495,L678,D68,R615,U700,L415,U597,L964,D858,R504,U805,L392,U140,L721,D215,L842,U929,L30,U64,L748,D136,R274,D605,R863,U460,L354,U78,R705,D298,L456,U117,R308,D186,L707,D367,R824,U965,L162,D19,R950,D582,R911,D436,L165,U506,L186,D906,L69,U412,R810,U13,L350,U314,R192,U963,L143,D937,L685,D574,R434,D937,L365,U646,L741,U703,L66,U959,L103,U799,L480,U340,R981,U96,L675,U662,R536,U15,R171,U382,R396,D431,L922,D662,R365,D921,R915"
beta = "L999,D290,L462,D773,L687,D706,L785,D219,R102,U307,L466,D166,R11,D712,L675,D844,R834,U665,R18,D91,R576,U187,L832,D969,L856,U389,R275,D587,L153,U329,R833,U762,R487,U607,R232,D361,R301,D738,L121,D896,R729,D767,R596,U996,R856,D849,R748,D506,L949,U166,R194,D737,L946,D504,L908,D980,L249,U885,R930,D910,R860,D647,L985,U688,L695,U207,L182,D444,R809,D394,R441,U664,L721,U31,R690,U597,R694,U942,R878,U320,R874,U162,L840,U575,L602,U649,L337,D775,L316,D588,R603,D175,L299,D538,R117,U213,L542,D429,R969,D641,R946,D373,L406,D119,R58,D686,R460,U906,L303,D13,L209,D546,R33,D545,R806,U615,R416,D294,L932,D877,R270,U350,R40,U720,L248,D13,L120,D657,L787,U313,R93,U922,R330,D184,L595,D578,R144,D213,L827,U787,R41,D142,R340,D733,L547,U595,L49,U652,L819,D691,R871,D628,R117,U880,L140,U736,L776,U151,R781,U582,R438,D382,R747,D390,R956,U44,L205,U680,R775,D152,L8,D80,R730,U922,L348,U363,L44,D355,R556,D880,R734,U60,R102,U776,L822,D732,L332,D769,L272,D784,R908,U58,L252,U290,R478,D192,R638,U548,R169,D946,L749,D638,L962,U844,R458,D283,R354,U95,L271,U738,R764,U757,R862,U176,L699,D810,L319,U866,R585,U743,L483,D502,R904,D248,L792,D37,R679,U607,L439,U326,L105,U95,L486,D214,R981,U260,R801,U212,L718,U302,L644,D987,L73,U228,L576,U507,L231,D63,R871,U802,R282,D237,L277,U418,R116,U194,R829,U786,L982,D131,R630,U358,R939,D945,L958,D961,R889,U949,L469,D980,R25,D523,L830,U343,R780,U581,R562,U115,L569,D959,R738,U299,L719,U732,L444,D579,L13,U242,L953,U169,R812,D821,R961,D742,R814,D483,R479,D123,L745,D892,L534"

# FIRST TEST SET, RESULT DISTANCE IS 6, AT POINT NUMBER 2.
#alpha = "R8,U5,L5,D3"
#beta = "U7,R6,D4,L4"


# SECOND TEST SET, RESULT DISTANCE IS 159, AT POINT NUMBER ?? MINIMUM STEPPING IS 610
#alpha = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
#beta = "U62,R66,U55,R34,D71,R55,D58,R83"

# THIRD TEST SET, RESULT DISTANCE IS 135, AT POINT NUMBER ?? MIN STEPPING IS 410
#alpha = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
#beta = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

#alpha = "R8,U5,L5,D3"
#beta = "U7,R6,D4,L4"

alpha = alpha.split(",")
beta = beta.split(",")

""" 
let's employ a cartesian coordinate system where:

"U" is towards positive y
"D" is towards negative y
"L" is towards negative x
"R" is towards positive x

in such way, we can define a path as a series of points,

for U5,L6,D3,L3:
    path = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[-1,5],[-2,5],[-3,5],[-4,5],[-5,5],[-6,5],[-6,4],[-6,3],[-6,2],[-7,2],[-8,2],[-9,2]]

in such way, another path, slightly shorter of R2,U2,L3:
    path2 = [[0,0],[1,0],[2,0],[2,1],[2,2],[1,2],[0,2],[-1,2]]

the paths have a "common point" of [0,2]. E.g, an intersection.

Find ALL the intersections (all common coordinates between both paths)
Calculate their cab distance by assuming abs(x)+abs(y) (FUN FACT: Manhattan distance is the same for abs(x)+abs(y), abs(y)+abs(x), and a interval-based-almost-pythagoras length.

 """


def direction2path(direction):
    #block#print()
    location = [0,0] # begins at zero
    path = [location]
    for i in range(0, len(direction)):
        
        # Transform movement "U552" to relative direction vector (0,+552), D20 = (0,-20)
        deltaCoordinate = [0,0]

        # "controllerRange" is a +/-1 that determines the direction of the travel. Due to Range(x) using inclusive for the first parameter and exclusive for the second one, this needs to be adopted.
        ##print("Processing movement "+str(direction[i][0]))
        controllerRange = 0
        if (direction[i][0]) == "U":
            deltaCoordinate[1] += int(direction[i][1:])
            controllerRange = 1
        elif direction[i][0] == "D":
            deltaCoordinate[1] += - int(direction[i][1:])
            controllerRange = -1
        elif direction[i][0] == "R":
            deltaCoordinate[0] += int(direction[i][1:])
            controllerRange = 1
        elif direction[i][0] == "L":
            deltaCoordinate[0] += - int(direction[i][1:])
            controllerRange = -1
        
        #print("delta = "+str(deltaCoordinate))

        # Apply transformation to last point on path
        #print("Current path "+str(path))
        current = [path[-1][0]+deltaCoordinate[0]]
        current.append(path[-1][1]+deltaCoordinate[1])
        #print("Endpoint is "+str(current))
        # Append the ending point to the path
        path.append(current)

   # enable#print()
    return path

def intersect(firstvect, secondvect):
        # find whether two lines defined by two points intersect.
        
        # ASSUMPTIONS: at no part in either paths do they travel parallel through the same points.
        # (continuous intersection)
        # intersections only happen in 90 degree crossings.

        # Skip calculations if vectors are parallel to one another.
        if (
            (firstvect[0][0] == firstvect[1][0] and     #PARALLEL IN X
            secondvect[0][0] == secondvect[1][0]) or 
            (firstvect[0][1] == firstvect[1][1] and     #PARALLEL IN Y
            secondvect[0][1] == secondvect[1][1])
            ):
            #print("Vectors are parallel")
            return "Parallel"
        
        # true if first vector moves parallel to x-axis and second parallel to y-axis
        if firstvect[0][0] == firstvect[1][0]: 
            #print("First vector changes on y")
            # acknowledge the range of change in y direction
            a = firstvect[0][1]
            b = firstvect[1][1]
            c = int((b-a)/abs(b-a))
            firstmove = range(a,b+c,c)
            '''
            for i in firstmove:
                #print(i)
            '''
            intersectPoint = ["null", "null"]
            a = secondvect[0][1]
            if a in firstmove:
                intersectPoint[1] = a

            ### Find if other index is within range of intersection
            a = secondvect[0][0]
            b = secondvect[1][0]
            c = int((b-a)/abs(b-a))
            secondmove = range(a,b+c,c)
            
            a = firstvect[0][0]
            if a in secondmove:
                intersectPoint[0] = a
                
            if intersectPoint[0] == "null" or intersectPoint[1] == "null":
                ##print("Error!")
                return "No intersection"
            return intersectPoint
            
        # true if first vector moves parallel to y-axis and second parallel to x-axis
        elif firstvect[0][1] == firstvect[1][1]:
            #print("First vector changes on x")
            # acknowledge the range of change in y direction
            a = firstvect[0][0]
            b = firstvect[1][0]
            c = int((b-a)/abs(b-a))
            firstmove = range(a,b+c,c)
            '''
            for i in firstmove:
                #print(i)
            '''
            intersectPoint = ["null", "null"]
            a = secondvect[0][0]
            if a in firstmove:
                intersectPoint[0] = a

            ### Find if other index is within range of intersection
            a = secondvect[0][1]
            b = secondvect[1][1]
            c = int((b-a)/abs(b-a))
            secondmove = range(a,b+c,c)
            
            a = firstvect[0][1]
            if a in secondmove:
                #print("intersect = "+str(intersectPoint))
                intersectPoint[1] = a
                

            if intersectPoint[0] == "null" or intersectPoint[1] == "null":
                ##print("Error!")
                return "No intersection"
            return intersectPoint

#############################################################################

###print(alpha)
##print("Maps to\n")
alphapath = direction2path(alpha)
##print("alphapath "+str(alphapath))


##print(beta)
##print("Maps to\n")
betapath = direction2path(beta)
##print("betapath "+str(betapath))
'''
#find common points
for i in range(0, len(alphapath)):
    type(alphapath[i][0]) == int
    #print(i)
'''
##print("Now for everything...")
results = []
for i in range(0, len(alphapath)-1):
    for k in range(0, len(betapath)-1):
        selectionAlpha = [alphapath[i],alphapath[i+1]]
        selectionBeta = [betapath[k],betapath[k+1]]
        #print(selectionAlpha)
        #print(selectionBeta)
        
        result = intersect(selectionAlpha,selectionBeta)
        
        # The function returns parallel encounters, non-intersections and intersections. (string, string, list respectively.)
        if type(result) == list:
            #print("passed result of "+str(result)+" from input "+str(selectionAlpha)+" and "+str(selectionBeta))
            results.append(result)
        
        #print(result)
        #print("next...")
#print(results)


'''
intersection = []
for i in alphapath:
    for k in betapath:
        if i == k:
            #print("Found intersection at "+str(k))
            intersection.append(i)
intersection.pop(0) # remove origin intersection from the list
'''
#find manhattan distance
manhattan = []
for i in results:
    distance = abs(i[0])+abs(i[1])
    manhattan.append(distance)

#_ = manhattan.pop(0)
#print("Distances are "+str(manhattan))

#report min. manhattan distance

if manhattan[0] == 0:
    minDistance = [manhattan[1], 1]
else:
    minDistance = [manhattan[0], 0]

#minDistance = [manhattan[0], 0]
for i in range(0, len(manhattan)):
    if manhattan[i] < minDistance[0]:
        minDistance[0] = manhattan[i]
        minDistance[1] = i
    elif manhattan[i] == minDistance[0] and not manhattan[i] == manhattan[0]: # Report if it has found two points with the same manhattan distance, unless it is the initial guess.
        print("Equal distances found! "+str([manhattan[i],i]))
print("Minimum manhattan is "+str(minDistance)+"(Distance, index (results -1)")

#### PART 2: FIND STEPS. ####
'''
defining a path as a set of vectors (lines between two cartesian points), as such

alphapath = [[0,0],[0,5],[3,5]]

for a path that goes 5 up and then 3 right ("U5,R3")

let an intersection point with another wire have cartesian coordinates of [2,5]

this point lies on the last leg of the alphapath: [0,5] -> [3,5]
'''

def getStep(path, point):
    step = 0
    #counter = 0
    for i in range(0, len(path)-1):
        startpoint = path[i]
        endpoint = path[i+1]
        if startpoint[0] != endpoint[0]: # x has changed, leg is parallel to x axis.
            a = startpoint[0]
            b = endpoint[0]
            c = int((b-a)/abs(b-a))
            
            if (point[0] in range(a,b+c,c)) and (point[1] == startpoint[1]):
                step += abs(point[0]-a)
                #counter += 1
                #print("counter = "+str(counter))
                return step
            else:
                step += abs(b-a)
                #counter += 1
        
        elif startpoint[1] != endpoint[1]: # y has changed, leg is parallel to y axis.
            a = startpoint[1]
            b = endpoint[1]
            c = int((b-a)/abs(b-a))
            
            if (point[1] in range(a,b+c,c)) and (point[0] == startpoint[0]):
                step += abs(point[1]-a)
                #counter += 1
                #print("counter = "+str(counter))
                return step
                
            else:
                step += abs(b-a)
                #counter += 1

    return step

#print(results)

stepper = []
for i in results:
    alphaStep = getStep(alphapath,i)
    betaStep = getStep(betapath,i)
    stepper.append(alphaStep+betaStep)

#print(stepper)

#report min. stepping distance
#_ = stepper.pop(0) # remove step at point (0,0)

# if both cables start parallel, the first intersection is not (0,0), this result wasn't filtered out until now.
if stepper[0] == 0:
    minStep = [stepper[1], 1]
else:
    minStep = [stepper[0], 0]


for i in range(0, len(stepper)):
    if stepper[i] < minStep[0]:
        minStep[0] = stepper[i]
        minStep[1] = i
    elif stepper[i] == minStep[0] and not stepper[i] == stepper[0]: # Report if it has found two points with the same stepping count, unless it is the initial guess.
        print("Equal stepping found! "+str([stepper[i],i]))
print("Minimum stepping count is "+str(minStep)+"(steps, index (stepper -1)")

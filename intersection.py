alpha = [[0,0],[0,4],[5,4]]#,[5,6],[2,6],[2,2]]
#alpha = [alpha[1],alpha[2]]
beta = [[0,0],[-1,0],[-1,1],[-2,1],[-2,3],[2,3],[2,6]]
#beta = [beta[5],beta[6]]
'''
for i in range(0, len(alpha)):
    alphavect = [alpha[i],alpha[i+1]]
    betavect = [beta[i],beta[i+1]]
    intersect(alphavect,betavect)
'''
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
            print("Vectors are parallel")
            return "Parallel"
        
        # true if first vector moves parallel to x-axis and second parallel to y-axis
        if firstvect[0][0] == firstvect[1][0]: 
            print("First vector changes on y")
            # acknowledge the range of change in y direction
            a = firstvect[0][1]
            b = firstvect[1][1]
            c = int((b-a)/abs(b-a))
            firstmove = range(a,b+c,c)
            '''
            for i in firstmove:
                print(i)
            '''
            intersectPoint = []
            a = secondvect[0][1]
            if a in firstmove:
                intersectPoint = ["null", a]

            ### Find if other index is within range of intersection
            a = secondvect[0][0]
            b = secondvect[1][0]
            c = int((b-a)/abs(b-a))
            secondmove = range(a,b+c,c)
            
            a = firstvect[0][0]
            if a in secondmove:
                intersectPoint[0] = a
                
            for j in intersectPoint:
                if j == "null":
                    #print("Error!")
                    return "No intersection"
                return intersectPoint
            
        # true if first vector moves parallel to y-axis and second parallel to x-axis
        elif firstvect[0][1] == firstvect[1][1]:
            print("First vector changes on x")
            # acknowledge the range of change in y direction
            a = firstvect[0][0]
            b = firstvect[1][0]
            c = int((b-a)/abs(b-a))
            firstmove = range(a,b,c)
            
            intersectPoint = []
            a = secondvect[0][0]
            if a in firstmove:
                intersectPoint = [a, firstvect[0][1]]

            ### Find if other index is within range of intersection
            a = secondvect[0][1]
            b = secondvect[1][1]
            c = int((b-a)/abs(b-a))
            secondmove = range(a,b+c,c)
            
            a = firstvect[0][1]
            if a in secondmove:
                intersectPoint[1] = a
                
            for j in intersectPoint:
                if j == "null":
                    #print("Error!")
                    return "No intersection"
                return intersectPoint
'''
print("Alpha ="+str(alpha))
print("Beta ="+str(beta))
print(intersect(alpha,beta))
'''
print("Now for everything...")
results = []
for i in range(0, len(alpha)-1):
    for k in range(0, len(beta)-1):
        selectionAlpha = [alpha[i],alpha[i+1]]
        selectionBeta = [beta[k],beta[k+1]]
        print(selectionAlpha)
        print(selectionBeta)
        
        result = intersect(selectionAlpha,selectionBeta)
        results.append(result)
        print(result)
        print("next...")
print(results)

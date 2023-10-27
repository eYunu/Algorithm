import time

PRINT_LVL = 1

def dprint(any, lvl):
    if (lvl <= PRINT_LVL) and (lvl > 0):
        print(any)

def getHW(map):
    h = len(map)
    # print("height,", h)
    w = len(map[0])
    # print("width,", w)
    return h, w

def GetThinWalls(m):
    h,w = getHW(m)
    thinWalls = []
    # printMap(h,w,m)
    for y in range(0, h):
        for x in range(0 , w):
            if(m[y][x] == 1):
                if((x != 0) and (y != h-1)) or ((x != w-1) and (y != 0)):
                    if (x == 0) or (x == w-1):
                        if((m[y+1][x] == 0) and (m[y-1][x] == 0)):
                            thinWalls.append([y,x])
                    elif (y == 0) or (y == h-1):
                        if((m[y][x+1] == 0) and (m[y][x-1] == 0)):
                            thinWalls.append([y,x])
                    else:
                        if(((m[y][x+1] == 0) and (m[y][x-1] == 0)) or ((m[y+1][x] == 0) and (m[y-1][x] == 0))):
                            thinWalls.append([y,x])
                        # m[y][x] = "x"
    # print the thin walls location
    # for i in range(len(thinWalls)):
        # m[thinWalls[i][0]][thinWalls[i][1]] = "x"
    # print("\n Walls:")
    # printMap(h,w,m)
    return thinWalls

def permutation(idx):
    pmtt = [
        [0, 1, 2, 3] , [0, 1, 3, 2] , [0, 2, 1, 3] , [0, 2, 3, 1] , [0, 3, 1, 2] , [0, 3, 2, 1] , 
        [1, 0, 2, 3] , [1, 0, 3, 2] , [1, 2, 0, 3] , [1, 2, 3, 0] , [1, 3, 0, 2] , [1, 3, 2, 0] ,
        [2, 0, 1, 3] , [2, 0, 3, 1] , [2, 1, 0, 3] , [2, 1, 3, 0] , [2, 3, 0, 1] , [2, 3, 1, 0] ,
        [3, 0, 1, 2] , [3, 0, 2, 1] , [3, 1, 0, 2] , [3, 1, 2, 0] , [3, 2, 0, 1] , [3, 2, 1, 0]
    ]
    # i = permutation.idx
    return pmtt[idx][0], pmtt[idx][1], pmtt[idx][2], pmtt[idx][3]

def nextstep(x,y,m,med,dt,permute):
    dU, dL, dD, dR = permutation(permute)
    DIR = 4
    ATTR = 4
    # print(dU, dL, dD, dR)
    # print(x,y)
    cmds = [ [ 0 for i in range(ATTR) ] for j in range(DIR) ]
    if(y < len(m)-1):
        if(m[y+1][x] == 0):
            cmds[dD][0] = 'D'
            cmds[dD][1] = med[y+1][x]
            cmds[dD][2] = x
            cmds[dD][3] = y+1
    if(y > 0):
        if(m[y-1][x] == 0):
            cmds[dU][0] = 'U'
            cmds[dU][1] = med[y-1][x]
            cmds[dU][2] = x
            cmds[dU][3] = y-1
    if(x < len(m[0])-1):
        if(m[y][x+1] == 0):
            cmds[dR][0] = 'R'
            cmds[dR][1] = med[y][x+1]
            cmds[dR][2] = x+1
            cmds[dR][3] = y
    if(x > 0):
        if(m[y][x-1] == 0):
            cmds[dL][0] = 'L'
            cmds[dL][1] = med[y][x-1]
            cmds[dL][2] = x-1
            cmds[dL][3] = y
    
    # print(cmds)
    selectedi = 0
    weight = 100000000 # cmds[0][1]
    for i in range(0, DIR):
        # print(cmds[i][0], cmds[i][1])
        if (cmds[i][0] != 0):
            # print("checking:", cmds[i][0])
            if (weight > cmds[i][1]):
                weight = cmds[i][1]
                selectedi = i
                # print("selected:", i)
    dt += 1
    x = cmds[selectedi][2]
    y = cmds[selectedi][3]
    med[y][x] += 1
    # print("x,y:",x,y)
    return x,y,med,dt

def nextshortest(x,y,med,smed,dt,permute):
    dU, dL, dD, dR = permutation(permute)
    DIR = 4
    ATTR = 4
    print(dU, dL, dD, dR)
    # print(x,y)
    cmds = [ [ 0 for i in range(ATTR) ] for j in range(DIR) ]
    if(y < len(med)-1):
        if(med[y+1][x] > 0):
            cmds[dD][0] = 'D'
            cmds[dD][1] = med[y+1][x]
            cmds[dD][2] = x
            cmds[dD][3] = y+1
    if(y > 0):
        if(med[y-1][x] > 0):
            cmds[dU][0] = 'U'
            cmds[dU][1] = med[y-1][x]
            cmds[dU][2] = x
            cmds[dU][3] = y-1
    if(x < len(med[0])-1):
        if(med[y][x+1] > 0):
            cmds[dR][0] = 'R'
            cmds[dR][1] = med[y][x+1]
            cmds[dR][2] = x+1
            cmds[dR][3] = y
    if(x > 0):
        if(med[y][x-1] > 0):
            cmds[dL][0] = 'L'
            cmds[dL][1] = med[y][x-1]
            cmds[dL][2] = x-1
            cmds[dL][3] = y
    
    # print(cmds)
    selectedi = 0
    weight = 100000000 # cmds[0][1]
    for i in range(0, DIR):
        # print(cmds[i][0], cmds[i][1])
        if (cmds[i][0] != 0):
            # print("checking:", cmds[i][0])
            if (weight > cmds[i][1]):
                weight = cmds[i][1]
                selectedi = i
                # print("selected:", i)
    dt += 1
    x = cmds[selectedi][2]
    y = cmds[selectedi][3]
    smed[y][x] += 1
    # print("x,y:",x,y)
    return x,y,med,dt


def printRtMap(h, w, m, med):
    # height, width = getHW(map)
    for y in range(h):
        for x in range(w):
            if (m[y][x] > 0):
                val = 'x'
            else:
                val = med[y][x]
            print(val,' ', end='')
        print('')

def printMap(h, w, m):
    # height, width = getHW(map)
    for y in range(h):
        for x in range(w):
            print(m[y][x],' ', end='')
        print('')

def PathSearch(map, setPermutation):
    # Your code here
    MAX_PERMUTATION = 24
    height, width = getHW(map)
    if(setPermutation > 0) and (setPermutation < MAX_PERMUTATION):
        PermuteCount = setPermutation
        MAX_PERMUTATION_TARGET = setPermutation+1
    else:
        PermuteCount = 0
        MAX_PERMUTATION_TARGET = MAX_PERMUTATION

    # distanceHistory = [ 0 for i in range(MAX_PERMUTATION) ]
    distanceHistory = [ [ 0 for i in range(2) ] for j in range(MAX_PERMUTATION) ]
    while (PermuteCount < MAX_PERMUTATION_TARGET):
        mapped = [ [ 0 for i in range(width) ] for j in range(height) ]
        shortestmap = [ [ 0 for i in range(width) ] for j in range(height) ]
        x = width-1
        y = height-1
        dt = 1
        mapped[x][y] = 1
        while (x>0) or (y>0):
            x,y,mapped,dt = nextstep(x,y,map,mapped,dt,PermuteCount)
            # print(x,y,dt)
        printRtMap(height, width, map, mapped)
        donRepeatAgain = 1
        if (donRepeatAgain == 1):
            y2 = height-1
            x2 = width-1
            dt2 = 1
            while (x2>0) or (y2>0):
                x2,y2,mapped,dt2 = nextshortest(x2,y2,mapped,shortestmap,dt2,1)
                
                print(x2,y2,dt2)
                printRtMap(height, width, map, shortestmap)
                # input("Press Enter to continue...")
                # time.sleep(0.2)
        # print(PermuteCount,dt)
            distanceHistory[PermuteCount][0] = dt2
            distanceHistory[PermuteCount][1] = PermuteCount
        else:
            distanceHistory[PermuteCount][0] = dt
            distanceHistory[PermuteCount][1] = PermuteCount
        PermuteCount += 1
        # input("Press Enter to continue...")
        # print("original map:")
        # printMap(height, width, map)
        # print("walkthrough map:")
        # printMap(height, width, mapped)
    return distanceHistory
    
def GetShortestDistance(dHistory):
    # Get least distance direction sets:
    shortestDistance = dHistory[0][0]
    shortestPermutation = 0 
    for i in range(len(dHistory)):
        if(shortestDistance > dHistory[i][0]):
            shortestDistance = dHistory[i][0]
            shortestPermutation = i
    return dHistory[shortestPermutation]
    # return shortestPermutation, shortestDistance

def solution(map):
    thinWalls = GetThinWalls(map)
    DistanceCandidates = []
    h,w = getHW(map)
    # printMap(h,w,map)
    xmap = [ [ 0 for i in range(w) ] for j in range(h) ]
    for i in range(len(thinWalls)+1):
        for y in range(h):
            for x in range(w):
                xmap[y][x] = map[y][x]
        
        if 0: #print
            print("\nRemoved all thin walls:")
            for i in range(len(thinWalls)):
                xmap[thinWalls[i][0]][thinWalls[i][1]] = "x"
            printMap(h,w,xmap)

        else: # test run
            if(i < len(thinWalls)):
                xmap[thinWalls[i][0]][thinWalls[i][1]] = 0
                print("Shortest Path for wall removed at:", thinWalls[i], i)
            else:
                print("Shortest path for last try with not removing any wall")
            
            # printMap(h,w,xmap)
            PathDistances = PathSearch(xmap, 24)
            thisWallShortest = GetShortestDistance(PathDistances)
            DistanceCandidates.append(thisWallShortest)
            # input("Press Enter to continue...")
        
        # print(PathDistances[ShortestIdx], ShortestIdx)

    FinalShortest = GetShortestDistance(DistanceCandidates)
    print("Final:")
    print(FinalShortest[0], FinalShortest[1], thinWalls[FinalShortest[1]])

# TODO: junctions vector mapping
# TODO: vector trees search
def xsolution(map):
    map[18][19] = 0
    print(GetShortestDistance(PathSearch(map, 3)))

# solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) 
# solution([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0v]]) 
# solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
if 1:
    xsolution([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1], 
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

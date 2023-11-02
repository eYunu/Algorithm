import time

PLVL_SOL = 5
PLVL_ERR = 6
PLVL_WAR = 7
PLVL_LOG = 8
PLVL_INF = 9
PLVL_MAP = 10
PLVL_MRT = 11
PLVL_USR = 12
PLVL_DBG = 13
PRINT_LVL = PLVL_USR
# ENABLE_PRINT = False
ENABLE_PRINT = True

def xprint(*argv, **kwargs):
    if(ENABLE_PRINT):
        print(*argv, **kwargs)

def dprint(lvl, *argv, **kwargs):
    if (lvl <= PRINT_LVL) and (lvl > 0):
        for arg in argv:
            xprint(arg, end='')
        if(kwargs):
            for key, arg in kwargs.items():
                if(key == 'end') and (arg == ''):
                    xprint("", end='')
        else:
            xprint("")

class point:
    IS_WALL = 1
    IS_PATH = 1 - IS_WALL
    IS_MARK = 'x'
    IS_JUNCTION = 2
    IS_STARTEND = 3
    IS_DEADEND = 4
    IS_NULL = 5

    def __init__ (self,x,y,typ):
        self.x = x
        self.y = y
        self.type = typ

class dir:
    UP      = 0
    DOWN    = 1
    LEFT    = 2
    RIGHT   = 3
    MAX     = 4

class cmap:
    def __init__(self, matrix):
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.x = self.w
        self.y = self.h
        self.matrix = matrix
        self.mtracker = [ [ 0 for i in range(self.w) ] for j in range(self.h) ]
    
    def val(self, x,y):
        return self.matrix[y][x]
    
    def look(self, direction, x, y):
        if(direction == dir.UP) and (y > 0):
            return self.matrix[y-1][x]
        elif(direction == dir.DOWN) and (y < self.h-1):
            return self.matrix[y+1][x]
        elif(direction == dir.LEFT) and (x > 0):
            return self.matrix[y][x-1]
        elif(direction == dir.RIGHT) and (x < self.w-1):
            return self.matrix[y][x+1]        

    def printMap(self):
        for y in range(self.h):
            for x in range(self.w):
                dprint(PLVL_MAP, self.matrix[y][x],' ', end='')
            dprint(PLVL_MAP, '')

    def markRtMap(self, x, y):
        self.mtracker[y][x] = point.IS_MARK
    def marknprtRtMap(self, x, y):
        self.mtracker[y][x] = point.IS_MARK
        self.printRtMap()
    
    def clrTrackerMap(self):
        for y in range(self.h):
            for x in range(self.w):
                self.mtracker[y][x] = 0

    def printRtMap(self):
        for y in range(self.h):
            for x in range(self.w):
                if (self.matrix[y][x] > 0):
                    val = point.IS_WALL
                else:
                    val = self.mtracker[y][x]
                dprint(PLVL_MRT, val,' ', end='')
            dprint(PLVL_MRT, '')
        dprint(PLVL_MRT, '====== map end ======')

class junction:
    def __init__(self, map_obj):
        self.mo = map_obj
        self.p = point(0,0,point.IS_NULL)
        self.x = self.y = self.jcnt = 0
        self.isPath = [False, False, False, False]
        self.toDis =  0 #[0, 0, 0, 0]
        self.EndCord = [0,0]
        self.isJunct = False

    def GetJunction(self, x, y):
        self.p = point(x,y, point.IS_NULL)
        self.x = x
        self.y = y
        self.isJunct, self.jcnt, self.isPath = self.GetJunctionCnts(x,y)
        if(self.isJunct == True):
            self.toDis, self.EndCord = self.get_distance(x, y)
        return self
    
    def get_distance(self, startx, starty):
        isJt = False
        # JtCnt=0
        # hasPath = []
        distance = 0
        endx = startx
        endy = starty
        for tryUntill in range(500): #try up to 500 corners
            for d in range(dir.MAX):
                if(self.mo.look(d, startx, starty) == point.IS_PATH):
                    dist, endx, endy = self.move(d, startx, starty)
                    # if((endx == startx) and (endy == starty)):
                    #     return distance, [endx, endy]
                    
                    distance += dist
                    isJt = self.isJunction(endx,endy)
                    if(isJt == True):
                        return distance, [endx, endy]
                    else:
                        startx = endx
                        starty = endy
                        distance =- 1 #minus starting end point overlapping
    
    def move(self, d, startx, starty):
        dist = 0
        endx = startx
        endy = starty
        if(d == dir.UP):
            for y in range(starty, -1, -1):
                dist += 1
                if(self.mo.look(d, startx, y) == point.IS_WALL) or ((self.isJunction(startx,y)) and (starty != y)):
                    endy = y
                    break
        elif(d == dir.DOWN):
            for y in range(starty, self.mo.h, 1):
                dist += 1
                if(self.mo.look(d, startx, y) == point.IS_WALL) or ((self.isJunction(startx,y)) and (starty != y)):
                    endy = y
                    break
        elif(d == dir.LEFT):
            for x in range(startx, -1, -1):
                dist += 1
                if(self.mo.look(d, x, starty) == point.IS_WALL) or ((self.isJunction(x,starty)) and (startx != x)):
                    endx = x
                    break

        elif(d == dir.RIGHT):
            for x in range(startx, self.mo.w, 1):
                dist += 1
                if(self.mo.look(d, x, starty) == point.IS_WALL) or ((self.isJunction(x,starty)) and (startx != x)):
                    endx = x
                    break
        return dist-1, endx, endy
    
    def isJunction(self, x,y):
        a,b,c = self.GetJunctionCnts(x,y)
        return a
    
    def GetJunctionCnts(self, x,y):
        jtcnt = 0
        thisPointIsJunction = False
        hasPath = [False, False, False, False]
        for d in range(dir.MAX):
            if(self.mo.look(d,x,y) == point.IS_PATH):
                hasPath[d] = True
                jtcnt += 1
                if(jtcnt >= 3):
                    thisPointIsJunction = True
        if((x == self.mo.w-1 and y == self.mo.h-1) or (x==0 and y==0)):
            thisPointIsJunction = True

        return thisPointIsJunction, jtcnt, hasPath

class node:
    def __init__(self, matrix):
        self.mo = cmap(matrix)
        self.junctions = []
        self.nodes = [[junction(self.mo) for x in range(self.mo.w)] for y in range(self.mo.h)]

    def populate(self):
        for y in range(self.mo.h-1, -1, -1):
            for x in range(self.mo.w-1, -1, -1):
                if(self.mo.val(x,y) == point.IS_PATH):
                    thisJunct = self.nodes[y][x].GetJunction(x,y) # self.jo.isJunction(x,y)
                    if(thisJunct.isJunct):
                        self.junctions.append(thisJunct)
                        dprint(PLVL_INF, "Is Junction at: x:", x,', y:',y)
                        # self.mo.printRtMap()
                        self.mo.marknprtRtMap(thisJunct.x,thisJunct.y)
        return self.junctions

    def get_junctions(self):
        return self.junctions
    
    def printJunctions(self):
        for j in self.junctions:
            dprint(PLVL_INF, j.x, ", ", j.y)

class vector:
    def __init__(self, po):
        self.p = self.nextp = po
        self.dis = 0
    
    def linknode(self, nextpo,distance):
        self.nextp = nextpo
        self.dis = distance

class path:
    def __init__(self, mapobj, jts):
        self.vectors = []
        self.mo = mapobj
        self.junctions = jts

    def mapping(self):
        save_route = []
        # for y in range(0, self.mo.h):
        #     for x in range(0 , self.mo.w):
        for jt in range(len(self.junctions)):
            v = vector(jt.x, jt.y)
            for d in range(dir.MAX):
                if(jt.isPath[d]):
                    endx = jt.EndCord[d][0]
                    endy = jt.EndCord[d][1]
                    
        return save_route
    
    def getJunctionIndex(self, x, y):
        for i in range(len(self.junctions)):
            if(x == self.junctions[i].EndCord[0]) and (y == self.junctions[i].EndCord[1]):
                return i



def GetThinWalls(m):
    mo = cmap(m)
    h = mo.h
    w = mo.w
    thinWalls = []
    # printMap(h,w,m)
    for y in range(0, h):
        for x in range(0 , w):
            if(m[y][x] == 1):
                if((x != 0) or (y != h-1)) and ((x != w-1) or (y != 0)) and ((x != 0) or (y != 0)) and ((x != w-1) or (y != h-1)):
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



def solution(map):
    # Your code here
    m = cmap(map)
    dprint(PLVL_USR, "Test Map:")
    m.printMap()
    n = node(map)
    # v.mo.printRtMap()
    dprint(PLVL_USR, "Test Result:")
    n.populate()
    n.mo.printMap()
    n.printJunctions()
    # dprint(PLVL_USR,"vectors:", v.vecs)
    # dprint(PLVL_USR,"Final:")

# TODO: junctions vector mapping
# TODO: vector trees search

# solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) 
# solution([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0v]]) 
# solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

if 1:
    solution([
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    ])

if 0:
    solution([
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    ])

if 0:
    solution([
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

import time

PLVL_ERR = 6
PLVL_WAR = 7
PLVL_LOG = 8
PLVL_INF = 9
PLVL_MAP = 10
PLVL_MRT = 11
PLVL_USR = 12
PLVL_DBG = 13
PRINT_LVL = PLVL_USR

def xprint(*argv, **kwargs):
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

class junction:
    def __init__(self, map_obj):
        self.mo = map_obj
        self.x = self.y = self.jcnt = 0
        self.isPath = [False, False, False, False]
        self.toDis = [0, 0, 0, 0]
        self.isJunct = False

    def isJunction(self, x, y):
        self.isPath = [False, False, False, False]
        self.toDis = [0, 0, 0, 0]
        self.EndCord = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.isJunct = False
        self.jcnt = 0
        self.x = x
        self.y = y
        for d in range(dir.MAX):
            if(self.mo.look(d,x,y) == point.IS_PATH):
                self.isPath[d] = True
                self.jcnt += 1

        # if(self.jcnt > 1):
        if(self.jcnt >= 3):
            for d in range(dir.MAX):
                self.toDis[d], self.EndCord[d] = self.get_distance(d, x, y)
            self.isJunct = True 
        return self
    
    def get_distance(self, d, startx, starty):
        distance = 0
        endx = startx
        endy = starty
        if(d == dir.UP):
            for y in range(starty, -1, -1):
                if(self.mo.look(d, startx, y) == point.IS_PATH):
                    distance += 1
                else:
                    endy = y
                    break
        elif(d == dir.DOWN):
            for y in range(starty, self.mo.h):
                if(self.mo.look(d, startx, y) == point.IS_PATH):
                    distance += 1
                else:
                    endy = y
                    break
        elif(d == dir.LEFT):
            for x in range(startx, -1, -1):
                if(self.mo.look(d, x, starty) == point.IS_PATH):
                    distance += 1
                else:
                    endx = x
                    break
        elif(d == dir.RIGHT):
            for x in range(startx, self.mo.w):
                if(self.mo.look(d, x, starty) == point.IS_PATH):
                    distance += 1
                else:
                    endx = x
                    break
        return distance, [endx, endy]
    
class vector:
    
    def __init__(self, matrix):
        self.mo = cmap(matrix)
        self.vecs = []
        # self.jo = junction(self.mo)
        self.nodes = [[junction(self.mo) for x in range(self.mo.w)] for y in range(self.mo.h)]
        self.populate()

    def populate(self):
        for y in range(0, self.mo.h):
            for x in range(0 , self.mo.w):
                if(self.mo.val(x,y) == point.IS_PATH):
                    thisJunct = self.nodes[y][x].isJunction(x,y) # self.jo.isJunction(x,y)
                    # self.mo.printRtMap()
                    if(thisJunct.isJunct):
                        self.vecs.append(thisJunct)
                        # dprint(PLVL_INF, "Is Junction at: x:", x,', y:',y)
                        # self.mo.marknprtRtMap(thisJunct.x,thisJunct.y)
        return self.vecs
    
    def route(self):
        save_route = []
        for y in range(0, self.mo.h):
            for x in range(0 , self.mo.w):
                if(self.nodes[y][x].isJunct == True):
                    save_route.append(self.nodes[y][x])
                    for d in range(dir.MAX):
                        if(self.nodes[y][x].isPath[d]):
                            endx = self.nodes[y][x].EndCord[d][0]
                            endy = self.nodes[y][x].EndCord[d][1]
                            if(self.nodes[endy][endx].isJunct == True):
                                x = endx
                                y = endy
        return save_route
    
    def printNodes(self):
        for j in self.vecs:
            dprint(PLVL_INF, j.x, ", ", j.y)

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
    v = vector(map)
    # v.mo.printRtMap()
    dprint(PLVL_USR, "Test Result:")
    v.mo.printMap()
    v.printNodes()
    # dprint(PLVL_USR,"vectors:", v.vecs)
    # dprint(PLVL_USR,"Final:")

# TODO: junctions vector mapping
# TODO: vector trees search

# solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) 
# solution([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0v]]) 
# solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

if 0:
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

if 1:
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

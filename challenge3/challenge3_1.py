import time

PRINT_LVL = 1

def dprint(any, lvl):
    if (lvl <= PRINT_LVL) and (lvl > 0):
        print(any)


def loopthrough(height, width, map):
    for y in range(height-1, -1, -1):
        for x in range(width-1, -1, -1):
            wall = map[y][x]
            print(y,x,wall)
    return wall

def getHW(map):
    h = len(map) 
    print("height,", h)
    w = len(map[0]) 
    print("width,", w)
    return h, w

def moveL(y, xoffset, m):
    for x in range(len(m[0])-1, xoffset-1, -1):
        print("y:", y, ", x:", x)
        if (m[y][x] == 0):
            dis += 1
        else:
            return x, dis

def move(cmd, xoffset, yoffset, m):
    print(cmd, xoffset, yoffset)
    match cmd:
        case "U":
            start   = yoffset
            end     = -1 
            step    = -1
        case "D":
            start   = yoffset 
            end     = len(m)-1
            step    = 1
        case "L":
            start   = xoffset 
            end     = -1
            step    = -1
        case "R":
            start   = xoffset
            end     = len(m[0])
            step    = 1
    
    dis = 0
    Wall = 'N'
    # print(start, end)
    for move in range(start, end, step):
        if(cmd == "U") or (cmd == "D"):
            ymove = move
            xmove = xoffset
        else:
            xmove = move
            ymove = yoffset
        
        if (m[ymove][xmove] == 0):
            print("xmov:", xmove, "ymov:", ymove)
            dis += 1
        else:
            Wall = 'Y'
            if(cmd == "U") or (cmd == "D"):
                ymove += 1
            else:
                xmove += 1
            break

    input("Press Enter to continue...")
    return xmove, ymove, dis, Wall

def isWall(x,y,m):
    return m[y][x]

def step(cmd, x, y, m, d, med):
    w = 0
    
    match cmd:
        case 'D':
            if(y < len(m)-1):
                if(m[y+1][x] == 0):
                    y += 1
                else:
                    w = 1
            else:
                w = 1
        case 'U':
            if(y > 0):
                if(m[y-1][x] == 0):
                    y -= 1
                else:
                    w = 1
            else:
                w = 1
        case 'R':
            if(x < len(m[0])-1):
                if(m[y][x+1] == 0):
                    x += 1
                else:
                    w = 1
            else:
                w = 1
        case 'L':
            if(x > 0):
                if(m[y][x-1] == 0):
                    x -= 1
                else:
                    w = 1
            else:
                w = 1
    if(w == 0):
        med[y][x] += 1
    d = d + (1 - w)
    print(x,y,w,d,cmd)
    return x,y,w,d,med

def cyclecmd():
    AllCmd = [['U', 'L'], ['U', 'R'], ['D', 'L'], ['D', 'R']]
    cmd = AllCmd[cyclecmd.j][cyclecmd.i]
    print(cyclecmd.i,cyclecmd.j,cmd)
    if(cyclecmd.i < len(AllCmd[0])-1):
        cyclecmd.i += 1
    else:
        cyclecmd.i = 0
        if(cyclecmd.j < len(AllCmd)-1):
            cyclecmd.j += 1
        else:
            cyclecmd.j = 0
    return cmd
cyclecmd.i=0
cyclecmd.j=0

def nextcmd(x,y,m,med):
    dU=0
    dL=1
    dD=2
    dR=3
    DIR = 4
    ATTR = 2
    cmdD = cmdU = cmdR = cmdL = ''
    cmds = [ [ 0 for i in range(ATTR) ] for j in range(DIR) ]

    # cmds = [['']*ATTR]*DIR
    if(y < len(m)-1):
        if(m[y+1][x] == 0):
            cmds[dD][0] = 'D'
            cmds[dD][1] = med[y+1][x]
            # print(cmds)
    if(y > 0):
        if(m[y-1][x] == 0):
            cmds[dU][0] = 'U'
            cmds[dU][1] = med[y-1][x]
            # print(cmds)
    if(x < len(m[0])-1):
        if(m[y][x+1] == 0):
            cmds[dR][0] = 'R'
            cmds[dR][1] = med[y][x+1]
            # print(cmds)
    if(x > 0):
        if(m[y][x-1] == 0):
            cmds[dL][0] = 'L'
            cmds[dL][1] = med[y][x-1]
            # print(cmds)
    
    selectedi = dL
    weight = 1000000 #enough big val to ensure 1st assignment
    for i in range(0, DIR):
        # print(i)
        if (cmds[i][0] != 0):
            # print("checking:", cmds[i][0])
            if (weight > cmds[i][1]):
                weight = cmds[i][1]
                selectedi = i
                # print("selected:", i)
    
    return cmds[selectedi][0]

def printMap(m):
    height, width = getHW(map)
    for y in range(height):
        print(m[y][:])

def solution(map):
    # Your code here
    height, width = getHW(map)
    mapped = [ [ 0 for i in range(width) ] for j in range(height) ]

    # cmdIdx = 0
    # AllCmd = ['L', 'R', 'U', 'D']
    # AllCmd = [['U', 'L'], ['U', 'R'], ['D', 'L'], ['D', 'R']]
    
    x = width-1
    y = height-1
    cI = cJ = 0
    cmd = cyclecmd()
    pcmd = cmd
    dt = 0

    # x,y,w,dt=step(cmd, width-1, height-1, map, dt)
    while (x>0) or (y>0):
        # if(w):
            # pcmd = cmd
            # cmd = cyclecmd()
        cmd = nextcmd(x,y,map,mapped)
        x,y,w,dt,mapped=step(cmd, x, y, map, dt, mapped)
        
        # input("Press Enter to continue...")
        time.sleep(0.05)
    printMap(mapped)
            


def solution0(map):
    # Your code here
    height, width = getHW(map)

    # cmdIdx = 0
    # AllCmd = ['L', 'R', 'U', 'D']
    AllCmd = [['U', 'L'], ['U', 'R'], ['D', 'L'], ['D', 'R']]
    
    x = width
    y = height
    cIdx = 0
    cmd = AllCmd[cIdx]
    pcmd = cmd
    x,y,dtotal,w=move(cmd, width-1, height-1, map)

    while (x>0) or (y>0):
        if 0: #(w == 'Y'):
            if (cmd == 'L'):
                if (pcmd == 'U'):
                    pcmd = cmd
                    cmd = 'D'
                else:
                    pcmd = cmd
                    cmd = 'U'
            elif (cmd == 'R'):
                if (pcmd == 'U'):
                    pcmd = cmd
                    cmd = 'D'
                else:
                    pcmd = cmd
                    cmd = 'U'
            elif (cmd == 'U'):
                if (pcmd == 'L'):
                    pcmd = cmd
                    cmd = 'R'
                else:
                    pcmd = cmd
                    cmd = 'L'
            elif (cmd == 'D'):
                if (pcmd == 'L'):
                    pcmd = cmd
                    cmd = 'R'
                else:
                    pcmd = cmd
                    cmd = 'L'


        if(cIdx < len(AllCmd)):
            cIdx += 1
        else:
            cIdx = 0
        cmd = AllCmd[cIdx]
        x,y,d,w=move(cmd, x, y, map)
        dtotal += d

        


    print("total: ", dtotal)


# solution([[10,11,12],[20,21,22],[30,31,32]])
# solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) 
# solution([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0v]]) 
# solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
solution([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], 
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

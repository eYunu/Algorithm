
PRINT_LVL = 1

def dprint(any, lvl):
    if (lvl <= PRINT_LVL) and (lvl > 0):
        print(any)


def solution(s):
    # Your code here
    if( isinstance(s, str) == False ):
        dprint("Error, Not String", 1)
        return 0
    
    dprint("Inputs: " + s, 1)
    sLen = len(s)
    if (sLen <= 0) or (sLen >= 200):
        dprint("Error, Empty String or More than 200 char: " + str(sLen), 1)
        return 0
    if (s.isalpha() == False):
        dprint("Error, contain non-alphabets", 1)
        return 0
    if (s.islower() == False):
        dprint("Error, alphabets has uppercase", 1)
        return 0
    
    dprint(sLen, 3)
    isNotFount = True
    for i in range(1, sLen):
        subStr = s[:i]
        ssLen = len(subStr)
        remainder = (sLen)%(ssLen)
        if(remainder) == 0:
            matchCnt = 0
            totalDiv = int((sLen)/(ssLen))
            splitStr = s.split(subStr)
            dprint("idx: " + str(i) +", No Remainder, " + str(splitStr), 3)
            for eachGrp in splitStr:
                if (len(eachGrp) == 0):
                    matchCnt += 1
            dprint("Matching: " + str(matchCnt) +"," + str(totalDiv), 3)
            if (matchCnt == len(splitStr)) and (matchCnt == totalDiv+1):
                dprint("FOUND! "+ str(totalDiv), 1)
                isNotFount = False
                return totalDiv
    
    if(isNotFount):
        return 1


print("Ans: " + str( solution("abccbaabccba") ))
print("Ans: " + str( solution("abccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccbaabccba") ))
print("Ans: " + str( solution("abcabcabcabc") ))
print("Ans: " + str( solution("abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") ))
print("Ans: " + str( solution("abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") ))
print("Ans: " + str( solution("abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcaabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") ))
print("Ans: " + str( solution("abcdefabcdef") ))
print("Ans: " + str( solution("sdasdasdassdasdasdassdasdasdassdasdasdassdasdasads") ))
print("Ans: " + str( solution("abcabcabcabc") ))
print("Ans: " + str( solution("abcabcabcabcAbc") ))
print("Ans: " + str( solution("abcabcab12ca3453bc") ))
print("Ans: " + str( solution("abcaAcabc%abc") ))
print("Ans: " + str( solution(1) ))


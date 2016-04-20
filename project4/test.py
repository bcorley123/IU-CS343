SPACE_CHAR = '_'
SPACE_PENALTY = -1

def s(x, y):
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    elif x==y:
        return 2
    else:
        return -2

def segAlign(s1, s2, enableGraphics=True):
    gapPenalty = -1
    size1 = len(s1)
    size2 = len(s2)
    ### GENERATE INIT BOARD ###
    dotMatrix = [[0 for c in range(size1 + 1)] for r in range(size2 + 1)]
    for x in range(size2 + 1):
        dotMatrix[x][0] = x * gapPenalty
    for y in range(size1 + 1):
        dotMatrix[0][y] = y * gapPenalty
    for r in dotMatrix:
        print r
    ##FILL IN AND UPDATE BOARD
    for i in range(1, size1+1):
        for j in range(1, size2+1):
            diag = dotMatrix[i-1][j-1] + s(s1[i-1], s2[j-1])
            top = dotMatrix[i][j-1] + gapPenalty
            left = dotMatrix[i-1][j] + gapPenalty
            dotMatrix[i][j] = max(diag, top, left)

    for r in dotMatrix:
        print r

    ##BACK, BACK, BACK IT UP (backtrace)
    newS1, newS2 = "",""
    i, j = size1+1, size2+1
    while i > 0 or j > 0:
        curr = dotMatrix[i][j]
        diag = dotMatrix[i-1][j-1] + s(s1[i-1], s2[j-1])
        top = dotMatrix[i][j-1] + gapPenalty
        left = dotMatrix[i-1][j] + gapPenalty
        
        if i > 0 and curr == diag:
            newS1 = s1[i-1] + newS1
            newS2 = s2[j-1] + newS2
            i -= i
            j -= j
            
        elif i > 0 and curr == left:
            newS1 = s1[i-1] + s1
            newS2 = '_' + news2
            i -= 1

        elif j > 0 and curr == top:
            newS1 = "_" + newS1
            newS2 = s2[j-1] + news2
            j -= 1

    return (newS1, newS2)

s1 = "ACACACTA"
s2 = "AGCACACA"

segAlign(s1, s2)



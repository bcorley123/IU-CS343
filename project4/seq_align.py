#! /usr/bin/env python

import sys, time, random
import pygame

e_aplh = "abcdefghijklmnopqrstuvwxyz"
dna_alph = "ACGT"

# generate random string drawn from the given alphabet and of a given length
def gen_random_string(alphabet, length):
    a_len = len(alphabet)
    ret = ""
    for n in range(length):
        ret += alphabet[random.randint(0, a_len-1)]
    return ret

# print gen_random_string(e_aplh, 5)

SPACE_CHAR = '_'
SPACE_PENALTY = -1

# the scoring function
def s(x, y):
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    elif x == y:
        return 2
    else:
        return -2

TILE_SIZE = 40
tile_color = (255, 255, 255)
highlight_color = (120, 129, 250)

def init_board(m, n):
    screen = pygame.display.set_mode(((m+2)*TILE_SIZE, (n+2)*TILE_SIZE))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Dot Board')
    pygame.font.init()
    font = pygame.font.Font(None, 15)
    return screen, font

def create_tile(font, text, color):
    tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
    tile.fill(color)
    b1 = font.render(text, 1, (0, 0, 0))
    tile.blit(b1, (TILE_SIZE/2, TILE_SIZE/2))
    return tile

def render_board(board, font, s1, s2, F):
    for i in range(len(s1)):
        tile = create_tile(font, s1[i], tile_color)
        board.blit(tile, ((i+2)*TILE_SIZE, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (TILE_SIZE, 0))
    for j in range(len(s2)):
        tile = create_tile(font, s2[j], tile_color)
        board.blit(tile, (0, (j+2)*TILE_SIZE))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, TILE_SIZE))
    for (x,y) in sorted(F.keys()):
        tile = create_tile(font, str(F[(x,y)]), tile_color)
        board.blit(tile, ((x+1)*TILE_SIZE, (y+1)*TILE_SIZE))
    
def seq_align(s1, s2, enableGraphics=True):
    gapPenalty = -1
    size1 = len(s1)
    size2 = len(s2)
    #print 'size1: ' + str(size1)
    #print 'size2: ' + str(size2)
    ### GENERATE INIT BOARD ###
    dotMatrix = [[0 for c in range(size2 + 1)] for r in range(size1 + 1)]
    for x in range(0, size1+1):
        dotMatrix[x][0] = x * gapPenalty
    for y in range(size2 + 1):
        dotMatrix[0][y] = y * gapPenalty
    ##FILL IN AND UPDATE BOARD
    for i in range(1, size1+1):
        for j in range(1, size2+1):
            diag = dotMatrix[i-1][j-1] + s(s1[i-1], s2[j-1])
            top = dotMatrix[i][j-1] + gapPenalty
            left = dotMatrix[i-1][j] + gapPenalty
            dotMatrix[i][j] = max(diag, top, left)
    #for r in dotMatrix:
    #    print r

    ##BACK, BACK, BACK IT UP (backtrace)
    newS1, newS2 = "",""
    i, j = size1, size2
    strI, strJ = i-1, j-1
    while (i > 0 or j > 0):
        curr = dotMatrix[i][j]
        diag = dotMatrix[i-1][j-1] + s(s1[strI], s2[strJ])
        top = dotMatrix[i][j-1] + gapPenalty
        left = dotMatrix[i-1][j] + gapPenalty
        #print i
        #print j
        if i > 0 and curr == diag:
            newS1 = s1[strI] + newS1
            newS2 = s2[strJ] + newS2
            i -= 1
            j -= 1
            strI -= 1
            strJ -= 1
        
            
        elif i > 0 and curr == left:
            newS1 = s1[strI] + newS2
            newS2 = '_' + newS2
            i -= 1
            strI -= 1

        elif j > 0 and curr == top:
            newS1 = "_" + newS1
            newS2 = s2[strJ] + newS2
            j -= 1
            strJ -= 1
    #print newS1
    #print newS2
    return (newS1, newS2)

if len(sys.argv) == 2 and sys.argv[1] == 'test':
    f=open('tests.txt', 'r');tests= eval(f.read());f.close()
    cnt = 0; passed = True
    for ((s1, s2), (a1, a2)) in tests:
        (ret_a1, ret_a2) = seq_align(s1, s2, False)
        if (ret_a1 != a1) or (ret_a2 != a2):
            print("test#" + str(cnt) + " failed...")
            passed = False
        cnt += 1
    if passed: print("All tests passed!")
elif len(sys.argv) == 2 and sys.argv[1] == 'gentests':
    tests = []
    for n in range(25):
        m = random.randint(8, 70); n = random.randint(8, 70)
        (s1, s2) = (gen_random_string(dna_alph, m), gen_random_string(dna_alph, n))
        (a1, a2) = seq_align(s1, s2, False)
        tests.append(((s1, s2), (a1, a2)))
    f=open('tests.txt', 'w');f.write(str(tests));f.close()
else:
    l = [('ACACACTA', 'AGCACACA'), ('IMISSMISSISSIPI', 'MYMISSISAHIPPIE'), ('CTGAACAGCCGAGTCTACGTGGGTCTCGGCGACT', 'C_G____GTC__G_CT___T_CAT_T__GCGA_A')]
    enable_graphics = True
    if enable_graphics: pygame.init()
    for (s1, s2) in l:
        print 'sequences:'
        print (s1, s2)
        
        m = len(s1)
        n = len(s2)
        
        print 'alignment: '
        print seq_align(s1, s2, enable_graphics)
    
    if enable_graphics: pygame.quit()

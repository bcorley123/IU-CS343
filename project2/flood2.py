from utilities import *
from sets import Set

def flood(color_of_tile, flooded_list, screen_size):
    numFlooded = len(flooded_list)
    floodSet = Set(flooded_list)
    for i in floodSet:
        floodC = color_of_tile[i]
        lt = left(i)
        rt = right(i)
        upt = up(i)
        dnt = down(i)
        if in_bounds(lt, screen_size) and lt not in floodSet:
            if color_of_tile[lt] == floodC:
                flooded_list.append(lt)
        if in_bounds(rt, screen_size) and rt not in floodSet:
            if color_of_tile[rt] == floodC:
                flooded_list.append(rt)
        if in_bounds(upt, screen_size) and upt not in floodSet:
            if color_of_tile[upt] == floodC:
                flooded_list.append(upt)
        if in_bounds(dnt, screen_size) and dnt not in floodSet:
            if color_of_tile[dnt] == floodC:
                flooded_list.append(dnt)

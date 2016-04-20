from utilities import *

def flood(color_of_tile, flooded_list, screen_size):
    numFlooded = len(flooded_list)
    floodC = color_of_tile[flooded_list[0]]
    for i in flooded_list:
        lt = left(i)
        rigt = right(i)
        up = up(i)
        down = down(i)
        if in_bounds(left, screen_Size) and left not in flooded_list:
            if color_of_tile[left] == floodC:
                flooded_list.append(left)
        if in_bounds(right, screen_Size) and right not in flooded_list:
            if color_of_tile[right] == floodC:
                flooded_list.append(right)
        if in_bounds(up, screen_Size) and up not in flooded_list:
            if color_of_tile[up] == floodC:
                flooded_list.append(up)
        if in_bounds(down, screen_Size) and down not in flooded_list:
            if color_of_tile[down] == floodC:
                flooded_list.append(down)

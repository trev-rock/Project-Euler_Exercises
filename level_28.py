from math import sqrt
from numpy import diag, fliplr

def find_center(lxh):
    return int(lxh/2), int(lxh/2) # this gets us the center because on the graph itself we start counting at 0, so if we had a 5x5, then row 2 is the center row and col 2 is the center col


def create_blank_grid(lxh):
    max_ranges = lxh
    blank = []
    for i in range(1,max_ranges+1):
        temp = []
        for j in range(1,max_ranges+1):
            temp.append("x")
        blank.append(temp)
    return blank


def move_right(x,y):
    return x+1, y


def move_left(x,y):
    return x-1, y


def move_up(x,y): # moving up is decreasing the y value 
    return x, y-1


def move_down(x, y): # moving down is increasing the y value
    return x, y+1


def fill_grid(grid, max_num, x, y):
    # the starting values for moving up/down/left/right
    times_to_go_left = 2
    times_to_go_right = 1
    times_to_go_up = 2
    times_to_go_down = 1
    num = 1 # start at 1 
    grid[y][x] = num # 1 is always at the center 
    num += 1 # add one to the number after every time it is assigned
    move = "right" # first move is to the right
    while True: # all logic is the same between them so understand how to move right
        if move == "right": # if we need to move right
            for r in range(1,times_to_go_right+1): # how many spaces we need to fill to that direction
                x, y = move_right(x, y) # move in the direction
                grid[y][x] = num # update space in grid
                if num == max_num: # needed to add a check for num == max_num when moving to the right because that's where it will end
                    return grid
                num += 1 # iterate to our next number
            times_to_go_right += 2 # it always goes up by 2
            move = "down" # we always move down after moving right

        if move == "down": 
            for d in range(1,times_to_go_down+1): 
                x, y = move_down(x, y) 
                grid[y][x] = num 
                num += 1 
            times_to_go_down += 2 
            move = "left" 

        if move == "left": 
            for l in range(1,times_to_go_left+1): 
                x, y = move_left(x, y) 
                grid[y][x] = num 
                num += 1 
            times_to_go_left += 2 
            move = "up" 

        if move == "up": 
            for u in range(1,times_to_go_up+1): 
                x, y = move_up(x, y) 
                grid[y][x] = num 
                num += 1 
            times_to_go_up += 2 
            move = "right" 


max_num = 1001*1001 # this will later be whatever the 1001*1001 is 
lxh = int(sqrt(max_num)) # length and height since it is a square
x, y = find_center(lxh) # our starting point before we begin to change everything inside of it
grid = create_blank_grid(lxh) # make the blank grid that we will fill out next
grid = fill_grid(grid, max_num, x, y)
total = sum(diag(grid)) + sum(diag(fliplr(grid))) - 1 # take the sum of the diagonal, flip it and take the sum of that diagonal, subtract 1 so we don't count the center twice

print(total)
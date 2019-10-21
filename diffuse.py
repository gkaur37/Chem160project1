import random

npart = 500
side = 51  #Should be an odd number 21, 31, 41, 51
steps = [(1,0),(-1,0),(0,1),(0,-1)]
maxsteps = 10000
perc = 0
x, y = 0, 0

density = float(input("Please enter a density value between 0.0 - 1.0: "))

grid=[[0 for x in range(side)] for y in range(side)]

#loop over all the cells in the grid and set cell to "1"
while x < len(grid):
    while y < len(grid[x]):
        grid[x][y] = random.choices([0,1],[1.0 - density, density], k=1)[0]
        y += 1
    x += 1
    y = 0

for ipart in range(npart):
    # Start particle at center
    x,y = side//2, side//2
    # perform the random walk until particle departs, convert while loop to for, and loop over max steps
    for isteps in range(maxsteps):
        # Randomly move particle
        sx,sy = random.choice(steps)
        # check if the new cell have a value == 1, if it is then skip to next iteration otherwise increment x & y
        if grid[x+sx][y+sy] == 1:
          continue
        else:
          x += sx
          y += sy
        # If particle reaches the edge of the system increment perc +1 and go to next particle
        if x<=0 or y<=0 or x==side-1 or y==side-1:
          perc += 1
          break

print("Probility of the particle percolating out of the system is {}".format(perc/npart))
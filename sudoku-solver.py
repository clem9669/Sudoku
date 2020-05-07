#/usr/bin/env python3
import numpy as np
import argparse,sys

# grid = [[5,3,0,0,7,0,0,0,0],
#         [6,0,0,1,9,5,0,0,0],
#         [0,9,8,0,0,0,0,6,0],
#         [8,0,0,0,6,0,0,0,3],
#         [4,0,0,8,0,3,0,0,1],
#         [7,0,0,0,2,0,0,0,6],
#         [0,6,0,0,0,0,2,8,0],
#         [0,0,0,4,1,9,0,0,5],
#         [0,0,0,0,8,0,0,7,9]]

# oneliner = "400005000000000198300082400000100080903000000000030670050009000000200907640300000" 
# oneliner2= "940020700001004009006000120000003010100000008070500000087000200600900300009080057"

def oneliner2grid(oneliner):
	global grid
	a = [int(oneliner[a:a+1]) for a in range(len(oneliner))]
	grid = []
	for x in range(0, len(a), 9):
	    grid.append(a[x:x+9])
	return grid	

def input2grid(file):
	f = open(file, 'r')
	for r, row in enumerate(f):
	    for c, cell in enumerate(row):
	        if cell == '\n': 
	        	continue
	        try:
	            int(cell)
	            grid[r][c] = int(cell)
	        except Exception as e:
	            grid[r][c] = '0'

# https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
def print_sudoku(grid):
    print("+" + "---+"*9)
    for i, row in enumerate(grid):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

def possible(y,x,n):
	global grid
	# Check if the number n is possible in the column
	for i in range(0,9):
		if grid[y][i] == n:
			return False
	# Check if the number n is possible in the row
	for i in range(0,9):
		if grid[i][x] == n:
			return False
	# Check if the number n is possible in the square
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if grid[y0+i][x0+j] == n:
				return False
	return True

def solve():
	global grid
	for y in range(0,9):
		for x in range(0,9):
			if grid[y][x] == 0:
				for n in range(1,10):
					if possible(y,x,n):
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return
	# Display solution as a matrix			
	# print(np.matrix(grid))
	# Display solution as ascii table
	print_sudoku(grid)

	# Multiple solutions ?
	input("More ?")

def main():
	# Construct the argument parser
	ap = argparse.ArgumentParser()

	# Add the arguments to the parser
	ap.add_argument("-c", "--ligne", required=False,
	   help="Give grid as a string of number row by row")
	ap.add_argument("-i", "--input", required=False,
	   help="Read the grid from a file")
	args = vars(ap.parse_args())

	# One arg only not both
	if args['input'] and args['ligne']:
		print("Don't handle both arguments.")
		exit()
	if args['ligne']:
		oneliner2grid(args['ligne'])
		print_sudoku(grid)
		solve()
	if args['input']:
		input2grid(args['input'])
		print_sudoku(grid)
		solve()

main()
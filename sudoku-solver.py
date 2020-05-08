#/usr/bin/env python3
import numpy as np
import argparse
import pdb

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

def file2grid(file):
	global grid
	grid = list(range(9))
	f = open(file, 'r')
	for r, row in enumerate(f):
	    for c, cell in enumerate(row):
	        if cell == '\n': 
	        	continue
	        try:
	            grid[r][c] = int(cell)
	        except Exception as e:
	            grid[r][c] = '0'
	f.close()

def input2grid():
	global grid
	grid = list(range(9))
	for i in range(9):
	    inp = input("row " + str(i + 1) + ": ")
	    grid[i] = list(map(int, list(inp)))

def print_sudoku(grid):
	# https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
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

def solve(output):
	global grid
	for y in range(0,9):
		for x in range(0,9):
			if grid[y][x] == 0:
				for n in range(1,10):
					if possible(y,x,n):
						grid[y][x] = n
						# pdb.set_trace()
						solve(output)
						grid[y][x] = 0
				return
	if output == "ascii":
		# Display solution as ascii table
		print_sudoku(grid)

	if output == "matrix":
		# Display solution as a matrix			
		print(np.matrix(grid))
	else:
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
	ap.add_argument("-o", "--output", required=False,
	   help="Print a ascii or matrix output")
	args = vars(ap.parse_args())

	if args['output'] != 'matrix' and args['output'] != 'ascii'and args['output']:
		print('Select either matrix or ascii output')
		exit()
	if not args['output'] or args['output'] == 'ascii':
		# One arg only not both
		if args['input'] and args['ligne']:
			print("Don't handle both arguments.")
			exit()
		if args['ligne']:
			oneliner2grid(args['ligne'])
			print_sudoku(grid)
			solve(ascii)
		if args['input']:
			file2grid(args['input'])
			print_sudoku(grid)
			solve(ascii)
		if not args['input'] and not args['ligne']:
			print("Please enter the rows of the sudoku. Use zero (0) for empty fields. No spaces.")
			input2grid()
			print_sudoku(grid)
			solve(ascii)
	if args['output'] == 'matrix':
		# One arg only not both
		if args['input'] and args['ligne']:
			print("Don't handle both arguments.")
			exit()
		if args['ligne']:
			oneliner2grid(args['ligne'])
			print_sudoku(grid)
			solve(output='matrix')
		if args['input']:
			file2grid(args['input'])
			print_sudoku(grid)
			solve(output='matrix')
		if not args['input'] and not args['ligne']:
			print("Please enter the rows of the sudoku. Use zero (0) for empty fields. No spaces.")
			input2grid()
			print_sudoku(grid)
			solve(output='matrix')

try:
	main()
except KeyboardInterrupt:
	print("\n[*] Bye")
	exit()
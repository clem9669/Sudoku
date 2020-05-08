# Sudoku solver

> Another one

<center><img src="https://camo.githubusercontent.com/df4fd7a52eea6261d23f36f4546f44657913007a/687474703a2f2f63646e2e706967656f6e73616e64706c616e65732e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031352f31322f646a2d6b68616c65642d323031352e6a7067" width="50%"></center>

This project is aim to solve sudoku puzzles.  The resolution is done via recursion *- look in the function `solve`*.

The implementation is heavily based on the video of Computerphile starred Professor Thorsten Altenkirch from Nottingham.  

The video is available on Youtube at [https://www.youtube.com/watch?v=G_UYXzGuqvM](https://www.youtube.com/watch?v=G_UYXzGuqvM).

## Todo

1. Check the fonction `-i`: KO
2. Add function direct row input by defaut: OK
3. Add an output option between *ascii* or *matrix*: OK
4. Add a KeyboardInterrupt function: OK
2. Make a graphical interface in python
3. Make a website
4. Add photo or live camera as input type



## Usage

```sh
$ python3 sudoku-solver.py -h
usage: sudoku-solver.py [-h] [-c LIGNE] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -c LIGNE, --ligne LIGNE
                        Give grid as a string of number row by row
  -i INPUT, --input INPUT
                        Read the grid from a file
  -o OUTPUT, --output OUTPUT
                        Print a ascii or matrix output
```

The usage of **numpy** is optionnal.

## Performance

According to [https://github.com/dado3212/Sudoku-Solver](dado3212/Sudoku-Solver) :

> On the hardest Sudoku in the world it takes \~25 seconds to solve. 
> 800000000003600000070090200050007000000045700000100030001000068008500010090000400


```bash
python3 sudoku-solver.py -c 800000000003600000070090200050007000000045700000100030001000068008500010090000400
[ .. SNIP .. ]
python3 sudoku-solver.py -c   1.49s user 0.09s system 105% cpu 1.493 total
```

This implementation takes only 1.49s.


PS: Press link to the article about the hardest puzzle: [http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html](http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html)


### Useful similar project or link 

- [https://github.com/dado3212/Sudoku-Solver/tree/web]()
- [https://github.com/BrandonTang89/SudokuSolver]()
- [https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3]()
- [https://github.com/mineshpatel1/sudoku-solver]()


UGlub3UK

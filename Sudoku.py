#Michelle Zhao
#CS1, Assignment 7

'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''



    def __init__(self):
        '''initializes the 9x9 board with a Sudoku board list and a list of 
        moves made.'''
        self.board = []
        for i in range(0,9):
            self.board.append([])
        self.movelist = []
       
        # TODO

    def load(self, filename):
        '''loads numbers from a filename into a Sudoku board.'''
        f = open(filename, 'r')
        for i in range(0,9):
            line = f.readline()
            for a in range(0,9):
                self.board[i].append(int(line[a]))

        
            
        # TODO

    def save(self, filename):
        '''saves the current Sudoku board to a file names filename.'''
        f = open(filename, 'w')
        for i in range(0,9):
            string_input = ''
            for j in range(0,9):
                string_input += str(self.board[i][j])
            f.write(string_input + '\n')

        
        # TODO

    def show(self):
        '''Pretty-print the current board representation.'''
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print
        
    def isValid(self, row, col, val):
        '''checks if the spot to move to is empty and does not have any of the 
        same number in spots along the row and column and the number is not
        already in the box.'''
        validvalue = True
        if self.board[row-1][col-1]!=0:
            validvalue = False
        #check columns and columns
        for i in range(0,9):
            if self.board[row-1][i] == val:
                validvalue = False
            if self.board[i][col-1] == val:
                validvalue = False
        #check box
        row_index = 0
        col_index = 0
        if row in range(0,4):
            row_index = 0
        elif row in range(4,7):
            row_index = 3
        elif row in range(7,10):
            row_index = 6
           
        
        if col in range(0,4):
            col_index = 0
        elif col in range(4,7):
            col_index = 3  
        elif col in range(7,10):
            col_index = 6  
        
        for i in range(row_index, row_index+3):
            for j in range(col_index, col_index+3):
                if self.board[i][j] == val:
                    validvalue = False
        return validvalue 
    
    def move(self, row, col, val):
        '''checks if the inputs are valid and puts a number into the Sudoku
        board if possible.'''
        if val not in range(1,10):
            raise SudokuMoveError('value input out of range')
        if col not in range(1,10):
            raise SudokuMoveError('col input out of range')   
        if row not in range(1,10):
            raise SudokuMoveError('row input out of range')
        
        if self.isValid(row, col, val) == False:
            raise SudokuMoveError('value not valid')
        self.board[row-1][col-1] = val
        self.movelist.append((row,col,val))
        
        
        
        # TODO


           
    
                
        
    def undo(self):
        '''undoes last move'''
        r,c,val = self.movelist[len(self.movelist)-1]
        self.board[r-1][c-1] = 0
        self.movelist.pop()
        # TODO


    def solve(self):
        '''has the user solve the Sudoku puzzle and raises errors when 
        entries are not possible.'''
        while True:
            try:
                rcv = raw_input('Enter the command: ')
                if len(rcv) == 3:
                    self.move(int(rcv[0]), int(rcv[1]),int(rcv[2]))
                    self.show()
                elif rcv=='q':
                    break
                elif rcv == 'u':
                    self.undo()  
                    self.show()
                elif rcv == 's':
                    self.save(filename)      
                else:
                    raise SudokuCommandError('command not valid')
            except SudokuMoveError, e:
                print e
            
            except SudokuCommandError:
                print 'Try again'
        # TODO

if __name__ == '__main__':
    s = Sudoku()
   
    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e

    s.show()
    s.solve()
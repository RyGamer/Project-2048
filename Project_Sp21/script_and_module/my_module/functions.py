"""All entirely original (self-made) functions used to manage the '2048' game."""

import random

def emptyBoard():
    """Returns an empty game board.
    
    Parameters
    ----------
    None
        
    Returns
    -------
    list
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    
    return [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
def fillEmpty(board=emptyBoard()):
    """Replaces a random empty tile in the game board a '2' or '4' tile.
    
    Parameters
    ----------
    board : list
        The game board to fill (default is an empty board).
        
    Returns
    -------
    board : list
        The updated version of the game board.
    """
    
    # Random value that determines if the new tile equals to '2' or '4'.
    choose = random.randrange(100)
    # Random value to determine the row of the new tile.
    row = random.randrange(len(board))
    # Random value to determine the column of the new tile.
    col = random.randrange(len(board))
    
    # Checks if the board is full
    full = True

    for r in board:
        for c in r:
            if c == 0:
                full = False
                break
                
    if full:
        return board
    
    # Checks every random coordinate of the game board if they are empty
    # and sets the [row, col] tile to that coordinate.
    while board[row][col] != 0:
        row = random.randrange(len(board))
        col = random.randrange(len(board))
        
    # Updates board.
    board[row][col] = 2 if choose > 25 else 4
    
    return board

def checkNeighbor(row, col, board=emptyBoard()):
    """Checks if any neighboring tiles around the tile defined by [row, col] are changeable.
    
    Parameters
    ----------
    row : int
        The row of the examined tile.
    col : int
        The column of the examined tile.
    board : list
        The game board where the tile is present (default is an empty board).
        
    Returns
    -------
    bool
        True if a changeable neighbor is found, False otherwise.
    """
    
    # Check one row down.
    if row + 1 < len(board):
        if(board[row+1][col] == 0) | (board[row+1][col] == board[row][col]):
            return True
        
    # Check one row up.
    if row - 1 > -1:
        if(board[row-1][col] == 0) | (board[row-1][col] == board[row][col]):
            return True
        
    # Check one column right.
    if col + 1 < len(board[row]):
        if(board[row][col+1] == 0) | (board[row][col+1] == board[row][col]):
            return True
        
    # Check one column left.
    if col - 1 > -1:
        if(board[row][col-1] == 0) | (board[row][col-1] == board[row][col]):
            return True
        
    return False

def checkGameOver(board=emptyBoard()):
    """Checks if there are no other possible moves the player could make.
    
    Parameters
    ----------
    board : list
        The game board, to be examined (default is an empty board).
        
    Returns
    -------
    bool
        True if no moves are possible in the game board, False otherwise.
    """
    
    # Iterate through each tile's set of neighbors to see if any moves are open.
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if checkNeighbor(i, j, board):
                return False
            
    return True

def checkWon(board=emptyBoard()):
    """Checks if any of the tiles in the game board equal to '2048'.
    
    Parameters
    ----------
    board : list
        The game board, to be examined (default is an empty board).
        
    Returns
    -------
    bool
        True if a single tile is equal to '2048', False otherwise.
    """
    
    # Iterate through each tile and check if any of their values equal to '2048'.
    for row in board:
        for col in row:
            if col == 2048:
                return True
            
    return False
"""All entirely original (self-made) tests for my game's functions."""

from functions import *

def test_emptyBoard():
    """Tests if the emptyBoard returns the correct empty game board.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    
    # Test board
    fullBoard = [[2, 3, 4, 5],
                 [6, 7, 8, 9],
                 [10, 11, 12, 13],
                 [14, 15, 16, 17]]
    
    fullBoard = emptyBoard()
    
    assert fullBoard == [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

def test_fillEmpty():
    """Tests if the board is filled properly using fillEmpty.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    
    # Test board
    fullBoard = [[2, 3, 4, 5],
                 [6, 7, 8, 9],
                 [10, 11, 12, 13],
                 [14, 15, 16, 17]]
    
    assert not fillEmpty() == emptyBoard()
    assert fillEmpty(fullBoard) == fullBoard
    
def test_checkNeighbor():
    """Tests if the neighbors in a board are checked for availability properly.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    
    # Test board
    closedBoard = [[2, 3, 4, 5],
                   [6, 7, 8, 9],
                   [10, 11, 12, 13],
                   [14, 15, 16, 17]]

    openBoard = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 2, 2]]
    
    assert checkNeighbor(1, 1, emptyBoard())
    assert not checkNeighbor(1, 1, closedBoard)
    assert checkNeighbor(3, 2, openBoard)

def test_checkGameOver():
    """Tests if a game over is detected properly.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """

    # Test boards
    openBoard = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 2, 2]]
    
    closedBoard = [[2, 3, 4, 5],
                   [6, 7, 8, 9],
                   [10, 11, 12, 13],
                   [14, 15, 16, 17]]
    
    assert not checkGameOver(openBoard)
    assert checkGameOver(closedBoard)
    
def test_checkWon():
    """Tests if a game won is detected properly.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    
    # Test board
    winningBoard = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 2048, 0]]
    
    assert checkWon(winningBoard)
    assert not checkWon()
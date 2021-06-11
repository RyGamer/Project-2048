"""Main script for running the actual game and displaying visuals."""

# Reference: https://www.youtube.com/watch?v=jO6qQDNa2UY&t=672s

# I used this video to learn about the different pygame methods
# and how they worked, so I could incorporate them into this
# separately-made game.

import pygame
from my_module.functions import *

# Font setup.
pygame.font.init()
# Window/game board setup.
pygame.display.set_caption('2048')
W, H = 512, 512
TILE_W, TILE_H = 118, 118
WINDOW = pygame.display.set_mode((W, H))
# Clock setup.
FPS = 60
CLOCK = pygame.time.Clock()

# Different Colors in (R, G, B) format.
BORDER = (130, 120, 100)
EMPTY = (160, 150, 140)
TWO = (250, 230, 180)
FOUR = (230, 200, 140)
EIGHT = (255, 140, 120)
SIXTEEN = (255, 0, 0)
THIRTY_TWO = (200, 20, 0)
SIXTY_FOUR = (160, 20, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

def displayRow(row, sep, y):
    """Displays a single row of the game board to screen (four tiles horizontal).
    
    Parameters
    ----------
    row : list
        The row of tiles to display.
    sep : int
        Length between tiles.
    y   : int
        Row number.
        
    Returns
    -------
    None
    """

    # Chooses color of the tile based on its value.
    for i in range(0, 4):
        if(row[i] == 2):
            color = TWO
        elif(row[i] == 4):
            color = FOUR
        elif(row[i] == 8):
            color = EIGHT
        elif(row[i] == 16):
            color = SIXTEEN
        elif(row[i] == 32):
            color = THIRTY_TWO
        elif(row[i] == 64):
            color = SIXTY_FOUR
        elif(row[i] == 0):
            color = EMPTY
        else:
            color = YELLOW

        # Sets the size/font of the tile's text.
        t_size = 64 if(row[i] < 128) else 48 if(row[i] < 1024) else 32
        font = pygame.font.SysFont('comic sans ms', t_size)
        # Sets the color of the tile's text.
        t_color = WHITE if(row[i] > 4) else BLACK
        # Determines if the tile is an 'empty' tile or has a value > 2.
        t_str = '' if(row[i] < 2) else str(row[i])
        # Draws out the actual tile to screen.
        tile = pygame.Rect(sep + (TILE_W + sep)*i, sep + (TILE_H + sep)*y, TILE_W, TILE_H)
        value = font.render(t_str, 0, t_color)
        pygame.draw.rect(WINDOW, color, tile)
        y_multiplier = 2 if(t_size == 64) else 4 if(t_size == 48) else 5
        WINDOW.blit(value, (sep*2 + (TILE_W + sep)*i, sep*y_multiplier + (TILE_H + sep)*y))

def displayBoard(board):
    """Displays the entire game board to screen.
    
    Parameters
    ----------
    board : list
        The list of rows to display as the game board.
        
    Returns
    -------
    None
    """

    # Background color.
    WINDOW.fill(BORDER)

    # Draws out each row.
    for i in range(0, 4):
        displayRow(board[i], 8, i)

    pygame.display.update()
    
def main():
    """Main function that runs the game loop.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Initializes all game variables.
    gameOver = False
    winner = False
    gameBoard = emptyBoard()

    # Randomly fills two tiles to start with.
    for i in range(0, 2):
        gameBoard = fillEmpty(gameBoard)

    # Debugging/testing out different cases.
    # gameBoard = [[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    # gameBoard[0][0] = 1024
    # gameBoard[1][0] = 1024

    # gameBoard[0] = [2, 2, 2, 2]
    
    # gameBoard[0][0] = 2
    # gameBoard[1][0] = 2
    # gameBoard[2][0] = 4
    # gameBoard[3][0] = 4

    # Runs the game loop.
    while not gameOver:
        # Sets the frame rate and launches the game in its default state.
        CLOCK.tick(FPS)
        move = ''
        change = False
        displayBoard(gameBoard)

        # Read the player's button inputs.
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN) & (move == ''):
                if(event.key == pygame.K_UP):
                    move = 'u'
                if(event.key == pygame.K_DOWN):
                    move = 'd'
                if(event.key == pygame.K_LEFT):
                    move = 'l'
                if(event.key == pygame.K_RIGHT):
                    move = 'r'
            if(event.type == pygame.QUIT):
                pygame.quit()
                return

        if(move == 'r'):
            # Initial values of the board before movement.
            oldBoard = emptyBoard()

            for i in range(0, 4):
                for j in range(0, 4):
                    oldBoard[i][j] = gameBoard[i][j]

            # Shifts all tiles to the right.
            for i in range(0, 4):
                newRow = []
                empty = 0

                for col in gameBoard[i]:
                    if col > 0:
                        newRow.append(col)
                        empty += 1

                for n in range(0, 4 - empty):
                    newRow.insert(0, 0)

                for n in range(0, 4):
                    gameBoard[i][n] = newRow[n]

                if(newRow[0] == newRow[1] == newRow[2] == newRow[3]):
                    doubCheck = True
                    checkType = False
                elif(newRow[0] == newRow[1]) & (newRow[2] == newRow[3]):
                    doubCheck = True
                    checkType = True
                else:
                    doubCheck = False

                for n in range(2, -1, -1):
                    if(gameBoard[i][n] == gameBoard[i][n+1]):
                        gameBoard[i][n+1] *= 2
                        gameBoard[i][n] = 0
                    elif(gameBoard[i][n+1] == 0):
                        gameBoard[i][n+1] = gameBoard[i][n]
                        gameBoard[i][n] = 0
                
                if doubCheck:
                    if checkType:
                        for n in range(0, 3):
                            if(gameBoard[i][n] == gameBoard[i][n+1]):
                                gameBoard[i][n+1] *= 2
                                gameBoard[i][n] = 0
                    else:
                        for n in range(2, -1, -1):
                            if(gameBoard[i][n] == gameBoard[i][n+1]):
                                gameBoard[i][n+1] *= 2
                                gameBoard[i][n] = 0
                            elif(gameBoard[i][n+1] == 0):
                                gameBoard[i][n+1] = gameBoard[i][n]
                                gameBoard[i][n] = 0


            # Checks for changes pre- and post-movement
            change = gameBoard != oldBoard
        elif(move == 'l'):
            # Initial values of the board before movement.
            oldBoard = emptyBoard()

            for i in range(0, 4):
                for j in range(0, 4):
                    oldBoard[i][j] = gameBoard[i][j]

            # Shifts all tiles to the left.
            for i in range(0, 4):
                newRow = []
                empty = 0

                for col in gameBoard[i]:
                    if col > 0:
                        newRow.append(col)
                        empty += 1

                for n in range(0, 4 - empty):
                    newRow.append(0)

                for n in range(0, 4):
                    gameBoard[i][n] = newRow[n]

                if(newRow[0] == newRow[1] == newRow[2] == newRow[3]):
                    doubCheck = True
                    checkType = False
                elif(newRow[0] == newRow[1]) & (newRow[2] == newRow[3]):
                    doubCheck = True
                    checkType = True
                else:
                    doubCheck = False

                for n in range(0, 3):
                    if(gameBoard[i][n] == gameBoard[i][n+1]):
                        gameBoard[i][n] *= 2
                        gameBoard[i][n+1] = 0
                    elif(gameBoard[i][n] == 0):
                        gameBoard[i][n] = gameBoard[i][n+1]
                        gameBoard[i][n+1] = 0

                if doubCheck:
                    if checkType:
                        for n in range(3, 0, -1):
                            if(gameBoard[i][n] == gameBoard[i][n-1]):
                                gameBoard[i][n-1] *= 2
                                gameBoard[i][n] = 0
                    else:
                        for n in range(0, 3):
                            if(gameBoard[i][n] == gameBoard[i][n+1]):
                                gameBoard[i][n] *= 2
                                gameBoard[i][n+1] = 0
                            elif(gameBoard[i][n] == 0):
                                gameBoard[i][n] = gameBoard[i][n+1]
                                gameBoard[i][n+1] = 0


            # Checks for changes pre- and post-movement
            change = gameBoard != oldBoard
        elif(move == 'd'):
            # Initial values of the board before movement.
            oldBoard = emptyBoard()

            for i in range(0, 4):
                for j in range(0, 4):
                    oldBoard[i][j] = gameBoard[i][j]

            # Shifts all tiles downward.
            for i in range(0, 4):
                newCol = []
                empty = 0

                for j in range(0, 4):
                    if gameBoard[j][i] > 0:
                        newCol.append(gameBoard[j][i])
                        empty += 1

                for n in range(0, 4 - empty):
                    newCol.insert(0, 0)

                for n in range(0, 4):
                    gameBoard[n][i] = newCol[n]

                if(newCol[0] == newCol[1] == newCol[2] == newCol[3]):
                    doubCheck = True
                    checkType = False
                elif(newCol[0] == newCol[1]) & (newCol[2] == newCol[3]):
                    doubCheck = True
                    checkType = True
                else:
                    doubCheck = False

                for n in range(2, -1, -1):
                    if(gameBoard[n][i] == gameBoard[n+1][i]):
                        gameBoard[n+1][i] *= 2
                        gameBoard[n][i] = 0
                    elif(gameBoard[n+1][i] == 0):
                        gameBoard[n+1][i] = gameBoard[n][i]
                        gameBoard[n][i] = 0

                if doubCheck:
                    if checkType:
                        for n in range(0, 3):
                            if(gameBoard[n][i] == gameBoard[n+1][i]):
                                gameBoard[n+1][i] *= 2
                                gameBoard[n][i] = 0
                    else:
                        for n in range(2, -1, -1):
                            if(gameBoard[n][i] == gameBoard[n+1][i]):
                                gameBoard[n+1][i] *= 2
                                gameBoard[n][i] = 0
                            elif(gameBoard[n+1][i] == 0):
                                gameBoard[n+1][i] = gameBoard[n][i]
                                gameBoard[n][i] = 0
            
            # Checks for changes pre- and post-movement
            change = gameBoard != oldBoard
        elif(move == 'u'):
            # Initial values of the board before movement.
            oldBoard = emptyBoard()

            for i in range(0, 4):
                for j in range(0, 4):
                    oldBoard[i][j] = gameBoard[i][j]

            # Shifts all tiles upward.
            for i in range(0, 4):
                newCol = []
                empty = 0

                for j in range(0, 4):
                    if gameBoard[j][i] > 0:
                        newCol.append(gameBoard[j][i])
                        empty += 1

                for n in range(0, 4 - empty):
                    newCol.append(0)

                for n in range(0, 4):
                    gameBoard[n][i] = newCol[n]


                if(newCol[0] == newCol[1] == newCol[2] == newCol[3]):
                    doubCheck = True
                    checkType = False
                elif(newCol[0] == newCol[1]) & (newCol[2] == newCol[3]):
                    doubCheck = True
                    checkType = True
                else:
                    doubCheck = False

                for n in range(0, 3):
                    if(gameBoard[n][i] == gameBoard[n+1][i]):
                        gameBoard[n][i] *= 2
                        gameBoard[n+1][i] = 0
                    elif(gameBoard[n][i] == 0):
                        gameBoard[n][i] = gameBoard[n+1][i]
                        gameBoard[n+1][i] = 0

                if doubCheck:
                    if checkType:
                        for n in range(3, 0, -1):
                            if(gameBoard[n][i] == gameBoard[n-1][i]):
                                gameBoard[n-1][i] *= 2
                                gameBoard[n][i] = 0
                    else:
                        for n in range(0, 3):
                            if(gameBoard[n][i] == gameBoard[n+1][i]):
                                gameBoard[n][i] *= 2
                                gameBoard[n+1][i] = 0
                            elif(gameBoard[n][i] == 0):
                                gameBoard[n][i] = gameBoard[n+1][i]
                                gameBoard[n+1][i] = 0

            # Checks for changes pre- and post-movement
            change = gameBoard != oldBoard            

        # Checks if the player won the game.
        winner = checkWon(gameBoard)
        # Checks if the game is over before the next iteration of the game loop.
        gameOver = checkGameOver(gameBoard)

        # Fills the game board if the game is continued and the board has shifted.
        if(not (gameOver | winner)):
            if(change) & (move != ''):
                gameBoard = fillEmpty(gameBoard)
        else:
            # Displays the game board's final state.
            displayBoard(gameBoard)
            break
    
    # Loads the final message to the player.
    pygame.time.delay(10)
    font = pygame.font.SysFont('comic sans ms', 64)
    whatNow = False

    while not whatNow:
        if(gameOver):
            message = "Game Over!"
            t_color = SIXTEEN
            b_color = BLACK
        elif(winner):
            message = "You won!"
            t_color = BLACK
            b_color = GREEN

        # Displays the loaded message to screen.
        messageOutline = pygame.Rect(0, H//2 - 64, W, 128)
        endMessage = font.render(message, 0, t_color)
        pygame.draw.rect(WINDOW, b_color, messageOutline)
        WINDOW.blit(endMessage, (512//2 - len(message)*17, 512//2 - 48))
        pygame.display.update()

        # Lets the player choose to continue or quit after the game results.
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                whatNow = True
            if(event.type == pygame.QUIT):
                pygame.quit()
                return

    # Restart game if the player doesn't choose to quit.
    main()

if(__name__ == "__main__"):
    main()
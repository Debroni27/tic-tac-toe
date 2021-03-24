# Ввод координат происходит следующим образом:
# Вводится пара чисел через пробел, например 1 1, 1 2 и тд


def PrintBoard(_gameBoard):
    print(" \t1\t2\t3")
    for i in range(3):
        print(str(i +1) + "\t" + str(_gameBoard[i * 3]) + "\t" + str(_gameBoard[i * 3 + 1]) + "\t" + str(_gameBoard[i * 3 + 2]) + "\t")

def CreateGame():
    gameBoard = ["-" for i in range(9)]
    allowPositions = list(range(9))
    player = 1

    return gameBoard, allowPositions, player


def CheckWin(_gameBoard, _winPosition):
    _x = ["X", "X", "X"]
    _o = ["O", "O", "O"]

    for position in _winPosition:
        if _gameBoard[position[0]] == _gameBoard[position[1]] == _gameBoard[position[2]] != "-":
            return True

    return False;

def CalculatePosition(_allowPositions):
    position = input("Choose position: ")

    positionX, positionY = 0, 0

    if len(position) == 3:
        positionX = int(position[0]) - 1
        positionY = int(position[2]) - 1

    while 3 * positionX + positionY not in _allowPositions or len(position) != 3:
        print("Incorrect input. Try again!!!\n")
        position = input("Choose position: ")
        positionX = int(position[0]) - 1
        positionY = int(position[2]) - 1

    _allowPositions.remove(3 * positionX + positionY)

    return (positionX, positionY)

def Step(_gameBoard, _allowPositions, _player):
    PrintBoard(_gameBoard)

    position = CalculatePosition(_allowPositions)

    if _player % 2 == 0:
        _gameBoard[3 * position[0] + position[1]] = "O"
    elif _player % 2 != 0:
        _gameBoard[3 * position[0] + position[1]] = "X"

    _player += 1

    PrintBoard(_gameBoard)
    print("---------------------------")

    return (_gameBoard, _allowPositions, _player)

def Game():
    game = CreateGame()
    winPositions = ([0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6])

    while True:
        game = Step(*list(game))
        if CheckWin(game[0], winPositions):
            if game[2] % 2 == 0:
                print("'X' wins!!!")
            else:
                print("'O' wins!!!")
            break
        else:
            if game[2] == 10:
                break

Game()
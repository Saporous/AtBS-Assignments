board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(chessBoard):
    numPawns = 0
    numPieces = 0

    if ('wking' not in chessBoard.values()) or ('bking' not in chessBoard.values()):
        print('Missing King!')
        return False
    
    for position, piece in chessBoard.items():
        if position[0] > '8' or position[0] < '1' or position[1] > 'h' or position[1] < 'a':
            print(piece + ' is in invalid position ' + position)
            return False

    return True

isValidChessBoard(board)
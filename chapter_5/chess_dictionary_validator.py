board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
pieceDict = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

def isValidChessBoard(chessBoard):
    numPawnsW = 0
    numPawnsB = 0
    numPiecesW = 0
    numPiecesB = 0

    if ('wking' not in chessBoard.values()) or ('bking' not in chessBoard.values()):
        print('Missing King!')
        return False
    
    for position, piece in chessBoard.items():
        if position[0] > '8' or position[0] < '1' or position[1] > 'h' or position[1] < 'a':
            print(piece + ' is in invalid position ' + position)
            return False
        if piece[0] == 'w':
            numPiecesW += 1
        elif piece[0] == 'b':
            numPiecesB += 1
        else:
            print('Missing black/white indication: ' + piece)
            return False
        if piece[1:] not in pieceDict:
            print('Invalid piece: ' + piece[1:])
            return False
    if numPawnsW > 8:
        print('Too many pawns: ' + str(numPawnsW))
        return False
    if numPawnsB > 8:
        print('Too many pawns: ' + str(numPawnsB))
        return False
    if numPiecesW > 16:
        print('Too many pieces: ' + str(numPiecesW))
        return False
    if numPiecesB > 16:
        print('Too many pieces: ' + str(numPiecesB))
        return False
    return True

print(str(isValidChessBoard(board)))
chessBoardA = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} # valid setup
chessBoardB = {'1h': 'bking', '6c': 'wking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} # too many kings
chessBoardC = {'1a': 'wpawn', '2a': 'wpawn', '3a': 'wpawn', '4a': 'wpawn', '5a': 'wpawn', '6a': 'wpawn',
                 '7a': 'wpawn', '8a' : 'wpawn', '1b': 'wpawn', '1h': 'bking', '3e': 'wking'} # too many pawns
chessBoardD = {'1a': 'wpawn', '2a': 'wpawn', '3a': 'wpawn', '4a': 'wpawn', '5a': 'wpawn', '6a': 'wpawn', # too many white pieces
                 '7a': 'wpawn', '8a': 'wqueen', '1c': 'wbishop', '2c': 'wbishop', '3c': 'wqueen',
                 '4c': 'wknight', '5c': 'wknight', '6c': 'wrook', '7c': 'wrook', '8c': 'wrook',
                 '1b': 'wpawn', '1h': 'bking', '3e': 'wking'}
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
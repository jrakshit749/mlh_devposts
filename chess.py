class Chess_Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board_x=[]

        for x in range(8):
            board_y =[]
            for y in range(8):

                board_y.append('.')

            board_x.append(board_y)
        board_x[7][4] = 'K'
        board_x[7][3] = 'Q'
        board_x[7][2] = 'B'
        board_x[7][1] = 'N'
        board_x[7][0] = 'R'
        return board_x

class WHITE_KING(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WK = 7
        self.position_y_WK = 4
        self.symbol_WK = 'K'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE KING')
                destination_x_WK = int(input())
                destination_y_WK = int(input())


                if self.board[destination_x_WK][destination_y_WK] == '.' :

                    if ( abs(self.position_x_WK-destination_x_WK) <2 and abs(self.position_y_WK-destination_y_WK) < 2 ):
                        self.board[self.position_x_WK][self.position_y_WK] = '.'
                        self.position_x_WK = destination_x_WK
                        self.position_y_WK = destination_y_WK
                        self.board[self.position_x_WK][self.position_y_WK] = self.symbol_WK

                        return self.board
                        break

                    else:
                        print ('your move is invalid, please choose cooridnates again')
                        continue

            except:
                pass


class WHITE_QUEEN(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WQ = 7
        self.position_y_WQ = 3
        self.symbol_WQ = 'Q'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE QUEEN')
                destination_x_WQ = int(input())
                destination_y_WQ = int(input())


                if self.board[destination_x_WQ][destination_y_WQ] == '.' :

                    if (destination_x_WQ == self.position_x_WQ or destination_y_WQ==self.position_y_WQ or abs(self.position_x_WQ-destination_x_WQ) == abs(self.position_y_WQ-destination_y_WQ) ):
                        self.board[self.position_x_WQ][self.position_y_WQ] = '.'
                        self.position_x_WQ = destination_x_WQ
                        self.position_y_WQ = destination_y_WQ
                        self.board[self.position_x_WQ][self.position_y_WQ] = self.symbol_WQ

                        return self.board
                        break

                    else:
                        print ('your move is invalid, please choose cooridnates again')
                        continue

            except:
                pass

class WHITE_ROOK(Chess_Board):

    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WR = 7
        self.position_y_WR = 0
        self.symbol_WR = 'R'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE ROOK ')
                destination_x_WR = int(input())
                destination_y_WR = int(input())


                if self.board[destination_x_WR][destination_y_WR] == '.' :

                    if (destination_x_WR == self.position_x_WR or destination_y_WR==self.position_y_WR  ):
                        self.board[self.position_x_WR][self.position_y_WR] = '.'
                        self.position_x_WR = destination_x_WR
                        self.position_y_WR = destination_y_WR
                        self.board[self.position_x_WR][self.position_y_WR] = self.symbol_WR

                        return self.board
                        break

                    else:
                        print ('your move is invalid, please choose cooridnates again')
                        continue

            except:
                pass

class WHITE_BISHOP(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WB = 7
        self.position_y_WB = 2
        self.symbol_WB = 'B'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE BISHOP')
                destination_x_WB = int(input())
                destination_y_WB = int(input())


                if self.board[destination_x_WB][destination_y_WB] == '.' :

                    if  abs(self.position_x_WB-destination_x_WB) == abs(self.position_y_WB-destination_y_WB) :
                        self.board[self.position_x_WB][self.position_y_WB] = '.'
                        self.position_x_WB = destination_x_WB
                        self.position_y_WB = destination_y_WB
                        self.board[self.position_x_WB][self.position_y_WB] = self.symbol_WB

                        return self.board
                        break

                    else:
                        print ('your move is invalid, please choose cooridnates again')
                        continue

            except:
                pass

class WHITE_KNIGHT(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WKN = 7
        self.position_y_WKN = 1
        self.symbol_WKN = 'N'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE KNIGHT')
                destination_x_WKN = int(input())
                destination_y_WKN = int(input())


                if self.board[destination_x_WKN][destination_y_WKN] == '.' :

                    if abs(self.position_x_WKN-destination_x_WKN)**2 + abs(self.position_y_WKN-destination_y_WKN)**2 == 5 :
                        self.board[self.position_x_WKN][self.position_y_WKN] = '.'
                        self.position_x_WKN = destination_x_WKN
                        self.position_y_WKN = destination_y_WKN
                        self.board[self.position_x_WKN][self.position_y_WKN] = self.symbol_WKN

                        return self.board
                        break

                    else:
                        print ('your move is invalid, please choose cooridnates again')
                        continue

            except:
                pass

class Engine(Chess_Board):

    def __init__(self):
        WHITE_KING.__init__(self)
        WHITE_QUEEN.__init__(self)
        WHITE_ROOK.__init__(self)
        WHITE_BISHOP.__init__(self)
        WHITE_KNIGHT.__init__(self)
        Chess_Board.__init__(self)

    def play(self):
        print('Please write what figure you choose to move: white_king, white_queen, white_rook, white_bishop'
              'or white knight')

        while True:
            choice=str(input())
            if  choice == 'white_king':
                WHITE_KING.move(self)
                break
            elif  choice == 'white_queen':
                WHITE_QUEEN.move(self)
                break
            elif  choice == 'white_bishop':
                WHITE_BISHOP.move(self)
                break
            elif  choice == 'white_knight':
                WHITE_KNIGHT.move(self)
                break
            elif  choice == 'white_rook':
                WHITE_ROOK.move(self)
                break
            else:
                print ('please choose again')


    def display(self):
        for i in range (8):
            for j in range (8):
                print (self.board[i][j], end=' ')
            print ()


    c_engine = Engine()
    c_engine.display()
    c_engine.play()
    c_engine.display()
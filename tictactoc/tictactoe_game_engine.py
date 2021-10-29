class TictactocGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.'*self.SIZE*self.SIZE) #['.','.','.','.','.','.','.','.','.']
        self.turn = 'X'

    def show_board(self):   #학생
        print(self.board)
    def self_turn(self):

    def set(self,row,col):  #송이김밥
        # 행 열을 입력 받아서 ex(3,2) 인덱스 배열 (7) 변환
       self.board[self.SIZE*(row-1)+(col-1)]=self.turn

    def set_winner(self):
        # - 3줄
        # | 3줄
        # \
        # /
        return self.turn
        # 비기는 조건 : 다 채워졌을때 위의 것에 해당안됐을때: self.board에 '.'이 없는 상태
        # return 'd' #draw
    def change_turn(self): #학생
        #self.turn 'X'면 'O', 'O'면 'X'로
        pass
if __name__ == '__main__':
    game_engine = TictactocGameEngine()
    game_engine.show_board()        #...\n...\n...
    game_engine.set(3,2)
    game_engine.show_board()    #['.','.','.','.','.','.','.','X','.']
    game_engine.set(3,1)
    game_engine.set(3,3)
    print(game_engine.set_winner())
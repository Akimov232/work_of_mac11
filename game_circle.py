from tkinter import *
#TODO change import method , to from tkinter import module

#константы 
CANAVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANAVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'green'
EMPITY = NONE

# имена и шаги игроков 
X = 'player 1 '
O = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self , start_player ):
        super().__init__()
        self.canvas = Canvas(height=CANAVAS_SIZE , width=CANAVAS_SIZE , bg = BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>' , self.click_event)
        self.board = [
            [EMPITY , EMPITY , EMPITY] , 
            [EMPITY , EMPITY , EMPITY] , 
            [EMPITY , EMPITY , EMPITY] , 
        ]

    def build_grid(self , grid_color):
        for i in range(RATIO):
            if i == 1 or  i == 2:
                self.canvas.create_line(FIGURE_SIZE * i , 0 , FIGURE_SIZE * i ,CANAVAS_SIZE )
                self.canvas.create_line(0 , FIGURE_SIZE * i  ,CANAVAS_SIZE , FIGURE_SIZE * i )

    def render_cross(self , posX , posY ):
        f_size = self.figure_size
        self.canvas.create_line(posX , posY , posX + f_size , posY + f_size , fill='red' , width=5)
        self.canvas.create_line(posX + f_size , posY , posX , posY + f_size ,fill='red' , width=5 )

    def render_circle(self , posX , posY):
        """
        magick number
        """
        f_size = self.figure_size-5
        self.canvas.create_oval(posX + 4, posY+4 , posX + f_size, posY + f_size , outline='red' , width=5 )

    def winner(self , player=None):
        center = CANAVAS_SIZE // 2
        if player:
            text = f'Winner:{player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center , center , text=text , fill='white' , font='Arial 50')
        self.canvas.unbind('<Button-1>')


    
    def click_event(self , event):
        x_cord = event.x // FIGURE_SIZE
        y_cord = event.y //FIGURE_SIZE
        self.make_move(x_cord , y_cord)
        # print(x_cord , y_cord)

    def make_move(self , x , y):
        position = {0:0 , 1: 200 , 2: 400}
        current_player = self.current_player

        if self.board[x][y] == EMPITY:
            self.update_board(x , y)

        



    def update_board(self , x , y):
        c_player = self.current_player
        self.board[x][y] = c_player
        if self.check_win(self.board , c_player):
            self.winner(c_player)
        elif self.check_draw():
            self.winner()
        
    def check_win(self , board ,  player):
        flag = None 
        for i in board:
            if i in board == player:
                flag == True 
            else:
                flag == False 
        return flag 

    def check_draw(self , board , player):
        flag = None 
        for i in board:
            if i in board != player:
                flag == True 
            else:
                flag == False 
        return flag 
        



        
#запуск 
game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid('bleck')


#тестирование 
# game_v1.render_cross(0 , 0)
# game_v1.render_circle(FIGURE_SIZE , FIGURE_SIZE)
# game_v1.winner()
game_v1.check_draw()

#работа программы 
game_v1.mainloop()
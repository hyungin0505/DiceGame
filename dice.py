#############################################
###### Build: hyungin0505(KoGandhi05)  ######
#############################################

# Modules
import random as r
from tkinter import *
from tkinter .simpledialog import askstring

# Screen Settings
win = Tk()
win.title("Dice Game (KGD)")
win.geometry('630x550+200+200')
win.resizable(False,False)
win.iconbitmap(default = 'images/logo.ico')

point = int(askstring("MONEY", '        보유 중인 잔액을 입력해주세요           '))

# Important Variable
double_b = 4 # 더블 배수
game = 0 
MIN = 1 # 배팅 최소 포인트 
MAX = 100000000000 # 배팅 최고 포인트

# Frame Sets
########################################################################
# Point, Bat Point, Games Frame
curr_frame = Frame(win)
curr_frame.grid(row = 0, column = 0, padx = (5,0), pady = (10, 0))

# Select, Console Frame
result_frame = Frame(win)
result_frame.grid(row = 1, column = 0, padx = (5,0), pady = (10, 0))

# Dice Frame
img_frame = Frame(win)
img_frame.grid(row = 2, column = 0, padx = (15,0), pady = (10, 0))

# Button Frame
play_frame = Frame(win)
play_frame.grid(row = 3, column = 0, pady = (25, 0))
########################################################################

# Point Frame Section
###########################################################
point_all = Label(curr_frame,
    text = '잔액', font = 'Dotum 16 bold',
    bg = 'lightgray',
    padx = 5,
    highlightbackground = "gray",
    highlightthickness = 1
    )
R_W = Label(curr_frame,
    text = "{}".format(point), font = "Dotum 16 bold",
    width = 10, height = 1,
    highlightbackground = "gray",
    highlightthickness = 1
    )
point_all.grid(row = 0, column = 0, pady = (5, 5))
R_W.grid(row = 0, column = 1, pady = (5,5))
############################################################

# Bat Point Section
#########################################################################
point_bat = Label(curr_frame,
    text = '배팅', font = 'Dotum 16 bold',
    bg = 'lightgray',
    padx = 5,
    highlightbackground = "gray",
    highlightthickness = 1
    )
B_W = Entry(curr_frame,
    font = "Dotum 16 bold",
    width = 10,
    highlightbackground = "gray",
    highlightthickness = 1
    )
point_bat.grid(row = 0, column = 2, padx = (10,0), pady = (5, 5))
B_W.grid(row = 0, column = 3, pady = (5,5))
B_W.insert(0, "0")
########################################################################

# Game Frame Section
#########################################################################
games = Label(curr_frame,
    text = '판수', font = 'Dotum 16 bold',
    bg = 'lightgray',
    padx = 5,
    highlightbackground = "gray",
    highlightthickness = 1
    )
G_W = Label(curr_frame,
    text = "0", font = "Dotum 16 bold",
    width = 5,
    highlightbackground = "gray",
    highlightthickness = 1
    )
games.grid(row = 0, column = 4, padx = (85,0), pady = (5, 5))
G_W.grid(row = 0, column = 5, pady = (5,5))
########################################################################

# Select, Result(Console) Frame Section
############################################################################
typ = IntVar()

# odd, even, double CheckBox
ODD = Radiobutton(result_frame, text = "홀수", variable = typ, value = 0)
EVEN = Radiobutton(result_frame, text = "짝수", variable = typ, value = 1)
DOUB = Radiobutton(result_frame, text = "더블", variable = typ, value = 2)

ODD.grid(row = 0, column = 0)
EVEN.grid(row = 1, column = 0)
DOUB.grid(row = 2, column = 0)

Result = Text(result_frame,
    font = "Dotum 12 bold",
    width = 60, height = 7,
    highlightbackground = "gray",
    highlightthickness = 1
    )
Result.grid(row = 0, column = 1, rowspan= 3, padx = (10,0), pady = (0,0))
############################################################################

# DiceImage Sets
############################################################################
dice0 = PhotoImage(file = "images/white.png").zoom(5)
dice1 = PhotoImage(file = "images/dice_1.png").zoom(5)
dice2 = PhotoImage(file = "images/dice_2.png").zoom(5)
dice3 = PhotoImage(file = "images/dice_3.png").zoom(5)
dice4 = PhotoImage(file = "images/dice_4.png").zoom(5)
dice5 = PhotoImage(file = "images/dice_5.png").zoom(5)
dice6 = PhotoImage(file = "images/dice_6.png").zoom(5)

DICE1 = Label(img_frame, image = dice0)
DICE2 = Label(img_frame, image = dice0)
DICE1.grid(row = 0, column = 0, padx = (0,15), pady = (0,0))
DICE2.grid(row = 0, column = 1, padx = (0,15), pady = (0,0))
############################################################################

# Dice1 Random
def shuf1():
    global shuf_t1
    shuf_t1 = r.randint(1,6)
    if shuf_t1 == 1:
        DICE1.config(image = dice1)
    elif shuf_t1 == 2:
        DICE1.config(image = dice2)
    elif shuf_t1 == 3:
        DICE1.config(image = dice3)
    elif shuf_t1 == 4:
        DICE1.config(image = dice4)
    elif shuf_t1 == 5:
        DICE1.config(image = dice5)
    elif shuf_t1 == 6:
        DICE1.config(image = dice6)

# Dice2 Random
def shuf2():
    global shuf_t2
    shuf_t2 = r.randint(1,6)
    if shuf_t2 == 1:
        DICE2.config(image = dice1)
    elif shuf_t2 == 2:
        DICE2.config(image = dice2)
    elif shuf_t2 == 3:
        DICE2.config(image = dice3)
    elif shuf_t2 == 4:
        DICE2.config(image = dice4)
    elif shuf_t2 == 5:
        DICE2.config(image = dice5)
    elif shuf_t2 == 6:
        DICE2.config(image = dice6)

# Roll Dice Function
def roll():
    global point, game
    bat_p = B_W.get()
    if int(bat_p) < MIN:
        Result.delete("1.0", END)
        Result.insert(END, "배팅은 최소 {}만원만 가능합니다.\n\n\n\n\n".format(MIN))
        game = int(game) - 1
    elif int(bat_p) > MAX:
        Result.delete("1.0", END)
        Result.insert(END, "배팅은 최대 {}만원만 가능합니다.\n\n\n\n\n".format(MAX))
        game = int(game) - 1
    else:
        if int(bat_p) > point:
            Result.delete("1.0", END)
            Result.insert(END, "잔액이 부족합니다.")
            game = int(game) - 1
        else:
            B_W.delete(0, END)
            B_W.insert(0, "0")
            Result.delete("1.0", END)
            Result.insert(END, "주사위를 굴립니다")
            
            shuf1()
            shuf2()

            Result.delete("1.0", END)
            Result.insert(END, "첫 번째 주사위는 {}입니다.\n\n".format(shuf_t1))
            Result.insert(END, "두 번째 주사위는 {}입니다.\n\n".format(shuf_t2))

            opt = typ.get()
            shuf = shuf_t1 + shuf_t2
            if shuf % 2 == 1:
                shuf_l = "홀수"
            elif shuf %2 == 0 and shuf_t1 != shuf_t2:
                shuf_l = "짝수"
            elif shuf_t1 == shuf_t2:
                shuf_l = "더블"

            if opt == 0:
                if shuf % 2 == 0:
                    Result.insert(END, "합은 {}로 {}만원을 잃었습니다.".format(shuf_l, bat_p))
                    point = point - int(bat_p)
                elif shuf % 2 == 1:
                    Result.insert(END, "합은 {}로 {}만원을 얻었습니다.".format(shuf_l, bat_p))
                    point = point + int(bat_p)
                elif shuf_t1 == shuf_t2:
                    Result.insert(END, "합은 {}로 {}만원을 잃었습니다.".format(shuf_l, bat_p))
                    point = point - int(bat_p)
            elif opt == 1:
                if shuf % 2 == 0 and shuf_t1 != shuf_t2:
                    Result.insert(END, "합은 {}로 {}만원을 얻었습니다.".format(shuf_l, bat_p))
                    point = point + int(bat_p)
                elif shuf % 2 == 1:
                    Result.insert(END, "합은 {}로 {}만원을 잃었습니다.".format(shuf_l, bat_p))
                    point = point - int(bat_p)
                elif shuf_t1 == shuf_t2:
                    Result.insert(END, "합은 {}로 {}만원을 잃었습니다.".format(shuf_l, bat_p))
                    point = point - int(bat_p)
            elif opt == 2:
                if shuf_t1 == shuf_t2:
                    Result.insert(END, "합은 {}로 {}만원을 얻었습니다.".format(shuf_l, bat_p))
                    point = point + (double_b * int(bat_p))
                elif shuf_t1 != shuf_t2:
                    Result.insert(END, "합은 {}로 {}만원을 잃었습니다.".format(shuf_l, bat_p))
                    point = point - int(bat_p)
    if point == 0:
        play.config(state = DISABLED)
        Result.delete("1.0", END)
        Result.insert(END, "돈을 모두 잃었습니다. \n재시작하려면 프로그램을 다시 실행해주세요.")
        play.config(state = DISABLED)


    R_W.config(text = point)
    game = int(game) + 1
    G_W.config(text = str(game))

    if game < 0:
        R_W.delete("1.0", END)
        R_W.insert("버그가 발생했습니다. \n재시작하려면 프로그램을 다시 실행해주세요.")

# Roll Btn Frame Section
############################################################################
play = Button(play_frame,
    text = '주사위 굴리기',
    font = "Dotum 16 bold",
    bg = "gray",
    fg = "white",
    height = 2,
    command = roll,
    state = NORMAL
    )
play.grid(row = 0, column = 0, padx = (0,0))
############################################################################

# Console Default Message
Result.delete("1.0", END)
Result.insert(END, "위에 배팅할 포인트를 입력하시고 왼쪽의 배팅 항목을 선택 후,\n아래 굴리기 버튼을 눌러주세요.\n두 주사위의 눈의 합을 예측하는 게임입니다.\n(배율: 홀/짝 - 2배, 더블 - {}배)\n\n부주의로 인해 포인트를 잃는 것을 방지하기 위해 천천히 신중하게 \n게임해주세요.".format(double_b))

win.mainloop()
# 고간디

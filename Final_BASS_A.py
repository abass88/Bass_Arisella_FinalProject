from tkinter import *
import random


# making main window,title,sizing, background color
main = Tk()
main.title("Rock, Paper, Scissors")
main.geometry("700x1000")

# Creating a label for main window
myLabel = Label(main, text="Let The Game Begin!!!")
myLabel.grid(row=0, column=2)

# Creating Images
computer_img = PhotoImage(file="robot.png")
play_img = PhotoImage(file="player1.png")
player_rock = PhotoImage(file="rock.png")
sm_player_rock = player_rock.subsample(3, 3)
player_paper = PhotoImage(file="paper.png")
sm_player_paper = player_paper.subsample(3, 3)
player_scissor = PhotoImage(file="sciss.png")
sm_player_scissor = player_scissor.subsample(3, 3)
com_rock = PhotoImage(file="rock.png")
com_paper = PhotoImage(file="paper.png")
com_scissor = PhotoImage(file="sciss.png")

# Labels for player, computer, and status
player_img = Label(main, image=play_img)
comp_img = Label(main, image=computer_img)
label_player = Label(main, text="PLAYER")
label_player.grid(row=1, column=1)
label_player.config(bg="black", fg="white")
label_computer = Label(main, text="COMPUTER")
label_computer.grid(row=1, column=3)
label_computer.config(bg="black", fg="white")
label_status = Label(main, text="", font=('arial', 20))
label_status.config(fg="red")
player_img.grid(row=2, column=1, padx=30, pady=20)
comp_img.grid(row=2, column=3, pady=20)
label_status.grid(row=3, column=2)


# Main Functions
def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()


def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()


def Scissor():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess()


def MatchProcess():
    com_choice = random.randint(1, 3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()

    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        ComputerScissor()


def ComputerRock():
    if player_choice == 1:
        label_status.config(text="Game is Tied. Play Again.")
    elif player_choice == 2:
        label_status.config(text="Player Wins!!!")
    elif player_choice == 3:
        label_status.config(text="Computer Wins!!!")


def MatchProcess():
    com_choice = random.randint(1, 3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()

    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        ComputerScissor()


def ComputerRock():
    if player_choice == 1:
        label_status.config(text="Game is Tied. Play Again.")
    elif player_choice == 2:
        label_status.config(text="Player Wins!!!")
    elif player_choice == 3:
        label_status.config(text="Computer Wins!!")


def ComputerPaper():
    if player_choice == 1:
        label_status.config(text="Computer Wins!!!")
    elif player_choice == 2:
        label_status.config(text="Game is Tied. Play Again.")
    elif player_choice == 3:
        label_status.config(text="Player Wins!!!")


def ComputerScissor():
    if player_choice == 1:
        label_status.config(text="Player Wins!!!")
    elif player_choice == 2:
        label_status.config(text="Computer Wins!!!")
    elif player_choice == 3:
        label_status.config(text="Game is Tied. Play Again.")


def ExitApp():
    main.destroy()
    exit()


# Buttons for player choice, and quit as well
rock = Button(main, image=sm_player_rock, command=Rock)
paper = Button(main, image=sm_player_paper, command=Paper)
scissor = Button(main, image=sm_player_scissor, command=Scissor)
btn_quit = Button(main, text="QUIT", command=ExitApp)
rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=2, pady=30)
scissor.grid(row=4, column=3, pady=30)
btn_quit.grid(row=5, column=2)

# Adding 2nd window,title,sizing, background color changed
main2 = Tk()
main2.title("Instructions")
main2.geometry("800x500")
main2.config(bg="black")

# Creating a label for main2 window
myLabel2 = Label(main2, text="Welcome!!!!!!", fg='white', bg='black')
myLabel2.grid()




main.mainloop()

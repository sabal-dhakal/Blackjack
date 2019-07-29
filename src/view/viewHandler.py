import tkinter as tk
from src.controller.blackjackController import BlackjackController


class BlackjackMain(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('BlackJack')

        # self.filename = 'bjtable.png'
        # self.bg_image = tk.PhotoImage(file=self.filename)
        #
        # # get the width and height of the image
        # self.w = self.bg_image.width()
        # self.h = self.bg_image.height()
        # # size the window so the image will fill it
        # self.master.geometry("%dx%d+50+30" % (self.w, self.h))
        # self.cv = tk.Canvas(width=self.w, height=self.h)
        # self.cv.pack(side='top', fill='both', expand='yes')
        # self.cv.create_image(0, 0, image=self.bg_image, anchor='nw')

        self.frame_dealer = tk.Frame(self.master)
        self.frame_dealer.grid(row=0, column=0, columnspan=3)
        self.label_dealer = tk.Label(self.frame_dealer, text="Dealer")

        self.frame_player = tk.Frame(self.master)
        self.frame_player.grid(row=1, column=0, columnspan=3)
        self.label_player = tk.Label(self.frame_player, text="Player")

        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.grid(row=2, column=0, columnspan=3)

        self.new_game()

    def new_game(self):
        self.curGame = BlackjackController()



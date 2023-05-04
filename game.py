from tkinter import *
from tkinter import ttk, font, messagebox
from random import randint
import os
from time import time

main_directory = os.getcwd()


class Game:
    x1, x2, y1, y2 = None, None, None, None
    add, amount, seconds, level, score, stop2 = 40, 0, 15, 1, 0, 5
    amount1, amount2, amount3 = amount, amount, amount
    high_score = int()
    hard, hard2 = 0, 0
    resume = False

    def background_1(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background.png")

    def background_2(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background2.png")

    def background_3(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background3.png")

    def background_4(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background4.png")

    def background_5(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background5.png")

    def background_6(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background6.png")

    def background_7(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background7.png")

    def background_8(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background8.png")

    def background_9(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background9.png")

    def background_10(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background10.png")

    def background_11(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background11.png")

    def background_12(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background12.png")

    def background_13(self):
        os.chdir(main_directory + "/Click game/Pictures")
        self.photo.configure(file="background13.png")

    def pause(self):
        self.text_font.set("Pause")
        messagebox.showinfo("Paused", "The game is paused. If you wish to continue, please click on the window.")
        self.rest()

    def rest(self):
        self.canvas.delete(self.e)
        self.resume = False

    def restart(self):
        self.rest()
        self.text_font.set("Resume")
        self.amount, self.amount1, self.amount2, self.add, self.seconds, self.level, \
            self.amount3, self.score, self.stop2, self.hard, self.hard2 = 0, 0, 0, 40, 15, 1, 0, 0, 5, 0, 0

        self.text_2.set("Score: {0.score}\t\t\t\t\t\t\t\tLevel: {0.level}".format(self))

    def open(self):
        self.rest()
        os.chdir(main_directory + "/Click game/Save")

        def select_file(event=None):
            try:
                if files_amount != 0:
                    widget_ = event.widget
                    index = int(widget_.curselection()[0])
                    value1 = widget_.get(index)
                    text.delete(0, "end")
                    text.insert(0, value1)
            except IndexError:
                pass

        def open2():
            file = text.get()
            if file != "":
                if os.path.exists(os.getcwd() + "/" + file + ".py"):
                    files = open(file + ".py", "r")
                    info = []
                    for lines in files:
                        lines = lines.split("=")
                        lines = lines[1].split("\n")
                        info.append(lines[0])
                    files.close()
                    self.score = int(info[0])
                    self.amount = int(info[1])
                    quits()

        def quits():
            root2.destroy()
            root2.quit()

        root2 = Tk()
        root2.geometry("202x258")
        root2.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 10", width=4, padding=4)

        num = StringVar()
        text = Entry(root2, textvariable=num, font=30, insertwidth=1, bd=10)
        text.pack(side=BOTTOM)

        label = LabelFrame(root2, text="Saved games", padx=5, pady=5)
        label.pack(side=TOP)

        cancel = ttk.Button(root2, text="cancel", command=quits)
        cancel.pack(side=RIGHT)
        save = ttk.Button(root2, text="load", command=open2)
        save.pack(side=RIGHT)

        lists = Listbox(label)
        files_amount = 0
        for line in os.listdir(os.getcwd()):
            if line != "high score.py" and line.endswith(".py"):
                files_amount += 1
                line = line.split(".")
                lists.insert(files_amount, line[0])
        lists.pack()
        lists.bind("<<ListboxSelect>>", select_file)
        root2.mainloop()

        self.add, self.seconds, self.level, self.stop2, self.hard, self.hard2 = 40, 15, 1, 5, 0, 0
        self.amount1, self.amount2, self.amount3 = self.amount, self.amount, self.amount
        while self.amount1 > 4:
            self.time1 = time()
            self.time2 = time()
            self.check()
        messagebox.showinfo("Instructions", "Now click anywhere on the screen to start.")
        self.high_score_track("read")

    def high_score_track(self, track):
        os.chdir(main_directory + "/Click game/Save")
        if track == "rewrite":
            highest = open("high score.py", "w")
            highest.write("high_score = {}".format(self.high_score))
            highest.close()
        if track == "read":
            highest = open("high score.py", "r")
            for line in highest:
                line = line.split("=")
                self.high_score = int(line[1])
        if track == "show":
            self.rest()
            messagebox.showinfo("High score", "High score: {}".format(self.high_score))
        if track == "reset":
            highest = open("high score.py", "w")
            highest.write("high_score = 0")
            highest.close()

    def save(self):
        self.rest()
        os.chdir(main_directory + "/Click game/Save")

        def select_file(event=None):
            try:
                if files_amount != 0:
                    widget_ = event.widget
                    index = int(widget_.curselection()[0])
                    value1 = widget_.get(index)
                    text.delete(0, "end")
                    text.insert(0, value1)
            except IndexError:
                pass

        def save2():
            file = text.get()
            if file != "":
                if os.path.exists(os.getcwd() + "/" + file + ".py"):
                    ask = messagebox.askquestion("Replace", "Do you want to rewrite your game?")
                    if ask == "yes":
                        files = open(file + ".py", "w")
                        files.write("Score = {0.score}\namount = {0.amount}".format(self))
                        files.close()
                        quits()
                if not os.path.exists(os.getcwd() + "/" + file + ".py"):
                    files = open(file + ".py", "w")
                    files.write("Score = {0.score}\namount = {0.amount}".format(self))
                    files.close()
                    quits()

        def delete_2():
            file = text.get()
            if file != "":
                if os.path.exists(file + ".py"):
                    info = []
                    w = open(file + ".py", "r")
                    for word in w:
                        info.append(word)
                    w.close()
                    os.remove(file + ".py")
                    os.chdir(main_directory + "/Click game/Save/Recovery")
                    w = open(file + ".py", "w")
                    for word in info:
                        w.write(word)
                    w.close()
                    os.chdir(main_directory + "/Click game/Save")
                    files_amount_2 = 0
                    lists.delete(0, "end")
                    for line_2 in os.listdir(os.getcwd()):
                        if line_2 != "high score.py" and line_2.endswith(".py"):
                            files_amount_2 += 1
                            line_2 = line_2.split(".")
                            lists.insert(files_amount_2, line_2[0])

        def quits():
            root2.destroy()
            root2.quit()

        root2 = Tk()
        root2.geometry("228x258")
        root2.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 10", width=4, padding=4)

        num = StringVar()
        text = Entry(root2, textvariable=num, font=30, insertwidth=1, bd=10)
        text.pack(side=BOTTOM)

        label = LabelFrame(root2, text="Saved games", padx=5, pady=5)
        label.pack(side=TOP)

        cancel = ttk.Button(root2, text="cancel", command=quits)
        cancel.pack(side=RIGHT)
        delete = ttk.Button(root2, text="delete", command=delete_2)
        delete.pack(side=RIGHT)
        save = ttk.Button(root2, text="save", command=save2)
        save.pack(side=RIGHT)

        lists = Listbox(label)
        files_amount = 0
        for line in os.listdir(os.getcwd()):
            if line != "high score.py" and line.endswith(".py"):
                files_amount += 1
                line = line.split(".")
                lists.insert(files_amount, line[0])
        lists.pack()
        lists.bind("<<ListboxSelect>>", select_file)
        root2.mainloop()

    def instructions(self, which):
        self.rest()
        if which == "play game":
            messagebox.showinfo("Instructions", "To start this game, click the window's screen. Then, a circle would "
                                                "appear somewhere on the screen. You have to click the circle before "
                                                "it is too late. After that, the circle would disappear and reappear "
                                                "someplace else. It will get harder as you score more points. your "
                                                "score will drop if you lost. If your score is less than -10, then you"
                                                " lose.")
        if which == "resuming":
            messagebox.showinfo("Resume", "Click anywhere on the game screen to resume.")

        if which == "Losing":
            messagebox.showinfo("Lost", "If your score is less than -10, You lose.")

        if which == "Win":
            messagebox.showinfo("Win", "To win, you must complete 13 levels.")

    def oval(self, event=None):
        self.resume = True
        self.time1 = time()
        if event.x in self.num and event and event.y in self.num2:
            self.amount += 1
            self.amount1 += 1
            self.amount2 += 1
            self.amount3 += 1
            self.score += 1
        self.check()
        coordinate = self.cord(0)
        self.canvas.delete(self.e)
        self.num.clear()
        self.num2.clear()
        for i in range(0, self.add + 1):
            self.num.append(self.x1 + i)
            self.num2.append(self.y1 + i)

        self.e = event.widget.create_oval(coordinate, outline=self.color[self.level-1],
                                          fill=self.color2[self.level-1], width=2)
        if self.amount > 80:
            coordinate = self.cord(1)
            event.widget.create_oval(coordinate, outline=self.color[self.level-1], fill=self.color2[self.level-1],
                                     width=4)

        if self.amount > 120:
            coordinate = self.cord(-1)
            event.widget.create_oval(coordinate, outline=self.color[self.level-1], fill=self.color2[self.level-1],
                                     width=1)
        if self.amount > 180:
            coordinate = self.cord(0.5)
            event.widget.create_oval(coordinate, outline=self.color[self.level-1], fill=self.color2[self.level-1],
                                     width=3)

        self.text_2.set("Score: {0.score}\t\t\t\t\t\t\t\tLevel: {0.level}".format(self))

    def cord(self, how_much):
        self.x1 = randint(0, 450)
        self.x2 = self.x1 + self.add + how_much
        self.y1 = randint(0, 450)
        self.y2 = self.y1 + self.add + how_much

        cord = self.x1, self.y1, self.x2, self.y2
        return cord

    def lost(self, event=None):
        self.time2 = time()
        if self.time2 - self.time1 > self.seconds and self.resume:
            self.score -= self.stop2
            if self.score > -11:
                self.amount += 1
                self.amount1 += 1
                self.amount2 += 1
                self.amount3 += 1
                self.oval(event)

            if self.score < -10:
                self.text_2.set("Score: {0.score}\t\t\t\t\t\t\t\tLevel: {0.level}".format(self))
                messagebox.showinfo("Lost", "You lost. Your score is {}".format(self.score))
                self.restart()

    def won(self, event=None):
        self.canvas.delete(self.e)
        messagebox.showinfo("Won", "Congratulations, You won. You reached level 13. Now, you can start again.")
        self.save()
        self.restart()

    def check(self):
        if self.amount1 / 5 >= 1:
            self.add -= 1
            self.amount1 -= 5

        if self.amount2 / 10 >= 1:
            self.seconds -= 1
            self.amount2 -= 10
            self.stop2 += 2

        if self.amount > 30 and self.hard == 0:
            self.hard += 1
        if self.hard == 1:
            self.seconds -= 7
            self.hard += 1

        if self.amount >= 70 and self.hard == 2:
            self.hard += 1
        if self.hard == 3:
            self.seconds += 9
            self.hard += 1

        if self.amount >= 110 and self.hard == 4:
            self.hard += 1
        if self.hard == 5:
            self.seconds -= 2
            self.hard += 1

        if self.amount >= 130 and self.hard == 6:
            self.hard += 1
        if self.hard == 7:
            self.seconds += 6
            self.hard += 1

        if self.amount > 45 and self.hard2 == 0:
            self.hard2 += 1
        if self.hard2 == 1:
            self.add -= 20
            self.hard2 += 1

        if self.amount > 65 and self.hard2 == 2:
            self.hard2 += 1
        if self.hard2 == 3:
            self.add += 30
            self.hard2 += 1

        if self.amount >= 90 and self.hard2 == 4:
            self.hard2 += 1
        if self.hard2 == 5:
            self.add -= 16
            self.hard2 += 1

        if self.amount >= 140 and self.hard2 == 6:
            self.hard2 += 1
        if self.hard2 == 7:
            self.add += 9
            self.hard2 += 1

        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_track("rewrite")

        if self.amount < 196:
            self.canvas.delete(self.pic)
            self.pic = self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
            self.pictures[self.level-1]()

        if self.amount3 / 15 >= 1:
            self.level += 1
            self.amount3 -= 15
            text_font = font.Font(family="Helvetica", size=40, weight="bold", slant="italic")
            self.canvas.create_text(250, 250, fill="dark blue", font=text_font, text="Level {}".format(self.level))

        if self.amount == 195:
            self.won()

    @staticmethod
    def recovery():
        line = os.listdir(main_directory + "/Click game/Save/Recovery")
        os.chdir(main_directory + "/Click game/Save/Recovery")
        while len(line) > 9:
            os.remove(line[0])
            line = os.listdir(main_directory + "/Click game/Save/Recovery")

    def button_click(self, event=None):
        if not self.resume:
            self.text_font.set("Resume")
            self.time1 = time()
            self.time2 = time()
            self.oval(event)
        if event.x in self.num and event and event.y in self.num2:
            if self.time2 - self.time1 <= self.seconds:
                self.oval(event)

    def __init__(self, root):

        self.recovery()

        # --- Photo ---
        self.photo = PhotoImage()
        self.background_1()
        self.photo_label = Label(root, image=self.photo)
        self.canvas = Canvas(root, width=500, height=500)
        self.canvas.pack(fill=BOTH, expand=TRUE)
        self.pic = self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        root.resizable(width=False, height=False)
        self.canvas.bind("<ButtonPress-1>", self.button_click)
        self.canvas.bind("<Motion>", self.lost)

        self.text_2 = StringVar()
        self.text_2.set("Score: {0.score}\t\t\t\t\t\t\t\tLevel: {0.level}".format(self))
        status = Label(root, textvariable=self.text_2, bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        self.time1 = time()
        self.time2 = time()

        self.num = []
        self.num2 = []
        the_menu = Menu(root)

        # --- choose menu ---
        self.text_font = StringVar()
        self.text_font.set("Resume")
        choose_menu = Menu(the_menu, tearoff=0)
        choose_menu.add_radiobutton(label="Restart", variable=self.text_font, command=self.restart)
        choose_menu.add_radiobutton(label="Pause", variable=self.text_font, command=self.pause)

        # --- File Menu ---
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_cascade(label="Load", command=self.open)
        file_menu.add_cascade(label="Save", command=self.save)
        the_menu.add_cascade(label="File", menu=file_menu)

        # --- View Menu ---
        view_menu = Menu(the_menu, tearoff=0)
        view_menu.add_cascade(label="Restart/Pause", menu=choose_menu)
        view_menu.add_cascade(label="High score", command=lambda: self.high_score_track("show"))
        the_menu.add_cascade(label="View", menu=view_menu)

        self.pictures = [self.background_1, self.background_2, self.background_3, self.background_4,
                         self.background_10,  self.background_11, self.background_12, self.background_5,
                         self.background_6,  self.background_7, self.background_8, self.background_9,
                         self.background_13]

        self.color = ["yellow green", "sea green", "dark olive green", "midnight blue", "midnight blue",
                      "dark slate gray", "Sky Blue", "red", "blue", "brown", "green", "yellow", "yellow"]

        self.color2 = ["dark turquoise", "DarkOliveGreen4", "khaki", "BurlyWood", "dark salmon", "white", "hot pink",
                       "red", "blue", "brown", "green", "yellow", "Dark Sea Green"]

        # --- Help Menu ---
        help_menu = Menu(the_menu, tearoff=0)
        help_menu.add_cascade(label="How to play", command=lambda: self.instructions("play game"))
        help_menu.add_cascade(label="How to resume", command=lambda: self.instructions("resuming"))
        help_menu.add_cascade(label="How do you lose", command=lambda: self.instructions("Losing"))
        help_menu.add_cascade(label="How to win", command=lambda: self.instructions("Win"))
        the_menu.add_cascade(label="Help", menu=help_menu)

        root.config(menu=the_menu)
        self.high_score_track("read")

        self.e = self.canvas.create_oval(50, 70, 80, 100)
        self.canvas.delete(self.e)


master = Tk()
master.title("Find the circle")

game = Game(master)

master.mainloop()

import random
import time
import os
import pickle
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator

# data = [savetime,name,plays,wins,losses,winnings,wagers,histories,t_plays,t_wins,t_losses,t_winnings,t_wager]

COLOR = "#A2416B"

t_money = "0.00"

def loading() -> list:
    location = os.getcwd()+"\\BETTING_GAME\\file.bin"

    try:
        with open(location,"rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        newf = ["never saved", "player", [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [[], [], [], [], [], []], 0, 0, 0, 0.0, 0.0]
        return newf
    except Exception as er:
        print("Failed func 'loading'")
        print(er)

def saving(data) -> None:
    location = os.getcwd()+"\\BETTING_GAME\\file.bin"
    rawtime = time.localtime()
    data[0] = time.strftime("%d/%m/%Y, %H:%M:%S", rawtime)
    # [savetime,name,plays,wins,losses,winnings,wagers,histories,t_plays,t_wins,t_losses,t_winnings,t_wager]

    try:
        with open(location, 'wb') as file:
            pickle.dump(data, file)
    except Exception as er:
        print(er)

def submit(*args) -> None: 
    name = str(entry.get())
    
    if name == "":
        name_msg.config(text="Name is not optional",font=("",12),pady=5)
    else:
        try:
            name_msg.config(text="",font=("",1),pady=0)
        except Exception as e:
            print(e)
        finally:
            if messagebox.askyesno(title="User Name", message="Are you sure you want the name \""+name+"\"?\nYou cannot change this later!"):
                data=loading()
                data[1] = name
                saving(data)
                comselect()

def comselect() -> None:
    data = loading()
    
    for widget in root.winfo_children():
        if widget != title:
            widget.destroy()
    
    root.geometry("400x300")

    Label(root,bg=COLOR,fg = "yellow",text="Welcome "+data[1]+"! Feeling lucky?",font=("",12)).pack(pady=5)
    Label(root,bg=COLOR,fg="white",font=("",16),text="Select your preferred betting company").pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, padx=10)
    
    box=Frame(root, bg=COLOR)
    box.pack()

    supreme = Frame(box, bg=COLOR)
    supreme.grid(row=0,column=0,padx=5,pady=5)

    izizzi = Frame(box, bg=COLOR)
    izizzi.grid(row=0,column=1,padx=5,pady=5)

    Label(supreme, text="Supreme Ventures", font=("",12), bg=COLOR, fg="white").pack()
    Separator(supreme, orient="horizontal", takefocus=True).pack(fill=X, padx=10)
    Label(supreme, text="Cashpot\nHot Pick\nPick Three", font=("",12), bg=COLOR, fg="white").pack()
    Button(box, text="Play",command=lambda: games(0,0)).grid(row=1,column=0,padx=5,pady=5)

    Label(izizzi, text="Izizzi Games", font=("",12), bg=COLOR, fg="white").pack()
    Separator(izizzi, orient="horizontal", takefocus=True).pack(fill=X, padx=10)
    Label(izizzi, text="1 Drop\n4 Play\nlucky Day Lotto", font=("",12), bg=COLOR, fg="white").pack()
    Button(box, text="Play",command=lambda: games(0,3)).grid(row=1,column=1,padx=5,pady=5)
    Separator(root, orient="horizontal").pack(fill=X, padx=10)

    bframe=Frame(root, bg=COLOR)
    bframe.pack()

    statsbtn=Button(bframe, command=history, text="History")
    statsbtn.grid(row=0,column=0,padx=5,pady=5)

    quitbtn=Button(bframe, command=quit, text="Quit")
    quitbtn.grid(row=0,column=1,padx=5,pady=5)

def games(company: int,num: int) -> None:
    from variables import GAMES,RULES,GAME_CONFIGS

    COMPANIES = ["Supreme Ventures","Izizzi Games"]

    root.geometry("600x450")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=COMPANIES[company]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)

    frame = Frame(root, bg=COLOR)
    frame.pack()

    """Loop isn't working so I'll break the law"""
    
    frame1 = Frame(frame,bg=COLOR,highlightbackground="white",highlightthickness=3)
    Button(frame1, font=("",12),text=GAMES[num],command=lambda: game_window(*GAME_CONFIGS[num])).pack(fill=X,padx=3,pady=3)
    Label(frame1,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame1,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame1,fg="yellow",bg=COLOR,font=("",12),text=RULES[num]).pack()

    frame2 = Frame(frame,bg=COLOR,highlightbackground="white",highlightthickness=3)
    Button(frame2, font=("",12),text=GAMES[num+1],command=lambda: game_window(*GAME_CONFIGS[num+1])).pack(fill=X,padx=3,pady=3)
    Label(frame2,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame2,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame2,fg="yellow",bg=COLOR,font=("",12),text=RULES[num+1]).pack()

    frame3 = Frame(frame,bg=COLOR,highlightbackground="white",highlightthickness=3)
    Button(frame3, font=("",12),text=GAMES[num+2],command=lambda: game_window(*GAME_CONFIGS[num+2])).pack(fill=X,padx=3,pady=3)
    Label(frame3,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame3,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame3,fg="yellow",bg=COLOR,font=("",12),text=RULES[num+2]).pack()

    frame1.grid(row=0,column=0,padx=5,pady=5,sticky="ns")
    frame2.grid(row=0,column=1,padx=5,pady=5,sticky="ns")
    frame3.grid(row=1,columnspan=2,padx=5,pady=5,sticky="we")

    Button(root, font=("",12),text="Back",command=lambda: comselect()).pack(side=BOTTOM, pady=10)

def game_window(game_num: int,min_wager: float,nums: int,max_num: int,fixed_wager = False) -> None:
    from variables import GAMES
    
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("600x460")

    Separator (root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=GAMES[game_num]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    frame=Frame(root,bg=COLOR)
    frame.pack()

    if fixed_wager:
        Label(frame,fg="white",bg=COLOR,font=("",12),text="Wager is fixed at $").grid(row=0,column=0,sticky="e")
        entry1 = Entry(frame, font=("",12),width=10)
        entry1.grid(row=0,column=1,padx=5)
        entry1.insert(0, str(min_wager))
        entry1.config(state="readonly",readonlybackground=COLOR)
    else:
        Label(frame,fg="white",bg=COLOR,font=("",12),text="Select your prefered wager $").grid(row=0,column=0,sticky="e")
        entry1 = Entry(frame, font=("",12),width=10,highlightbackground="red")
        entry1.grid(row=0,column=1,padx=5)
        entry1.insert(0, str(min_wager))
        entry1.focus()
    
    error1 = Label(frame,fg="white",bg=COLOR,font=("",0))
    error1.grid(row=1,columnspan=2)

    Label(frame,fg="white",bg=COLOR,font=("",12),text=f"Choose the lucky number (1-{max_num}):").grid(row=2,column=0)
    num_frame = Frame(frame,bg=COLOR)
    num_frame.grid(row=2,column=1,padx=3)
    entry_list = []

    for i in range(nums):
        entry_list.append(Entry(num_frame, font=("",12),width=10//nums,highlightbackground="red"))
        entry_list[i].grid(row=2,column=i+1,padx=6//nums)

    if nums > 1:
        entry_list[0].bind('<Return>', lambda event: entry_list[1].focus())
        entry_list[1].bind('<Return>', lambda event: entry_list[2].focus())
    
    if nums > 3: entry_list[2].bind('<Return>', lambda event: entry_list[3].focus())
    if nums > 4: entry_list[3].bind('<Return>', lambda event: entry_list[4].focus())

    if fixed_wager:
        entry_list[0].focus()
    else:
        entry1.bind('<Return>', lambda event: entry_list[0].focus())

    error2 = Label(frame,fg="white",bg=COLOR,font=("",0),highlightbackground="red")
    error2.grid(row=3,columnspan=2)

    Separator(frame, orient="horizontal", takefocus=True).grid(sticky="we",row=4,columnspan=3,pady=5)
    bframe = Frame(root, bg=COLOR)
    bframe.pack()
    play = Button(bframe,font=("",12),text="Play",command=lambda: playnums(game_num,max_num,play,entry1,min_wager,error1,error2,entry_list))
    play.grid(row=0,column=0,padx=5,pady=5)
    Button(bframe,font=("",12),text="Back",command=lambda: comselect()).grid(row=0,column=1,padx=5,pady=5)

def history() -> None:
    data = loading()
    
    for widget in root.winfo_children():
        widget.destroy()
    Separator(root, orient=HORIZONTAL,takefocus=True).pack(fill=X,pady=5)
    Label(root, text="||| History |||", 
        bg=COLOR, fg="yellow",
        pady=10, font = ("",18)).pack()
    Separator(root, orient=HORIZONTAL,takefocus=True).pack(fill=X,pady=5)
    frame=Frame(root, bg=COLOR)
    frame.pack()
    # [savetime,name,plays,wins,losses,winnings,wagers,histories,t_plays,t_wins,t_losses,t_winnings,t_wager]
    gameinfo = ["  You played "+str(data[8])+" games",  # Total games played
                "  You won "+str(data[9])+" games",     # Total games won
                "  You lost "+str(data[10])+" games"]   # Total ga,es lost
    for x in range(0,3):
        Label(frame,bg=COLOR,fg="white",font=("",12),text=gameinfo[x],justify=LEFT).pack()
    Separator(root, orient=HORIZONTAL,takefocus=True).pack(fill=X,pady=5)
    bframe = Frame(frame, bg=COLOR)
    bframe.pack()
    Button(bframe,text="back",command=lambda: comselect()).grid(row=0,column=0,padx=10,pady=10)
    Button(bframe,text="more info",command=playstats).grid(row=0,column=1,padx=10,pady=10)

def playstats() -> None:
    from variables import GAMES

    data = loading()
    root.bind("<Escape>", lambda: comselect())
    root.geometry("560x512")

    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text="||| Statistics |||", 
        bg=COLOR, fg="yellow",
        pady=10, font = ("",18)).pack()
    Separator(root, orient=HORIZONTAL,takefocus=True).pack(fill=X)
    
    box=Canvas(root, bg=COLOR)
    box.pack(side=LEFT,fill=BOTH,expand=1)
    bar=Scrollbar(box,orient="vertical",command=box.yview)
    bar.pack(side=RIGHT,fill=Y)
    box.configure(yscrollcommand=bar)
    box.bind("<Configure>", lambda event: box.configure(scrollregion=box.bbox("all")))
    box.bind_all("<MouseWheel>", lambda event: box.yview_scroll(-1*(event.delta//120), "units"))
    frame=Frame(box, bg=COLOR)
    box.create_window((0,0),window=frame,anchor="nw")
    
    frameA=Frame(frame,bg=COLOR)
    frameA.grid(row=0,column=0,padx=5)
    frameB=Frame(frame,bg=COLOR)
    frameB.grid(row=0,column=1,padx=5)

    # [savetime,name,plays,wins,losses,winnings,wagers,histories,t_plays,t_wins,t_losses,t_winnings,t_wager]
    Label(frameA, bg=COLOR, fg="white", font=("",16),text="Supreme Ventures").pack()
    Separator(frameA, orient=HORIZONTAL, takefocus=True).pack(fill=X)
    for x in range(0,3):
        Label(frameA,bg=COLOR,fg="white",font=("",12),
        text=f"You played \"{GAMES[x]}\" {str(data[2][x])} times\nWon {str(data[3][x])} and lost {str(data[4][x])}").pack()

    Label(frameB, bg=COLOR, fg="white", font=("",16),text=" Izizzi Games ").pack()
    Separator(frameB, orient=HORIZONTAL, takefocus=True).pack(fill=X)
    for x in range(3,6):
        Label(frameB,bg=COLOR,fg="white",font=("",12),
        text=f"You played \"{GAMES[x]}\" {str(data[2][x])} times\nWon {str(data[3][x])} and lost {str(data[4][x])}").pack()

    Label(frame, bg=COLOR, fg="white", font=("",16),text=" GAME HISTORY ").grid(row=1,columnspan=2,pady=(20,0))
    Separator(frame, orient=HORIZONTAL, takefocus=True).grid(row=2,columnspan=2,sticky="we")
    frame1 = Frame(frame,bg=COLOR)
    frame1.grid(row=3,column=0,sticky="n")
    frame2 = Frame(frame,bg=COLOR)
    frame2.grid(row=3,column=1,sticky="n")

    for i in range(0,3):
        Label(frame1, bg=COLOR, fg="white", font=("",12), text=GAMES[i]).pack()
        Separator(frame1, orient=HORIZONTAL, takefocus=True).pack(fill=X)

        if len(data[7][i]) == 0:
            Label(frame1,bg=COLOR,fg="yellow",text="Never played").pack()
        else:
            for j in range(0,(len(data[7][i]))):
                Label(frame1,bg=COLOR,fg="white",text=data[7][i][j]).pack()

    for i in range(3,6):
        Label(frame2, bg=COLOR, fg="white", font=("",12), text=GAMES[i]).pack()
        Separator(frame2, orient=HORIZONTAL, takefocus=True).pack(fill=X)

        if len(data[7][i]) == 0:
            Label(frame2,bg=COLOR,fg="yellow",text="Never played").pack()
        else:
            for j in range(0,(len(data[7][i]))):
                Label(frame2,bg=COLOR,fg="white",text=data[7][i][j]).pack()

    Separator(frame, orient=HORIZONTAL, takefocus=True).grid(columnspan=2,row=4,column=0,sticky="we")
    Label(frame, bg=COLOR, fg="white", font=("",12), text="You won a total of $"+str(t_money)).grid(columnspan=2,row=5,column=0)
    Label(frame, bg=COLOR, fg="white", font=("",12), text="and spent a total of $"+str(data[12])).grid(columnspan=2,row=6,column=0)
    Separator(frame, orient=HORIZONTAL, takefocus=True).grid(columnspan=2,row=7,column=0,sticky="we")

    Button(frame, font=("",12), text="Back", command=lambda: comselect()).grid(columnspan=2,row=8,pady=5)

def quit() -> None:
    data = loading()
    if messagebox.askyesno(title="Confirm Quit",
        message=f"{data[1]}, your current total is ${t_money}\n\nAre you sure you want to quit?)"):
        root.destroy()

def playnums(x: int,max_num: int,play: Button,entry1: Entry,min_wager: float,error1: Label,error2: Label,entry_list: list) -> None:
    from variables import GAME_CONFIGS
    
    global t_money
    player = []
    computer = []

    entry1.config(highlightthickness=0)
    error1.config(font=("",0),text="")

    for entry in entry_list:
        entry.config(highlightthickness=0)
    error2.config(font=("",0),text="")
    
    try:
        if entry1.get() == "": 
            entry1.config(highlightthickness=3)
            error1.config(fg="yellow",font=("",12),text="Wager is not Optional")
            return
        wager = float(entry1.get())
    except Exception as er:
        entry1.config(highlightthickness=3)
        error1.config(fg="yellow",font=("",12),text=str(er))
        return

    for entry in entry_list:
            try:
                if entry.get() == "":
                    entry.config(highlightthickness=3)
                    error2.config(fg="yellow",font=("",12),text="There is/are number(s) missing!")
                    return
                num = int(entry.get())
                if num > max_num or num < 1:
                    entry.config(highlightthickness=3)
                    error2.config(fg="yellow",font=("",12),text=f"Only numbers from 1-{max_num} are valid")
                    return
                player.append(num)
                computer.append(random.randint(1,max_num))
            except Exception as er:
                entry.config(highlightthickness=3)
                error2.config(fg="yellow",font=("",12),text=str(er))
                return

    if wager < min_wager: 
        entry1.config(highlightthickness=3)
        error1.config(fg="yellow",font=("",12),text=f"The minimum wager is ${min_wager}.00")
    else:
        play.config(state=DISABLED)
        data = loading()
        data[2][x] +=1      # total game plays
        data[8] +=1         # total plays
        data[6][x] += wager # total wager for the game
        data[12] += wager   # total wager
        result = f"You selected {str(player)},\nComputer played {str(computer)}"
        resultlbl = Label(root,bg=COLOR,fg="white",font=("",20),text=result)
        resultlbl.pack(pady=(12,0))

        player.sort()
        computer.sort()
        # [savetime,name,plays,wins,losses,winnings,wagers,histories,t_plays,t_wins,t_losses,t_winnings,t_wager]
        if player == computer:
            winmoney = calc_winnings(x,wager)
            data[5][x] += winmoney  # total winnings for the game
            data[11] += winmoney    # total winnings
            money = "{:,.2f}".format(winmoney)
            t_money = "{:,.2f}".format(data[11])

            Label(root,bg=COLOR,fg="green",font=("",24),text="YOU WIN!!!").pack()
            Label(root,bg=COLOR,fg="green",font=("",14),text="You earned $"+money).pack()
            data[3][x] +=1
            data[9] +=1

            T_H_A_W()
        else:
            Label(root,bg=COLOR,fg="white",font=("",14),text="You will be luckier next time").pack()
            data[4][x] +=1
            data[10] +=1

        data[7][x].append(result)
        data[7][x].append("You waged $"+str(wager))
        Button(root, font=("",12),text="Retry",command = lambda: game_window(*GAME_CONFIGS[x])).pack()

        saving(data)

def calc_winnings(x: int,wager: float) -> float:
    if x == 0:
        return wager * 26
    elif x == 1:
        return 1000
    elif x == 2:
        if wager == 40:
            return 1000
        elif wager < 60:
            return 4000
        else:
            return wager * 10
    elif x == 3:
        return wager * 27
    elif x == 4:
        return wager * 60
    else:
        return 100000

def T_H_A_W() -> bool:
    data = loading()

    if data[11] == 0:
        thaw = False
        return thaw
    elif (data[12]/data[11]) > 0.02:
        data[11] -= data[11]
        thaw = True
        saving(data)

        for widget in root.winfo_children():
            widget.destroy()
        root.geometry("640x440")
        Separator(root,orient=HORIZONTAL).pack(fill=X)
        Label(root,bg=COLOR,fg="red",font=("",18),text="!!!DO NOT LEAVE YOUR CURRENT LOCATION!!!").pack(pady=10)
        Separator(root,orient=HORIZONTAL).pack(fill=X)
        frame = Frame(root,bg=COLOR)
        frame.pack(pady=10)
        Label(frame,bg=COLOR,fg="blue",font=("",18),text="YOU ARE SOMEHOW WINNING FAR MORE THAN WHAT").pack()
        Label(frame,bg=COLOR,fg="blue",font=("",18),text="IS PROBABLE, YOU ARE SUSPECTED OF CHEATING").pack()
        Label(frame,bg=COLOR,fg="blue",font=("",18),text="WE ARE SENDING SOMEONE TO YOUR LOCATION").pack()
        Label(frame,bg=COLOR,fg="blue",font=("",18),text="PLEASE REMAIN SEATED AND CALM").pack()
        Separator(root,orient=HORIZONTAL).pack(fill=X)
        Label(root,bg=COLOR,fg="red",font=("",18),text="!!!DO NOT LEAVE YOUR CURRENT LOCATION!!!").pack(pady=10)
        Separator(root,orient=HORIZONTAL).pack(fill=X)
        frame2 = Frame(root,bg=COLOR)
        frame2.pack(pady=10)
        Label(frame2,bg=COLOR,fg="yellow",font=("",18),text="Your account has been emptied and\nyour IP Address has been collected").pack()
        Label(frame2,bg=COLOR,fg="yellow",font=("",18),text=f"{data[1]}, You won $0.00").pack()
        Button(root,text="QUIT", command=root.destroy).pack()
    else: thaw = False
    return thaw

# START ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__=="__main__":
    root = Tk() # Make window

    win_width = 400
    win_height = 250
    screen_width = int(root.winfo_screenwidth())
    screen_height = int(root.winfo_screenheight())
    
    x = int((screen_width/2) - (win_width/2))
    y = int((screen_height/2) - (win_height))

    root.geometry("{}x{}+{}+{}".format(win_width,win_height,x,y))
    root.title("Betting Game")
    root.config(background = COLOR)

    title = Label(root, text="||| JACKPOT |||", 
            bg=COLOR, fg="yellow",
            pady=10, font = ("",18),
            border=5, relief=SUNKEN)
    title.pack()
    Label(root, text="Welcome to Jackpot!!!", 
            bg=COLOR, fg="white",
            pady=10, font = ("",16)).pack()

    frame = Frame(root, bg=COLOR)
    frame.pack()

    Label(frame, text="What is your name?", 
            bg=COLOR, fg="white", font =("",12),
            pady=5,justify="left").pack()
    entry = Entry(frame, font=("",12))
    entry.bind('<Return>', submit)
    entry.pack(pady=5)
    entry.focus()

    name_msg = Label(frame,bg=COLOR,fg="red",font=("",1))
    name_msg.pack(side='bottom')

    frame1 = Frame(root, bg=COLOR)
    frame1.pack()
    frame2 = Frame(root, bg=COLOR)
    frame2.pack()

    Button(frame1, text="Submit", font=("",12),
            command=submit).pack(side = "left", padx=3)
    Button(frame1, text="Clear", font=("",12),
            command=lambda: entry.delete(0, END)).pack(side = "right", padx=3)

    root.after(500, lambda: messagebox.showinfo("Game Information",
    """    This is a game made by me, DI.
    I do not own any rights to these \"game\" titles.
    This \"game\" was made purely for practice.

    Enjoy if you can!"""))

    root.mainloop()
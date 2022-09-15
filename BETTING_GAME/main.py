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

def loading():
    location = os.getcwd()+"\\BETTING_GAME\\file.bin"

    try:
        with open(location,"rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        newf = ["never saved", "player", [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [[], [], [], [], [], []], 0, 0, 0, 0.0, 0.0]
        return newf
    except Exception as er:
        print(er)

def saving(data):
    location = os.getcwd()+"\\BETTING_GAME\\file.bin"
    rawtime = time.localtime()
    data[0] = time.strftime("%d/%m/%Y, %H:%M:%S", rawtime)
    # [savetime,name,plays,wins,losses,winnings,wagers,histories,t_plays,t_wins,t_losses,t_winnings,t_wager]

    try:
        with open(location, 'wb') as file:
            pickle.dump(data, file)
    except Exception as er:
        print(er)

def submit(*args): 
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

def comselect():
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
    Button(box, text="Play",command=gamesA).grid(row=1,column=0,padx=5,pady=5)
    Label(izizzi, text="Izizzi Games", font=("",12), bg=COLOR, fg="white").pack()
    Separator(izizzi, orient="horizontal", takefocus=True).pack(fill=X, padx=10)
    Label(izizzi, text="1 Drop\n4 Play\nlucky Day Lotto", font=("",12), bg=COLOR, fg="white").pack()
    Button(box, text="Play",command=gamesB).grid(row=1,column=1,padx=5,pady=5)
    Separator(root, orient="horizontal").pack(fill=X, padx=10)
    bframe=Frame(root, bg=COLOR)
    bframe.pack()
    statsbtn=Button(bframe, command=history, text="History")
    statsbtn.grid(row=0,column=0,padx=5,pady=5)
    quitbtn=Button(bframe, command=quit, text="Quit")
    quitbtn.grid(row=0,column=1,padx=5,pady=5)

def gamesA():
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text="Supreme Ventures").pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)

    frame = Frame(root, bg=COLOR)
    frame.pack()
    frame1 = Frame(frame, bg=COLOR,highlightbackground="white",highlightthickness=3)
    frame2 = Frame(frame, bg=COLOR,highlightbackground="white",highlightthickness=3)
    frame3 = Frame(frame, bg=COLOR,highlightbackground="white",highlightthickness=3)
    frame1.grid(row=0,column=0,padx=5,pady=5,sticky="ns")
    frame2.grid(row=0,column=1,padx=5,pady=5,sticky="ns")
    frame3.grid(row=1,columnspan=2,padx=5,pady=5,sticky="we")

    Button(frame1, font=("",12),text=GAMES[0],command=cashpot).pack(fill=X,padx=3,pady=3)
    Label(frame1,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame1,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame1,fg="yellow",bg=COLOR,font=("",12),
        text="Pick a number between 1 and 36.\nYou win if your selected number is\nrandomly generated.\nThe minimum wager is $10.00.\nPay-out is 26 times the wager.").pack()
    
    Button(frame2, font=("",12),text=GAMES[1],command=hotpick).pack(fill=X,padx=3,pady=3)
    Label(frame2,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame2,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame2,fg="yellow",bg=COLOR,font=("",12),
        text="Pick a number between 1 and 16.\nYou win if your selected number is\nrandomly generated.\nThe only wager applicable is $20.00.\nPay-out is fixed at $1,000.00.").pack()

    Button(frame3, font=("",12),text=GAMES[2],command=pickthree).pack(fill=X,padx=3,pady=3)
    Label(frame3,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame3,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame3,fg="yellow",bg=COLOR,font=("",12),
        text="Pick 3 numbers between 1 and 35.\nYou win if your selected numbers are randomly generated.\nThe minimum wager is $40.00.\nIf your wager is $40.00, pay-out $1,000.00.\nIf your wager is greater than $40.00 but less than $60.00,\npay-out is $4,000.00.\nIf your wager is $60.00 or greater, pay-out is 10 times your wager.").pack()

    Button(root, font=("",12),text="Back",command=lambda: comselect()).pack(side=BOTTOM, pady=10)

def gamesB():
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text="Izizzi Games").pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)

    frame = Frame(root, bg=COLOR)
    frame.pack()
    frame1=Frame(frame, bg=COLOR,highlightbackground="white",highlightthickness=3)
    frame2=Frame(frame, bg=COLOR,highlightbackground="white",highlightthickness=3)
    frame3=Frame(frame, bg=COLOR,highlightbackground="white",highlightthickness=3)
    frame1.grid(row=0,column=0,padx=5,pady=5,sticky="ns")
    frame2.grid(row=0,column=1,padx=5,pady=5,sticky="ns")
    frame3.grid(row=1,columnspan=2,padx=5,pady=5,sticky="we")

    Button(frame1, font=("",12),text=GAMES[3],command=onedrop).pack(fill=X,padx=3,pady=3)
    Label(frame1,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame1,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame1,fg="yellow",bg=COLOR,font=("",12),
        text="Pick a number between 1 and 36.\nYou win if your selected number is\nrandomly generated.\nThe minimum wager is $10.00.\nPay-out is 27 times the wager.").pack()
    
    Button(frame2, font=("",12),text=GAMES[4],command=fourplay).pack(fill=X,padx=3,pady=3)
    Label(frame2,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame2,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame2,fg="yellow",bg=COLOR,font=("",12),
        text="Pick 4 numbers between 1 and 15.\nYou win if your selected numbers are\nrandomly generated.\nThe minimum wager is $10.00.\nPay-out is 60 times the wager.").pack()

    Button(frame3, font=("",12),text=GAMES[5],command=ldlotto).pack(fill=X,padx=3,pady=3)
    Label(frame3,fg="yellow",bg=COLOR,font=("",12),text="How to play:")
    Separator(frame3,orient="horizontal", takefocus=True).pack(fill=X)
    Label(frame3,fg="yellow",bg=COLOR,font=("",12),
        text="Pick 5 numbers between 1 and 20.\nYou win if your selected numbers are randomly generated.\nThe only wager applicable is $40.00.\nThe pay-out is $100,000.00.\nIf your wager is greater than $40.00 but less than $60.00,\npay-out is $4,000.00.\nIf your wager is $60.00 or greater, pay-out is 10 times your wager.").pack()

    Button(root, font=("",12),text="Back",command=lambda: comselect()).pack(side=BOTTOM, pady=10)

def cashpot():
    min_wager = 10
    max_num = 36
    x = 0
    
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=GAMES[x]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    frame=Frame(root,bg=COLOR)
    frame.pack()

    Label(frame,fg="white",bg=COLOR,font=("",12),text="Select your prefered wager $").grid(row=0,columnspan=2,sticky="e")
    entry1 = Entry(frame, font=("",12),width=10)
    entry1.grid(row=0,column=2,padx=5)
    entry1.insert(0, str(min_wager))
    entry1.focus()
    error1 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error1.grid(row=1,columnspan=3)

    Label(frame,fg="white",bg=COLOR,font=("",12),text=f"Choose the lucky number (1-{max_num}) ").grid(row=2,columnspan=2)
    entry2 = Entry(frame, font=("",12),width=10)
    entry2.grid(row=2,column=2,padx=5)
    error2 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error2.grid(row=3,columnspan=3)
    entry1.bind('<Return>', lambda event: entry2.focus())

    Separator(frame, orient="horizontal", takefocus=True).grid(sticky="we",row=4,columnspan=3,pady=5)
    bframe = Frame(root, bg=COLOR)
    bframe.pack()
    play = Button(bframe,font=("",12),text="Play", command=lambda: playnums(x,max_num,play,entry1,min_wager,error1,error2,entry2))
    play.grid(row=0,column=0,padx=5,pady=5)
    Button(bframe,font=("",12),text="Back",command=lambda: comselect()).grid(row=0,column=1,padx=5,pady=5)

def hotpick():
    min_wager = 20
    max_num = 16
    x = 1
    
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=GAMES[x]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    frame=Frame(root,bg=COLOR)
    frame.pack()

    Label(frame,fg="white",bg=COLOR,font=("",12),text="The wager is fixed at $").grid(row=0,columnspan=2,sticky="e")
    entry1 = Entry(frame, font=("",12),width=10,bg=COLOR)
    entry1.grid(row=0,column=2,padx=5)
    entry1.insert(0, str(min_wager))
    entry1.config(state="readonly",readonlybackground=COLOR)
    error1 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error1.grid(row=1,columnspan=3)

    Label(frame,fg="white",bg=COLOR,font=("",12),text=f"Choose the lucky number (1-{max_num}) ").grid(row=2,columnspan=2)
    entry2 = Entry(frame, font=("",12),width=10)
    entry2.grid(row=2,column=2,padx=5)
    entry2.focus()
    error2 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error2.grid(row=3,columnspan=3)

    Separator(frame, orient="horizontal", takefocus=True).grid(sticky="we",row=4,columnspan=3,pady=5)
    bframe = Frame(root, bg=COLOR)
    bframe.pack()
    play = Button(bframe,font=("",12),text="Play", command=lambda: playnums(x,max_num,play,entry1,min_wager,error1,error2,entry2))
    play.grid(row=0,column=0,padx=5,pady=5)
    Button(bframe,font=("",12),text="Back",command=lambda: comselect()).grid(row=0,column=1,padx=5,pady=5)

def pickthree():
    min_wager = 40
    max_num = 16
    x = 2
    
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=GAMES[x]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    frame=Frame(root,bg=COLOR)
    frame.pack()

    Label(frame,fg="white",bg=COLOR,font=("",12),text="Select your prefered wager $").grid(row=0,column=0,sticky="e")
    entry1 = Entry(frame, font=("",12),width=10)
    entry1.grid(row=0,column=1,columnspan=3,padx=5,sticky="we")
    entry1.insert(0, str(min_wager))
    entry1.focus()
    error1 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error1.grid(row=1,columnspan=4)

    Label(frame,fg="white",bg=COLOR,font=("",12),text=f"Choose the lucky numbers (1-{max_num}) ").grid(row=2,column=0)
    entry2a = Entry(frame, font=("",12),width=3)
    entry2a.grid(row=2,column=1,padx=3)
    entry2b = Entry(frame, font=("",12),width=3)
    entry2b.grid(row=2,column=2,padx=1)
    entry2c = Entry(frame, font=("",12),width=3)
    entry2c.grid(row=2,column=3,padx=3)

    error2 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error2.grid(row=3,columnspan=4)

    entry1.bind('<Return>', lambda event: entry2a.focus())
    entry2a.bind('<Return>', lambda event: entry2b.focus())
    entry2b.bind('<Return>', lambda event: entry2c.focus())

    Separator(frame, orient="horizontal", takefocus=True).grid(sticky="we",row=4,columnspan=4,pady=5)
    bframe = Frame(root, bg=COLOR)
    bframe.pack()
    play = Button(bframe,font=("",12),text="Play", command=lambda: playnums(x,max_num,play,entry1,min_wager,error1,error2,entry2a,entry2b,entry2c))
    play.grid(row=0,column=0,padx=5,pady=5)
    Button(bframe,font=("",12),text="Back",command=lambda: comselect()).grid(row=0,column=1,padx=5,pady=5)

def onedrop():
    min_wager = 10
    max_num = 36
    x = 3
    
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=GAMES[x]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    frame=Frame(root,bg=COLOR)
    frame.pack()

    Label(frame,fg="white",bg=COLOR,font=("",12),text="Select your prefered wager $").grid(row=0,columnspan=2,sticky="e")
    entry1 = Entry(frame, font=("",12),width=10)
    entry1.grid(row=0,column=2,padx=5)
    entry1.insert(0, str(min_wager))
    entry1.focus()
    error1 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error1.grid(row=1,columnspan=3)

    Label(frame,fg="white",bg=COLOR,font=("",12),text=f"Choose the lucky number (1-{max_num}) ").grid(row=2,columnspan=2)
    entry2 = Entry(frame, font=("",12),width=10)
    entry2.grid(row=2,column=2,padx=5)
    error2 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error2.grid(row=3,columnspan=3)
    entry1.bind('<Return>', lambda event: entry2.focus())

    Separator(frame, orient="horizontal", takefocus=True).grid(sticky="we",row=4,columnspan=3,pady=5)
    bframe = Frame(root, bg=COLOR)
    bframe.pack()
    play = Button(bframe,font=("",12),text="Play", command=lambda: playnums(x,max_num,play,entry1,min_wager,error1,error2,entry2))
    play.grid(row=0,column=0,padx=5,pady=5)
    Button(bframe,font=("",12),text="Back",command=lambda: comselect()).grid(row=0,column=1,padx=5,pady=5)

def fourplay():
    min_wager = 10
    max_num = 15
    x = 4
    
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=GAMES[x]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    frame=Frame(root,bg=COLOR)
    frame.pack()

    Label(frame,fg="white",bg=COLOR,font=("",12),text="Select your prefered wager $").grid(row=0,column=0,sticky="e")
    entry1 = Entry(frame, font=("",12),width=10)
    entry1.grid(row=0,column=1,columnspan=4,padx=5,sticky="we")
    entry1.insert(0, str(min_wager))
    entry1.focus()
    error1 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error1.grid(row=1,columnspan=5)

    Label(frame,fg="white",bg=COLOR,font=("",12),text=f"Choose the lucky numbers (1-{max_num}) ").grid(row=2,column=0)
    entry2a = Entry(frame, font=("",12),width=3)
    entry2a.grid(row=2,column=1,padx=2)
    entry2b = Entry(frame, font=("",12),width=3)
    entry2b.grid(row=2,column=2,padx=1)
    entry2c = Entry(frame, font=("",12),width=3)
    entry2c.grid(row=2,column=3,padx=1)
    entry2d = Entry(frame, font=("",12),width=3)
    entry2d.grid(row=2,column=4,padx=2)

    error2 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error2.grid(row=3,columnspan=5)

    entry1.bind('<Return>', lambda event: entry2a.focus())
    entry2a.bind('<Return>', lambda event: entry2b.focus())
    entry2b.bind('<Return>', lambda event: entry2c.focus())
    entry2c.bind('<Return>', lambda event: entry2d.focus())

    Separator(frame, orient="horizontal", takefocus=True).grid(sticky="we",row=4,columnspan=5,pady=5)
    bframe = Frame(root, bg=COLOR)
    bframe.pack()
    play = Button(bframe,font=("",12),text="Play", command=lambda: playnums(x,max_num,play,entry1,min_wager,error1,error2,entry2a,entry2b,entry2c,entry2d))
    play.grid(row=0,column=0,padx=5,pady=5)
    Button(bframe,font=("",12),text="Back",command=lambda: comselect()).grid(row=0,column=1,padx=5,pady=5)

def ldlotto():
    min_wager = 20
    max_num = 20
    x = 5
    
    root.geometry("600x460")
    for widget in root.winfo_children():
        widget.destroy()
    
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    Label(root, bg=COLOR, fg="yellow", font=("",24),text=GAMES[x]).pack()
    Separator(root, orient="horizontal", takefocus=True).pack(fill=X, pady=5)
    frame=Frame(root,bg=COLOR)
    frame.pack()

    Label(frame,fg="white",bg=COLOR,font=("",12),text="The wager is fixed at $").grid(row=0,column=0,sticky="e")
    entry1 = Entry(frame, font=("",12),width=10)
    entry1.grid(row=0,column=1,columnspan=5,padx=5,sticky="we")
    entry1.insert(0, str(min_wager))
    entry1.config(state="readonly",readonlybackground=COLOR)
    error1 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error1.grid(row=1,columnspan=6)

    Label(frame,fg="white",bg=COLOR,font=("",12),text=f"Choose the lucky numbers (1-{max_num}) ").grid(row=2,column=0)
    entry2a = Entry(frame, font=("",12),width=3)
    entry2a.grid(row=2,column=1,padx=1)
    entry2b = Entry(frame, font=("",12),width=3)
    entry2b.grid(row=2,column=2,padx=1)
    entry2c = Entry(frame, font=("",12),width=3)
    entry2c.grid(row=2,column=3,padx=1)
    entry2d = Entry(frame, font=("",12),width=3)
    entry2d.grid(row=2,column=4,padx=1)
    entry2e = Entry(frame, font=("",12),width=3)
    entry2e.grid(row=2,column=5,padx=1)

    entry2a.focus()

    error2 = Label(frame,fg="white",bg=COLOR,font=("",1))
    error2.grid(row=3,columnspan=6)

    entry1.bind('<Return>', lambda event: entry2a.focus())
    entry2a.bind('<Return>', lambda event: entry2b.focus())
    entry2b.bind('<Return>', lambda event: entry2c.focus())
    entry2c.bind('<Return>', lambda event: entry2d.focus())
    entry2d.bind('<Return>', lambda event: entry2e.focus())

    Separator(frame, orient="horizontal", takefocus=True).grid(sticky="we",row=4,columnspan=6,pady=5)
    bframe = Frame(root, bg=COLOR)
    bframe.pack()
    play = Button(bframe,font=("",12),text="Play", command=lambda: playnums(x,max_num,play,entry1,min_wager,error1,error2,entry2a,entry2b,entry2c,entry2d))
    play.grid(row=0,column=0,padx=5,pady=5)
    Button(bframe,font=("",12),text="Back",command=lambda: comselect()).grid(row=0,column=1,padx=5,pady=5)

def history():
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
    Button(bframe,text="back",command=lambda name: comselect()).grid(row=0,column=0,padx=10,pady=10)
    Button(bframe,text="more info",command=playstats).grid(row=0,column=1,padx=10,pady=10)

def playstats():
    data = loading()
    root.bind("<Escape>", lambda name: comselect())
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
    frame1.grid(row=3,column=0)
    frame2 = Frame(frame,bg=COLOR)
    frame2.grid(row=3,column=1)

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

    Button(frame, font=("",12), text="Back", command=lambda name: comselect()).grid(columnspan=2,row=8,pady=5)

def quit():
    if messagebox.askyesno(title="Confirm Quit",message="Are you sure you want to quit?"):
        root.destroy()

def playnums(x,max_num,play,entry1,min_wager,error1,error2,*args):
    global t_money
    player = []
    computer = []

    try:
        wager = float(entry1.get())
    except Exception as er:
        error1.config(fg="yellow",font=("",12),text=str(er))
        return

    for entry in args:
            try:
                num = int(entry.get())
                if num > max_num or num < 1:
                    entry.config(highlightbackground="red",highlightthickness=1)
                    error2.config(fg="yellow",font=("",12),text=f"Only numbers from 1-{max_num} are valid")
                    return
                player.append(num)
                computer.append(random.randint(1,max_num))
            except Exception as er:
                entry.config(highlightbackground="red",highlightthickness=1)
                error2.config(fg="yellow",font=("",12),text=str(er))
                return

    if wager < min_wager:
        error1.config(fg="yellow",font=("",12),text=f"The minimum wager is ${min_wager}.00")
    else:
        play.config(state=DISABLED)
        data = loading()
        data[2][x] +=1      # total game plays
        data[8] +=1         # total plays
        data[6][x] += wager # total wager for the game
        data[12] += wager   # total wager
        result = f"You selected {str(player)}, computer played {str(computer)}"
        resultlbl = Label(root,bg=COLOR,fg="white",font=("",20),text=result)
        resultlbl.pack(pady=(12,0))

        player.sort()
        computer.sort()
        # [savetime,name,plays,wins,losses,winnings,wagers,histories,t_plays,t_wins,t_losses,t_winnings,t_wager]
        if player == computer:
            winmoney = wager * 26
            data[5][x] += winmoney  # total winnings for the game
            data[11] += winmoney    # total winnings
            money = "{:,.2f}".format(winmoney)
            t_money = "{:,.2f}".format(data[11])

            Label(root,bg=COLOR,fg="green",font=("",24),text="YOU WIN!!!")
            Label(root,bg=COLOR,fg="green",font=("",24),text="You earned $"+money)
            data[3][x] +=1
            data[9] +=1
        else:
            Label(root,bg=COLOR,fg="white",font=("",14),text="You will be luckier next time").pack()
            data[4][x] +=1
            data[10] +=1

        data[7][x].append(result)
        data[7][x].append("You waged $"+str(wager))
        Button(root, font=("",12),text="Retry",command = GAMES_F[x]).pack()

        saving(data)
        T_H_A_W()

def T_H_A_W():
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
        root.geometry("640x420")
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

GAMES_F = (cashpot,hotpick,pickthree,onedrop,fourplay,ldlotto)
GAMES = (" Cashpot "," Hot Pick "," Pick Three "," One Drop "," Four play ","Lucky Day Lotto")

# START ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__=="__main__":
    root = Tk() # Make window
    root.geometry("400x250")
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

    root.after(1000, lambda: messagebox.showinfo("Game Information",
        "This is a game made by me, DI.\nI do not own any rights to these \"game\" titles\nThis \"game\" was made purely for practice.\n\nEnjoy if you can!"))

    root.mainloop()
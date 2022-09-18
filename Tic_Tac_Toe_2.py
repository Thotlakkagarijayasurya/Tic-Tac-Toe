from tkinter import *
from tkinter import messagebox
import random
from time import *
global gui
x=0
b=[[0,0,0],[0,0,0],[0,0,0]]
gamedone=0
def check_winner(q):
    global b,x,btn0_0,btn0_1,btn0_2,btn1_0,btn1_1,btn1_2,btn2_0,btn2_1,btn2_2
    for i in range(3):
        if b[i][0]==b[i][1] and b[i][0]==b[i][2] and b[i][0]!=0:
            if i==0:
                cross(btn0_0)
                cross(btn0_1)
                cross(btn0_2)
            if(i==1):
                cross(btn1_0)
                cross(btn1_1)
                cross(btn1_2)
            if(i==2):
                cross(btn2_0)
                cross(btn2_1)
                cross(btn2_2)
            display_winner(b[i][0],q)
            return 1
        elif(b[0][i]==b[1][i] and b[0][i]==b[2][i] and b[0][i]!=0):
            if(i==0):
                cross(btn0_0)
                cross(btn1_0)
                cross(btn2_0)
            if(i==1):
                cross(btn0_1)
                cross(btn1_1)
                cross(btn2_1)
            if(i==2):
                cross(btn0_2)
                cross(btn1_2)
                cross(btn2_2)
            display_winner(b[0][i],q)
            return 1
    if(b[0][0]==b[1][1] and b[0][0]==b[2][2] and b[0][0]!=0):
        cross(btn0_0)
        cross(btn1_1)
        cross(btn2_2)
        display_winner(b[0][0],q)
        return 1
    elif(b[0][2]==b[1][1] and b[0][2]==b[2][0] and b[0][2]!=0):
        cross(btn0_2)
        cross(btn1_1)
        cross(btn2_0)
        display_winner(b[0][2],q)
        return 1
def cross(bt):
    bt['fg']="red"
def close():
    global gui,win
    gui.destroy()
    win.destroy()
def changeText(btn,u,v):
    m=0
    global b,x,gui,tie,label,gamedone
    if gamedone==0:
        if b[u][v]==0:
            x=x+1
            if(x%2==0):
                label=Label(gui,text="PLAYER-1(X):",fg="blue",bg="cyan",font=("Times New Roman",15))
                label.grid(row=3,column=0)
                btn['text'] = 'O'
                btn['font'] =("Times New Roman",10)
                b[u][v]=2
            else:
                label=Label(gui,text="PLAYER-2(O):",fg="blue",bg="cyan",font=("Times New Roman",15))
                label.grid(row=3,column=0)
                btn['text'] = 'X'
                btn['font'] =("Times New Roman",10)
                b[u][v]=1
            if(x>=5):
                m=check_winner(1)
            if(m!=1):
                if(x==9):
                    tie=Tk()
                    gamedone=1
                    tie.geometry("200x100")
                    tie.configure(bg="#00ffff")
                    tie.geometry("+670+420")
                    tie.overrideredirect(True)
                    t2=Label(tie,bg="cyan",fg="black",text="MATCH TIE")
                    l2=Button(tie,bg="cyan",fg="red",text="Replay",command=lambda: [tie.destroy(),gui.destroy(),Tic_Tac_Toe_2(1)])
                    quittt=Button(tie,text="Quit",command=lambda:[tie.destroy(),gui.destroy()],fg="red",bg="cyan")
                    t2.pack()
                    quittt.place(x=30,y=40)
                    l2.place(x=100,y=40)
                    tie.mainloop()
        else:
            messagebox.askquestion("invalid","incorrect choice\nTry again ")
def modee():
    mode=Tk()
    mode.configure(bg="cyan")
    mode.geometry("+500+200")
    ll=Label(mode,text="TIC TAC TOE",anchor="center",bg="cyan",fg="red",font=("times New Roman",55))
    l=Label(mode,text="SELECT MODE",anchor="center",bg="cyan",fg="orange",font=("times New Roman",35))
    b1=Radiobutton(mode,text="1.VS Computer",anchor="w",fg="blue",bg="cyan",font=("times New Roman",25),command=lambda:[mode.destroy(),Tic_Tac_Toe_2(2)])
    b2=Radiobutton(mode,text="2.VS Friend      ",fg="blue",bg="cyan",anchor="w",font=("times New Roman",25),command=lambda:[mode.destroy(),Tic_Tac_Toe_2(1)])
    ll.pack()
    l.pack()
    b1.pack()
    b2.pack()
    mode.mainloop()
def two_player():
    global gui,b,btn0_0,btn0_1,btn0_2,btn1_0,btn1_1,btn1_2,btn2_0,btn2_1,btn2_2
    label=Label(gui,text="PLAYER-1(X):",fg="blue",bg="cyan",font=("Times New Roman",15))
    label.grid(row=3,column=0)
    back=Button(gui,text="Go back",command=lambda:[gui.destroy(),modee()],fg="blue",bg="cyan",font=("Times New Roman",15))
    back.grid(row=2,column=0)
    quitt=Button(gui,text="Quit",command=gui.destroy,fg="blue",bg="cyan",font=("Times New Roman",15))
    quitt.grid(row=2,column=2)
    btn0_0= Button(gui,height=7,width=22,command=lambda:changeText(btn0_0,0,0),fg="blue",relief=SOLID)
    btn0_1= Button(gui,height=7,width=22, command=lambda:changeText(btn0_1,0,1),fg="blue",relief=SOLID)
    btn0_2= Button(gui, height=7,width=22,command=lambda:changeText(btn0_2,0,2),fg="blue",relief=SOLID)
    btn1_0= Button(gui,height=7,width=22, command=lambda:changeText(btn1_0,1,0),fg="blue",relief=SOLID)
    btn1_1= Button(gui, height=7,width=22,command=lambda:changeText(btn1_1,1,1),fg="blue",relief=SOLID)
    btn1_2= Button(gui,height=7,width=22, command=lambda:changeText(btn1_2,1,2),fg="blue",relief=SOLID)
    btn2_0= Button(gui, height=7,width=22,command=lambda:changeText(btn2_0,2,0),fg="blue",relief=SOLID)
    btn2_1= Button(gui,height=7,width=22, command=lambda:changeText(btn2_1,2,1),fg="blue",relief=SOLID)
    btn2_2= Button(gui, height=7,width=22, command=lambda:changeText(btn2_2,2,2),fg="blue",relief=SOLID)
    btn0_0.grid(row=4,column=0)
    btn0_1.grid(row=4,column=1)
    btn0_2.grid(row=4,column=2)
    btn1_0.grid(row=5,column=0)
    btn1_1.grid(row=5,column=1)
    btn1_2.grid(row=5,column=2)
    btn2_0.grid(row=6,column=0)
    btn2_1.grid(row=6,column=1)
    btn2_2.grid(row=6,column=2)
    gui.mainloop()
def display_winner(a,q):
    global gui,win,gamedone
    win=Tk()
    gamedone=1
    win.geometry("200x100")
    win.configure(bg="cyan")
    win.geometry("+650+420")
    win.overrideredirect(True)
    if(q==1):
        winner="winner:player "+str(a)
        l1=Label(win,font=("Times New Roman",20),text=winner,fg="red",bg="cyan")
        l1.grid(row=0,column=0)
    elif q==2:
        if a==1:
            l1=Label(win,font=("Times New Roman",20),text="YOU WON",fg="red",bg="cyan")
            l1.grid(row=0,column=0)
        elif a==2:
            l1=Label(win,font=("Times New Roman",20),text="YOU LOSE",fg="red",bg="cyan")
            l1.grid(row=0,column=0)
    bproceed=Button(win,text='Replay',command=lambda:[close(),Tic_Tac_Toe_2(q)],fg="red",bg="cyan")
    quitt=Button(win,text="Quit",command=close,fg="red",bg="cyan")
    quitt.place(x=30,y=40)
    bproceed.place(x=100,y=40)
    win.mainloop()   
def computer_turn():
    global b,gui
    x=com_choose(b)
    if(x==-1):
        k=computer_turnn(b)
        funn(k)
    else:
        funn(x)
    return
def funn(x):
    global gui,btn0_0,btn0_1,btn0_2,btn1_0,btn1_1,btn1_2,btn2_0,btn2_1,btn2_2
    if(x==1):
        btn0_0['text'] = 'O'
        btn0_0['font'] =("Times New Roman",10)
        b[0][0]=2
        return
    elif(x==2):
        btn0_1['text'] = 'O'
        btn0_1['font'] =("Times New Roman",10)
        b[0][1]=2
        return
    elif(x==3):
        btn0_2['text'] = 'O'
        btn0_2['font'] =("Times New Roman",10)
        b[0][2]=2
        return
    elif(x==4):
        btn1_0['text'] = 'O'
        btn1_0['font'] =("Times New Roman",10)
        b[1][0]=2
        return
    elif(x==5):
        btn1_1['text'] = 'O'
        btn1_1['font'] =("Times New Roman",10)
        b[1][1]=2
        return
    elif(x==6):
        btn1_2['text'] = 'O'
        btn1_2['font'] =("Times New Roman",10)
        b[1][2]=2
        return
    elif(x==7):
        btn2_0['text'] = 'O'
        btn2_0['font'] =("Times New Roman",10)
        b[2][0]=2
        return
    elif(x==8):
        btn2_1['text'] = 'O'
        btn2_1['font'] =("Times New Roman",10)
        b[2][1]=2
        return
    elif(x==9):
        btn2_2['text'] = 'O'
        btn2_2['font'] =("Times New Roman",10)
        b[2][2]=2
        return
def com_choose(b):
    for i in range(3):
        if(b[i][0]==b[i][1] and b[i][0]==2 and b[i][2]==0):
            return (i*3+3)
        elif(b[i][0]==b[i][2] and b[i][0]==2 and b[i][1]==0):
            return (i*3+2)
        elif(b[i][1]==b[i][2] and b[i][1]==2 and b[i][0]==0):
            return (i*3+1)
        elif(b[0][i]==b[1][i] and b[0][i]==2 and b[2][i]==0):
            return (i+7)
        elif(b[0][i]==b[2][i] and b[0][i]==2 and b[1][i]==0):
            return (4+i)
        elif(b[1][i]==b[2][i] and b[1][i]==2 and b[0][i]==0):
            return (i+1)
    if(b[0][0]==b[1][1] and b[0][0]==2 and b[2][2]==0):
        return 9
    elif(b[0][0]==b[2][2] and b[0][0]==2 and b[1][1]==0):
        return 5
    elif(b[1][1]==b[2][2] and b[1][1]==2 and b[0][0]==0):
        return 1
    elif(b[0][2]==b[1][1] and b[1][1]==2 and b[2][0]==0):
        return 7
    elif(b[0][2]==b[2][0] and b[2][0]==2 and b[1][1]==0):
        return 5
    elif(b[1][1]==b[2][0] and b[1][1]==2 and b[0][2]==0):
        return 3
    else:
        return -1
def computer_turnn(b):
    for i in range(3):
        if(b[i][0]==b[i][1] and b[i][0]!=0 and b[i][2]==0):
            return (i*3+3)
        elif(b[i][0]==b[i][2] and b[i][0]!=0 and b[i][1]==0):
            return (i*3+2)
        elif(b[i][1]==b[i][2] and b[i][1]!=0 and b[i][0]==0):
            return (i*3+1)
        elif(b[0][i]==b[1][i] and b[0][i]!=0 and b[2][i]==0):
            return (i+7)
        elif(b[0][i]==b[2][i] and b[0][i]!=0 and b[1][i]==0):
            return (4+i)
        elif(b[1][i]==b[2][i] and b[1][i]!=0 and b[0][i]==0):
            return (i+1)
    if(b[0][0]==b[1][1] and b[0][0]!=0 and b[2][2]==0):
        return 9
    elif(b[0][0]==b[2][2] and b[0][0]!=0 and b[1][1]==0):
        return 5
    elif(b[1][1]==b[2][2] and b[1][1]!=0 and b[0][0]==0):
        return 1
    elif(b[0][2]==b[1][1] and b[1][1]!=0 and b[2][0]==0):
        return 7
    elif(b[0][2]==b[2][0] and b[2][0]!=0 and b[1][1]==0):
        return 5
    elif(b[1][1]==b[2][0] and b[1][1]!=0 and b[0][2]==0):
        return 3
    else:
        randomm(b)

def randomm(b):
    t=[0,1,2]
    n=random.choice(t)
    s=random.choice(t)
    if(b[n][s]==0):
        b[n][s]=2
        funn(n*3+s+1)
        return
    else:
        randomm(b)
def changetext(btn,u,v):
    m=0
    global b,x,gui,tie,label,gamedone
    if gamedone==0:
        if(b[u][v]==0):
            if(x%2==0):
                label=Label(gui,text="      YOU:     ",fg="blue",bg="cyan",font=("Times New Roman",15))
                label.grid(row=3,column=0)
                btn['text'] = 'X'
                btn['font'] =("Times New Roman",10)
                b[u][v]=1
                x=x+1
                m=checking(btn,u,v,2)
            if(m!=1):
                computer_turn()
                x=x+1
                m=checking(btn,u,v,2)
        else:
            messagebox.askquestion("invalid","incorrect choice\nTry again ")
def checking(btn,u,v,q):
    m=0
    global b,x,gui,tie,label,gamedone
    if(x>=5):
        m=check_winner(q)
    if(m!=1):
        if(x==9):
            gamedone=1
            tie=Tk()
            tie.geometry("200x100")
            tie.configure(bg="cyan")
            tie.geometry("+670+420")
            tie.overrideredirect(True)
            t2=Label(tie,bg="cyan",fg="black",text="MATCH TIE",font=("Times New Roman",15))
            l2=Button(tie,bg="cyan",fg="red",text="Replay",command=lambda: [tie.destroy(),gui.destroy(),Tic_Tac_Toe_2(q)])
            quittt=Button(tie,text="Quit",command=lambda:[tie.destroy(),gui.destroy()],fg="red",bg="cyan")
            t2.pack()
            quittt.place(x=30,y=40)
            #Tic_Tac_Toe_2()
            l2.place(x=100,y=40)
            tie.mainloop()
            return 1
    else:
        return m
def computerplay():
    global gui,b,btn0_0,btn0_1,btn0_2,btn1_0,btn1_1,btn1_2,btn2_0,btn2_1,btn2_2,mode
    label=Label(gui,text="   YOU:",fg="blue",bg="cyan",font=("Times New Roman",15))
    label.grid(row=3,column=0)
    quitt=Button(gui,text="Quit",command=gui.destroy,fg="blue",bg="cyan",font=("Times New Roman",15))
    quitt.grid(row=2,column=2)
    back=Button(gui,text="Go back",command=lambda:[gui.destroy(),modee()],fg="blue",bg="cyan",font=("Times New Roman",15))
    back.grid(row=2,column=0)
    btn0_0= Button(gui,height=7,width=22,command=lambda:changetext(btn0_0,0,0),fg="blue",relief=SOLID)
    btn0_1= Button(gui,height=7,width=22, command=lambda:changetext(btn0_1,0,1),fg="blue",relief=SOLID)
    btn0_2= Button(gui, height=7,width=22,command=lambda:changetext(btn0_2,0,2),fg="blue",relief=SOLID)
    btn1_0= Button(gui,height=7,width=22, command=lambda:changetext(btn1_0,1,0),fg="blue",relief=SOLID)
    btn1_1= Button(gui, height=7,width=22,command=lambda:changetext(btn1_1,1,1),fg="blue",relief=SOLID)
    btn1_2= Button(gui,height=7,width=22, command=lambda:changetext(btn1_2,1,2),fg="blue",relief=SOLID)
    btn2_0= Button(gui, height=7,width=22,command=lambda:changetext(btn2_0,2,0),fg="blue",relief=SOLID)
    btn2_1= Button(gui,height=7,width=22, command=lambda:changetext(btn2_1,2,1),fg="blue",relief=SOLID)
    btn2_2= Button(gui, height=7,width=22, command=lambda:changetext(btn2_2,2,2),fg="blue",relief=SOLID)
    btn0_0.grid(row=4,column=0)
    btn0_1.grid(row=4,column=1)
    btn0_2.grid(row=4,column=2)
    btn1_0.grid(row=5,column=0)
    btn1_1.grid(row=5,column=1)
    btn1_2.grid(row=5,column=2)
    btn2_0.grid(row=6,column=0)
    btn2_1.grid(row=6,column=1)
    btn2_2.grid(row=6,column=2)
    gui.mainloop()
def Tic_Tac_Toe_2(k):
    global gui,gamedone
    gamedone=0
    gui = Tk()
    gui.configure(bg="#00ffff")
    gui.geometry("+500+200")
    global b,x
    x=0
    b=[[0,0,0],[0,0,0],[0,0,0]]
    label_name=Label(gui,text="TIC TAC TOE",bg="cyan",fg="red",font=("Times New Roman",20))
    label_name.grid(row=0,column=1)
    if(k==1):
        two_player()
    if(k==2):
        computerplay()
modee()

import tkinter
from tkinter import *




window = Tk()
window.title("Zombie Land Game")
# window.configure(background= "blue")
# window.geometry("512x512")

####################################################################
def start_game():
    g.destroy()
    lounge.pack_forget()
    b_lounge.pack_forget()
    start_window.pack()
    b_f.pack()


def menu_command():
    x=Tk()
    l = Label(x,text = "save seccussfully")
    b = Button(x, text = "ok", command= x.destroy)
    l.pack()
    b.pack()

    x.mainloop()

# Create Menu
my_menu = Menu(window)
window.config(menu=my_menu)

# Add Menu items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="save", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="exit", command=window.quit)

####################################################################


def new_game():
    start_window.pack_forget()
    b_f.pack_forget()
    room0.pack()
    b_room0.pack()


def room_0():
    m_alley.pack_forget()
    b_allay.pack_forget()
    room0.pack()
    b_room0.pack()

def option():
    o= Tk()
    o.title("Options")
    l = Label(o,text = "All setting are set",font = "12")
    b = Button(o, text = "back",font = "9", command= o.destroy)
    l.pack()
    b.pack()

def look_around():
    a= Tk()
    a.title("around")
    l_a = Label(a,text = "There is nothing useful",font = "12")
    b_a = Button(a, text = "back",font = "9", command= a.destroy)
    l_a.pack()
    b_a.pack()

def a_alley():
    room0.pack_forget()
    b_room0.pack_forget()

    room1.pack_forget()
    b_room1.pack_forget()

    room2.pack_forget()
    b_room2.pack_forget()

    m_alley.pack()
    b_allay.pack()


def room_1():
    m_alley.pack_forget()
    b_allay.pack_forget()

    room1.pack()
    b_room1.pack()

def room_2():
    m_alley.pack_forget()
    b_allay.pack_forget()

    room2.pack()
    b_room2.pack()

def the_lounge():
    m_alley.pack_forget()
    b_allay.pack_forget()

    lounge.pack()
    b_lounge.pack()

def game_over():
    global g
    g = Tk()
    g.title("around")
    l_g = Label(g,text = "Congratulation, you won the game\n", font = "12")
    l_g2 = Label(g, text = "Do you want to play again", font = "12")
    b_g2 = Button(g, text = "yes",font = "9", command =start_game)
    b_g = Button(g, text = "exit",font = "9", command= window.quit)
    l_g.pack()   
    l_g2.pack()

    b_g2.pack(side = LEFT,padx = 50)
    b_g.pack(side  = LEFT,padx = 30)



########################################################
#                                                      #
#                    start menu                        #
#                                                      #
#                    zombie land                       #
#                                                      #
#                                                      #
#                 button    button                     #
#                                                      #
#                      button                          #
#                      button                          #
#                                                      #
########################################################

# first = LabelFrame(window,text="1st", padx = 200, pady = 250, bg= "gray")




start_window = Frame(window, padx = 32, pady = 50, bg= "black")
labl = Label(start_window, text= "ZOMBIE LAND",font="Times 55", bg="black" , fg= "red")

labl.pack()

start_window.pack()


b_f = Frame(window,bg="black",width=570,height=500)
b_f.pack()
b_f.pack_propagate(0)
b_f.update()


fb1 = Button(b_f,text= "NEW GAME",font="Times 25",command = new_game)
fb2 = Button(b_f,text= "LOAD GAME",font="Times 25",command = room_0)
fb3 = Button(b_f,text= "OPTION",font="Times 25",padx=163,command = option)
fb4 = Button(b_f,text= "QUIT",font="Times 25",padx=185,command = window.quit)
fb1.place(x=50 ,y=10)
fb2.place(x=300 ,y=10)
fb3.place(x=50 ,y=120)
fb4.place(x=50 ,y=240)


########################################################
#                                                      #
#                    room 0                            #
#                                                      #
#                    this is room 0                    #
#                                                      #
#                                                      #
#                 button    button                     #
#                                                      #
#                                                      #
#                                                      #
#                                                      #
########################################################


room0 = Frame(window,bg="gray", padx = 145, pady = 50)
room0_labl = Label(room0, text= "ROOM 0",font="Times 55", bg="gray" , fg= "red")

room0_labl.pack()

# btn = Button(start_window, text= "start game").place(x=12, y=20)


# room0.pack()


b_room0 = Frame(window,bg="gray",width=570,height=500)
# b_room0.pack()
b_room0.pack_propagate(0)
b_room0.update()



room0_b1 = Button(b_room0,text= "LOOK AROUND",font="Times 25",padx=105,command = look_around)
room0_b2 = Button(b_room0,text= "EXIT",font="Times 25",padx=185,command = a_alley)

room0_b1.place(x=50 ,y=10)
room0_b2.place(x=50 ,y=120)




########################################################
#                                                      #
#                       alley                          #
#                                                      #
#              where do you want to go                 #
#                                                      #
#                                                      #
#                 button    button                     #
#                                                      #
#                 button    button                     #
#                                                      #
#                                                      #
########################################################


m_alley = Frame(window, padx = 32, pady = 50, bg= "black")
m_alley_labl = Label(m_alley, text= "WHERE TO GO",font="Times 55", bg="black" , fg= "red")

m_alley_labl.pack()



# m_alley.pack()


b_allay = Frame(window,bg="black",width=570,height=500)
# b_allay.pack()
b_allay.pack_propagate(0)
b_allay.update()


alley_b1 = Button(b_allay,text= "ROOM 0",font="Times 25",command = room_0)
alley_b2 = Button(b_allay,text= "ROOM 1",font="Times 25",command = room_1)
alley_b3 = Button(b_allay,text= "ROOM 2",font="Times 25",command = room_2)
alley_b4 = Button(b_allay,text= "LOUNGE",font="Times 25",command = the_lounge)
alley_b1.place(x=50 ,y=10)
alley_b2.place(x=300 ,y=10)
alley_b3.place(x=50 ,y=120)
alley_b4.place(x=300 ,y=120)




########################################################
#                                                      #
#                    room 1                            #
#                                                      #
#                    this is room 1                    #
#                                                      #
#                                                      #
#                 button    button                     #
#                                                      #
#                                                      #
#                                                      #
#                                                      #
########################################################


room1 = Frame(window,bg="gray", padx = 145, pady = 50)
room1_labl = Label(room1, text= "ROOM 1",font="Times 55", bg="gray" , fg= "red")

room1_labl.pack()



# room1.pack()


b_room1 = Frame(window,bg="gray",width=570,height=500)
# b_room1.pack()
b_room1.pack_propagate(0)
b_room1.update()



room1_b1 = Button(b_room1,text= "LOOK AROUND",font="Times 25",padx=105,command = look_around)
room1_b2 = Button(b_room1,text= "EXIT",font="Times 25",padx=185,command = a_alley)

room1_b1.place(x=50 ,y=10)
room1_b2.place(x=50 ,y=120)




########################################################
#                                                      #
#                    room 2                            #
#                                                      #
#                    this is room 2                    #
#                                                      #
#                                                      #
#                 button    button                     #
#                                                      #
#                                                      #
#                                                      #
#                                                      #
########################################################


room2 = Frame(window,bg="gray", padx = 145, pady = 50)
room2_labl = Label(room2, text= "ROOM 2",font="Times 55", bg="gray" , fg= "red")

room2_labl.pack()



# room2.pack()


b_room2 = Frame(window,bg="gray",width=570,height=500)
# b_room2.pack()
b_room2.pack_propagate(0)
b_room2.update()



room2_b1 = Button(b_room2,text= "LOOK AROUND",font="Times 25",padx=105,command = look_around)
room2_b2 = Button(b_room2,text= "EXIT",font="Times 25",padx=185,command = a_alley)

room2_b1.place(x=50 ,y=10)
room2_b2.place(x=50 ,y=120)




########################################################
#                                                      #
#                    the lounge                        #
#                                                      #
#                    this is the lounge                #
#                                                      #
#                                                      #
#                 button    button                     #
#                                                      #
#                                                      #
#                                                      #
#                                                      #
########################################################


lounge = Frame(window,bg="gray", padx = 145, pady = 50)
lounge_labl = Label(lounge, text= "LOUNGE",font="Times 50", bg="gray" , fg= "red")

lounge_labl.pack()



# lounge.pack()


b_lounge = Frame(window, bg="gray",width=570,height=500)
# b_lounge.pack()
lables = Label(b_lounge,text="there is zombie \nkill him to win",font="Times 40",bg="gray")
lables.pack()
b_lounge.pack_propagate(0)
b_lounge.update()



b_lounge_b1 = Button(b_lounge,text= "ATTACK",font="Times 25",padx=105,command = game_over)
b_lounge_b2 = Button(b_lounge,text= "EXIT",font="Times 25",padx=185,command = a_alley)

# b_lounge_b1.place(x=50 ,y=10)
b_lounge_b1.place(x=100 ,y=150)


############################################################################


window.mainloop()
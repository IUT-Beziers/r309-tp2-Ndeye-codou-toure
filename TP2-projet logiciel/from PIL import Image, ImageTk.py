''' from PIL import Image, ImageTk 
import  tkinter as Tk 
root = Tk.Tk() 

image = Image.open("me.png") 
photo = ImageTk.PhotoImage(image) 
 
canvas = Tk.Canvas(root, width = image.size[0], height = image.size[1]) 
canvas.create_image(0,0, anchor = Tk.NW, image=photo)
canvas.pack() 
root.mainloop() '''

''' import tkinter as Tk
 
def affi(i):
    photo=Tk.PhotoImage(file=i)
    labl.config(image=photo) # Ecrase labl.image donc pas besoin de faire un delete ou autre.
    labl.image=photo # Garder la référence
 
page=Tk.Tk()
labl = Tk.Label(page) # Il est aussi possible (et préférable) de mettre 1.gif dés le départ pour que le pack prenne compte de la géométrie.
labl.pack()    
Tk.Button(page,text="Etape 1",command=lambda: affi("me.png")).pack(side="left") # Pas besoin de nommer tes Widgets Button si tu
Tk.Button(page,text="Etape 2",command=lambda: affi("me.png")).pack(side="left") # N'en a pas besoin par la suite.
Tk.Button(page,text="Etape 3",command=lambda: affi("me.png")).pack(side="left")
page.mainloop() '''

''' from tkinter import*
from PIL import Image, ImageTk '''
  
''' def clesol():
  
    global photosol
    can3.delete(ALL)
    can3.create_image(72,77, image =photosol)
fen1=Tk()
global photosol
can3 = Canvas(fen1, width =512, height =130, bg='white')
can3.pack()
photosol = PhotoImage(file ='me.png')
CLESOL=Button(fen1,text='Clé de Sol',command=clesol)
CLESOL.pack()
  
fen1.mainloop()




def alert():
    global photo
    canvas.delete(ALL)
    canvas.create_image(0,0, image=photo)
    
    
fenetre = Tk()
global photo
canvas = Canvas(fenetre,width =640, height =640, bg ='ivory') 
canvas.pack() 
photo = PhotoImage(file='me.png') '''
''' 
fen = Tk()
can = Canvas(fen, width =640, height =640, bg ='ivory')
can.pack()
img = ImageTk.PhotoImage(file="me.png")
#rect=can.create_image(30, 30,image=img)
rect=can.create_rectangle(30, 30, 130, 130, fill="red", outline='')

old=[None, None]
def clic(event):
    old[0]=event.x
    old[1]=event.y
    
def glisser(event):
    
    a,b,c,d=can.coords(rect)
    if c< RIGHT or event.x<old[0]:
        can.move(rect, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y


can.bind("<B1-Motion>",glisser)
can.bind("<Button-1>",clic)


fen.mainloop() '''


''' from tkinter import *
import time
import PIL
from time import *
 
root = Tk()
img = PhotoImage(file='me.png')
canvas = Canvas(root,width=500, height=700, bg="white")
canvas.pack( side= RIGHT,padx=10,pady=10)
img_2 = img.subsample(1,1)
image=canvas.create_image(0,0,anchor=NW,image=img_2)
old=[None, None]

def clic(event):
    old[0]=event.x
    old[1]=event.y
def deplacement(event):
    img_coords = canvas.coords(image)
    img_width = img_2.width()
 
    if img_coords[0] + img_width <= 700:
        canvas.move(image, event.x-old[0],0)
    old[0]=event.x
    old[1]=event.y
canvas.bind("<B1-Motion>",deplacement)
canvas.bind("<Button-1>",clic)

 
 
root.mainloop() '''

''' #!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


class MyWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.create_menu_bar()

        # TODO: Fill the content of the window

        self.geometry("300x200")
        self.title("My First MenuBar V1.0")

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", underline=0, accelerator="CTRL+N", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Open...", underline=0, accelerator="CTRL+O", command=self.open_file)
        menu_file.add_command(label="Save", underline=0, accelerator="CTRL+S", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", underline=1, command=self.quit)
        menu_bar.add_cascade(label="File", underline=0, menu=menu_file)

        self.bind_all("<Control-n>", lambda x: self.do_something())
        self.bind_all("<Control-o>", lambda x: self.open_file())
        self.bind_all("<Control-s>", lambda x: self.do_something())

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Undo", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Copy", command=self.do_something)
        menu_edit.add_command(label="Cut", command=self.do_something)
        menu_edit.add_command(label="Paste", command=self.do_something)
        menu_bar.add_cascade(label="Edit", underline=0, menu=menu_edit)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About...", command=self.do_about)
        menu_bar.add_cascade(label="Help", underline=0, menu=menu_help)

        self.config(menu=menu_bar)

    def open_file(self):
        types = [("PNG image", ".png"), ("GIF image", ".gif"), ("All files", ".*")]
        file = askopenfilename(title="Choose the file to open", filetypes=types)
        print(file)

    def do_something(self):
        print("Menu clicked")

    def do_about(self):
        messagebox.showinfo("My title", "My message")


window = MyWindow()
window.mainloop()

 '''
 
 
 
''' from tkinter import *
from random import randrange
#import  tkinter as Tk

SIDE=400

root=Tk()
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("800x600")
w=600
h=400
x=w/2
y=h/2
my_canvas=Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=20)
img=PhotoImage(file="me.png")
def image():
    global img
    x1, y1= randrange(SIDE),randrange(SIDE)
    my_canvas.create_image(x1,y1,anchor=NW,image=img)
    def move(e):
        global img
        img=PhotoImage(file="me.png")
        my_canvas.create_image(e.x,e.y,image=img)
        my_label.config(text="Coordinates x:" + str(e.x) + "y" + str(e.y))
    my_canvas.bind('<B1-Motion>',move)
    def clic(event):
        x1=event.x
        y1=event.y
        t=my_canvas.find_closest(x1, y1)
        if t:
            my_canvas.delete(t[0])
    my_canvas.bind("<Button>",clic)

button_w = Button(root, text = 'img', command = lambda:image())
button_w.pack()
my_label = Label(root,text="")
my_label.pack(pady=20)
root.mainloop() '''

''' # script drag_and_drop.py
from PIL import Image, ImageTk
import tkinter as tk
 
 
def clic(event):
    """ Gestion de l'événement Clic gauche """
    global DETECTION_CLIC_SUR_OBJET
    global IMA
    IMA = 1
    nombre = 3
    # position du pointeur de la souris
    x = event.x
    y = event.y
    print("Position du clic -> ", x, y)
    # coordonnées de l'objet
    while IMA <= nombre:
        [x_min, y_min] = Canevas.coords(IMA)
        print("Position objet -> ", x_min, y_min)
        if x_min <= x <= x_min + LargeurI and y_min <= y < y_min + HauteurI:
            DETECTION_CLIC_SUR_OBJET = True
            print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET)
            break
        else:
            DETECTION_CLIC_SUR_OBJET = False
            print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET)
        IMA += 1
 
 
def drag(event):
    """ Gestion de l'événement bouton gauche enfoncé """
    # position du pointeur de la souris
    x = event.x + (LargeurI / 2)
    y = event.y + (HauteurI / 2)
    print("Position du pointeur -> ", x, y)
 
    if DETECTION_CLIC_SUR_OBJET:
        # limite de l'objet dans la zone graphique
        if x < LargeurI:
            x = LargeurI
        if x > Largeur:
            x = Largeur
        if y < HauteurI:
            y = HauteurI
        if y > Hauteur:
            y = Hauteur
        # mise à jour de la position de l'objet (drag)
        Canevas.coords(IMA, x - LargeurI, y - HauteurI)
 
 
IMA = 1
DETECTION_CLIC_SUR_OBJET = False
 
# Création de la fenêtre principale
root = tk.Tk()
root.title("Drag and drop")
# Image

image = Image.open("me.png")
resize_image = image.resize((100, 80))
photo = ImageTk.PhotoImage(resize_image)
# Création d'un widget Canvas
Largeur = 800
Hauteur = 600
HauteurI = image.size[1]
print("Taille de l'image en hauteur", HauteurI)
LargeurI = image.size[0]
print("Taille de l'image en Largeur", LargeurI)
Canevas = tk.Canvas(root, width=Largeur, height=Hauteur, bg='white')
# Création des objets graphiques environ une trentaine
ima1 = Canevas.create_image(0, 0, anchor=tk.NW, image=photo)

 
# La méthode bind() permet de lier un événement avec une fonction
Canevas.bind('<Button-1>', clic)  # événement clic gauche (press)
Canevas.bind('<B1-Motion>', drag)  # événement bouton gauche enfoncé (hold down)
 
Canevas.focus_set()
Canevas.pack(padx=10, pady=10)
root.mainloop() '''
''' 
import tkinter as tk
my_w = tk.Tk()
width,height=620,400 # set the variables 
c_width,c_height=width-10,height-65 # canvas width height
d=str(width)+"x"+str(height)
my_w.geometry(d) 
c1 = tk.Canvas(my_w, width=c_width, height=c_height,bg='lightgreen')
c1.grid(row=0,column=0,columnspan=3,padx=5,pady=5)


my_path = tk.PhotoImage(file = "me.png") # Update your image path
my_path2 = tk.PhotoImage(file = "switch12.png") # Update your image path
img_width,img_height=int(my_path.width()/2),int(my_path.height()/2)
img_width2,img_height2=int(my_path2.width()/2),int(my_path2.height()/2)
x1,y1=90,20 # Image position coordinate ( initial )
x2,y2=100,20
r1 = c1.create_image(x1,y1,  image=my_path)
r2 = c1.create_image(x2,y2,  image=my_path2)
x_new,y_new=0,0 # to store the Initial mouse click position
x_new2,y_new2=0,0

def my_callback(event):
    global x1,x2,y1,y2,x_new,y_new,x_new2,y_new2 # get the current coordinates of the image
    if(event.x<=x1+img_width and event.x>=x1-img_width and event.y<=y1+img_height and event.y>=y1-img_height):
    
        x1=event.x  # Set the new position as image x coordinate 
        y1=event.y  # Set the new position as image y coordinate
        step_x=event.x-x_new # Change in x value ( Horizontal)
        step_y=event.y-y_new # Change in y value ( vertical )
        x2=event.x  # Set the new position as image x coordinate 
        y2=event.y  # Set the new position as image y coordinate
        step_x2=event.x-x_new2 # Change in x value ( Horizontal)
        step_y2=event.y-y_new2 
        
        c1.move(r1,step_x,step_y) # Move image to new position 
        x_new,y_new=x1,y1
        c1.move(r2,step_x2,step_y2) # Move image to new position 
        x_new2,y_new2=x2,y2
     
def my_position(event):
    global x_new,y_new
    global x_new,y_new # collect the mouse left buttton press coordinates
    
my_w.bind('<B1-Motion>',my_callback) # Mouse left button pressed and move
my_w.bind('<Button-1>',my_position) # Mouse left button pressed

my_w.mainloop() '''


'''  
from tkinter import *
from PIL import Image, ImageTk
 
 
 
def clic(event):
    global DETECTION_CLIC_SUR_OBJET, DETECTION_CLIC_SUR_OBJET_2, \
            DETECTION_CLIC_SUR_OBJET_3, DETECTION_CLIC_SUR_OBJET_4, \
            DETECTION_CLIC_SUR_OBJET_5, DETECTION_CLIC_SUR_OBJET_6, oldpos
    DETECTION_CLIC_SUR_OBJET = False
    DETECTION_CLIC_SUR_OBJET_2 = False
    DETECTION_CLIC_SUR_OBJET_3 = False
    DETECTION_CLIC_SUR_OBJET_4 = False

    X = event.x
    Y = event.y
    left, top = can1.coords(IMAGE_1)
    left2, top2 = can1.coords(IMAGE_2)
    left3, top3 = can1.coords(IMAGE_3)
    left4, top4 = can1.coords(IMAGE_4)
 
    # on connait les dimensions de l'image
    left -= 64
    top -= 95
    left2 -= 61
    top2 -= 92
    left3 -= 120
    top3 -= 97
    left4 -= 100
    top4 -= 100
    
    right, bottom = left + 128, top + 190
    right2, bottom2 = left2 + 123, top2 + 184
    right3, bottom3 = left3 + 239, top3 + 194
    right4, bottom4 = left4 + 200, top4 + 200

  
    oldpos = X, Y
    if left <= X <= right and top <= Y <= bottom: 
        DETECTION_CLIC_SUR_OBJET = True
    elif left2 <= X <= right2 and top2 <= Y <= bottom2:
        DETECTION_CLIC_SUR_OBJET_2 = True
    elif left3 <= X <= right3 and top3 <= Y <= bottom3:
        DETECTION_CLIC_SUR_OBJET_3 = True
    elif left4 <= X <= right4 and top4 <= Y <= bottom4:
        DETECTION_CLIC_SUR_OBJET_4 = True
    else:
        oldpos = 0, 0
 
def drag(event):
    global oldpos
    X = event.x
    Y = event.y
    if DETECTION_CLIC_SUR_OBJET == True :
        if X < 0: 
            X = 0
        elif X > 1100: 
            X = 1100
        if Y < 0: 
            Y = 0
        if Y > 600: 
            Y = 600
        movex = X - oldpos[0]
        movey = Y - oldpos[1]
        can1.move(IMAGE_1, movex, movey)
        oldpos = X, Y
    elif DETECTION_CLIC_SUR_OBJET_2 == True :
        if X < 0: 
            X = 0
        elif X > 1100: 
            X = 1100
        if Y < 0: 
            Y = 0
        if Y > 600: 
            Y = 600
        movex = X - oldpos[0]
        movey = Y - oldpos[1]
        can1.move(IMAGE_2, movex, movey)
        oldpos = X, Y
    elif DETECTION_CLIC_SUR_OBJET_3 == True :
        if X < 0: 
            X = 0
        elif X > 1100: 
            X = 1100
        if Y < 0: 
            Y = 0
        if Y > 600: 
            Y = 600
        movex = X - oldpos[0]
        movey = Y - oldpos[1]
        can1.move(IMAGE_3, movex, movey)
        oldpos = X, Y
    elif DETECTION_CLIC_SUR_OBJET_4 == True :
        if X < 0: 
            X = 0
        elif X > 1100: 
            X = 1100
        if Y < 0: 
            Y = 0
        if Y > 600: 
            Y = 600
        movex = X - oldpos[0]
        movey = Y - oldpos[1]
        can1.move(IMAGE_4, movex, movey)
        oldpos = X, Y
 
DETECTION_CLIC_SUR_OBJET = False
DETECTION_CLIC_SUR_OBJET_2 = False
DETECTION_CLIC_SUR_OBJET_3 = False
DETECTION_CLIC_SUR_OBJET_4 = False

oldpos = 0, 0
fen1 = Tk()
image = Image.open("me.png")
image1 = Image.open("me.png")
image2 = Image.open("me.png")
image3 = Image.open("me.png")

photo = ImageTk.PhotoImage(image)
photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)
photo3 = ImageTk.PhotoImage(image3)

can1 = Canvas(fen1,bg='white',height=600,width=1100)
IMAGE_1 = can1.create_image(60,100,image=photo)
IMAGE_2 = can1.create_image(200,100,image=photo1)
IMAGE_3 = can1.create_image(360,100,image=photo2)
IMAGE_4 = can1.create_image(560,100,image=photo3)

 
can1.bind('<Button-1>',clic)
can1.bind('<B1-Motion>',drag)
can1.focus_set()
can1.pack(side=TOP)

bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
fen1.mainloop()
 '''







'''

def left(event):
    x=-10
    y=0
    my_canvas.move(my_image,x,y)
    
def right(event):
    x=10
    y=0
    my_canvas.move(my_image,x,y)
def up(event):
    x=0
    y=-10
    my_canvas.move(my_image,x,y)
def down(event):
    x=0
    y=10
    my_canvas.move(my_image,x,y)
    
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)'''

import tkinter as tk

# Constantes
LARGEUR = 480
HAUTEUR = 320

# Variables globales
old_x, old_y = 0, 0

def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    global old_x, old_y
    # position du pointeur de la souris
    old_x = event.x
    old_y = event.y

def drag(event):
    global old_x, old_y
    x = event.x
    y = event.y
    surface_dessin.create_line(old_x, old_y ,x, y, fill='green')

    old_x = event.x
    old_y = event.y

def effacer():
    """ Efface la zone graphique """
    surface_dessin.delete(tk.ALL)

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Cercle')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width = LARGEUR, height = HAUTEUR, bg = 'white')
surface_dessin.pack(padx =5, pady =5)

# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la surface provoquera l'appel de la fonction clic()
surface_dessin.bind('<Button-1>', clic)
surface_dessin.bind('<B1-Motion>', drag)
surface_dessin.pack(padx = 5, pady = 5)

# Création d'un widget Button (bouton effacer)
tk.Button(mon_app, text = 'Effacer', command = effacer).pack(side = tk.LEFT,padx = 5,pady = 5)
# Création d'un widget Button (bouton Quitter)
tk.Button(mon_app, text = 'Quitter', command = mon_app.destroy).pack()

mon_app.mainloop()
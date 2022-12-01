from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk 
from random import randrange


import sqlite3
from tkinter import messagebox
import os
import configparser
import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter
#import  tkinter as Tk

SIDE=400
w=900
h=400
x=w/2
y=h/2


fenetre = Tk()
fenetre.title("Vos architectures réseaux de façon simple et élégante")
menubar = Menu(fenetre)
canvas = Canvas(fenetre,width=w,height=h,bg="white")
canvas.focus_set()
canvas.pack(side=TOP) 
 # Variables globales
old_x, old_y = 0, 0

def clic_b(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    global old_x, old_y
    # position du pointeur de la souris
    old_x = event.x
    old_y = event.y

def drag_b(event):
    global old_x, old_y
    x = event.x
    y = event.y
    canvas.create_line(old_x, old_y ,x, y, fill='green')

    old_x = event.x
    old_y = event.y
# Création d'un widget Canvas (zone graphique)

canvas.bind_all('<KeyPress-n>', clic_b)
canvas.bind_all('<Control-n>', drag_b)
def effacer():
    """ Efface la zone graphique """
    canvas.delete(ALL)

def move(image, event):
    canvas.coords(image, event.x, event.y)

##########################Pour deplacer une image je fais je double clique sur la clic gauche et je deplace avec la souris######
def switch12():
    global photo
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image = canvas.create_image(x,y, image=photo,tags="icon")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):

        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=open_img)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
        
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda e:clic0)

    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    def openfn():
        filename = filedialog.askopenfilename(title='App - Selectionne une image')
        return filename
    def open_img():
        global img
        x = openfn()
        img = Image.open(x)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        Label(fenetre, image=img).grid (row = 4, column = 0)

 
       

    
        
#############################################################################################""   
def switch24():
    global photo1
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image = canvas.create_image(x,y, image=photo1)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):

        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
        
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)

    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
#######################################################################################""        
def routeur_f():
    global photo2
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image = canvas.create_image(x,y, image=photo2)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):

        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
        
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
################################################################################################    
def routeur():
    global photo3
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo3)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):

        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
        
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
############################################################################################################
def pc_p():
    global photo4
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo4)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
#############################################################################################################
def pc_f1():
    global photo5
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo5)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
#############################################################################################################
def pc_f2():
    global photo6
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo6)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
#############################################################################################################   
def telephone_f():
    global photo7
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo7)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
        
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
#############################################################################################################   
def telephone_s_f():
    global photo8
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo8)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
#############################################################################################################   
def iphone():
    global photo9
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo9)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
    
#############################################################################################################    
def android():
    global photo10
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo10)
    canvas.tag_bind(image, "<B1-Motion>", lambda e: move(image, e))
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e))
    
    def propriete(e):
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=switch12)
        propri.add_command(label="Supprimer", command= lambda: clic0(e))
        propri.add_command(label="Renommer", command=renommer)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<KeyPress-x>",lambda:clic0)
    def renommer():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveu nom:",bg ="Dark grey").place(x = 40, y = 60)
        src_dir = StringVar()
        Entry(top,textvariable = src_dir,width = 50).place(x = 40, y = 100)
        Button(top,text ="Modifier", command= top.destroy).place(x = 40, y = 160)
#####################################################################################################################
global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10
photo = PhotoImage(file='switch12_b.png')
photo1 = PhotoImage(file='switch24_b.png')
photo2 = PhotoImage(file='routeur_filaire_b.png')
photo3 = PhotoImage(file='routeur_b.png')
photo4 = PhotoImage(file='pc_portable_b.png')
photo5 = PhotoImage(file='pc_fixe_b.png')
photo6 = PhotoImage(file='pc_fixe2_b.png')
photo7 = PhotoImage(file='telephone_fixe_b.png')
photo8 = PhotoImage(file='telephone_s_fil_b.png')
photo9 = PhotoImage(file='iphone_b.png')
photo10 = PhotoImage(file='android_b.png')
############################################################ LABEL ########################""
my_label = Label(fenetre,text="")
my_label.pack(pady=20)
#################################### MENU #######################################
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Switch 12 ports",image=photo,compound=BOTTOM,accelerator="Touche 'S'", command=switch12)
menu1.add_separator()
#fenetre.iconphoto(False, PhotoImage(file='me.png'))
menu1.add_command(label="Switch 24 ports", image=photo1,compound=BOTTOM,accelerator="Touche 's'",command=switch24)
menubar.add_cascade(label="Switchs", menu=menu1)
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Routeur filaire",image=photo2,compound=BOTTOM,accelerator="Touche 'R'", command=routeur_f)
menu2.add_separator()
menu2.add_command(label="Routeur sans fil",image=photo3,compound=BOTTOM,accelerator="Touche 'r'", command=routeur)
menubar.add_cascade(label="Routeurs", menu=menu2)
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="PC Portable",image=photo4,compound=BOTTOM,accelerator="Touche 'P'", command=pc_p)
menu3.add_separator()
menu3.add_command(label="PC Fixe M1",image=photo5,compound=BOTTOM,accelerator="Touche '1'", command=pc_f1)
menu3.add_separator()
menu3.add_command(label="PC Fixe M2",image=photo6,compound=BOTTOM,accelerator="Touche '2'" ,command=pc_f2)
menu3.add_separator()
menu3.add_command(label="Telephone fixe",image=photo7,compound=BOTTOM,accelerator="Touche 'T'", command=telephone_f)
menu3.add_separator()
menu3.add_command(label="Telephone sans fil",image=photo8,compound=BOTTOM,accelerator="Touche 't'", command=telephone_s_f)
menu3.add_separator()
menu3.add_command(label="Android",image=photo10,compound=BOTTOM, accelerator="Touche 'A'",command=android)
menu3.add_separator()
menu3.add_command(label="Iphone",image=photo9,compound=BOTTOM, accelerator="Touche 'I'",command=iphone)
menu3.add_separator()
menubar.add_cascade(label="Clients", menu=menu3)
################################################################################################################
##############################   POUR MES RACCOURCIS   ##########################################
fenetre.bind_all("<KeyPress-S>", lambda x:switch12())
fenetre.bind_all("<KeyPress-s>", lambda x:switch24())
fenetre.bind_all("<KeyPress-R>", lambda x:routeur_f())
fenetre.bind_all("<KeyPress-r>", lambda x:routeur())
fenetre.bind_all("<KeyPress-P>", lambda x:pc_p())
fenetre.bind_all("<KeyPress-1>", lambda x:pc_f1())
fenetre.bind_all("<KeyPress-2>", lambda x:pc_f2())
fenetre.bind_all("<KeyPress-T>", lambda x:telephone_f())
fenetre.bind_all("<KeyPress-t>", lambda x:telephone_s_f())
fenetre.bind_all("<KeyPress-A>", lambda x:android())
fenetre.bind_all("<KeyPress-I>", lambda x:iphone())
###############################################################################################
b1 = Button(fenetre, text ='Quitter', command =fenetre.destroy)
b1.configure(bg='red')
b1.pack(side =BOTTOM)
# Création d'un widget Button (bouton effacer)
b2=Button(fenetre, text = 'Effacer', command = effacer)
b2.configure(bg='green')
b2.pack(side = BOTTOM)
fenetre.config(menu=menubar)

fenetre.mainloop()

from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk 
from random import randrange


#import  tkinter as Tk

SIDE=400
w=900
h=560
x=w/2
y=h/2
###########################################################################
############################ definition de la fenetre et du canvas#########
###########################################################################
fenetre = Tk()
fenetre.title("Logiciel d'équipements réseaux")
menubar = Menu(fenetre)
canvas = Canvas(fenetre,width=w,height=h,bg="white")
canvas.focus_set()
canvas.pack(side=TOP) 
#########################################################################################################
######################### Les 2 fonctions pour dessiner des cables gris ##################################
###########################################################################################################
 # Variables globales
old_x, old_y = 0, 0

def clic_b(event):
    """ Gestion de l'événement touche "n" sur la zone graphique """
    global old_x, old_y
    # position du pointeur de la souris
    old_x = event.x
    old_y = event.y

def drag_b(event):
    global old_x, old_y,ligne
    x = event.x
    y = event.y
    ligne=canvas.create_line(old_x, old_y,x, y, fill='gray',width=2)

    old_x = event.x
    old_y = event.y

canvas.bind_all('<KeyPress-n>', clic_b)
canvas.bind_all('<Control-n>', drag_b)
def effacer():
    """ Efface la zone graphique """
    canvas.delete(ligne)
#############################fonction pour effacer tout###############""
def effacertout():
    canvas.delete(ALL)
################################# Fonction pour deplacer tous les images ############################
def move(image, event):
    canvas.coords(image, event.x, event.y)
############# Fonction pour supprimer le nom de l'image ###################
def clear(text):
    canvas.delete(text)
##############################################################################################################################
########################## Ces différents fonctions séparées pas des # ont pour role chacune de créer ##############
#################################### une image, de le deplacer et de creer les propriétés de chaque image  ###################
##############################################################################################################################
##########################Pour deplacer une image je fais une clique gauche et je deplace avec la souris######
def switch12():
    global photo,img
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image = canvas.create_image(x,y, image=photo,tags="Switch12")
    text=canvas.create_text(x+2,y+20, text=canvas.gettags(image), tags="texte")
    #canvas.tag_bind(text, "<B1-Motion>", lambda e: movetext(text, e))
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+2,event.y+20)
        #my_label.config(text="Coordinates x:" + str(event.x) + "y" + str(event.y))
    
    def change():
        canvas.itemconfig("Switch12", image=img)
        
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind_all("<Button-2>",lambda event:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#############################################################################################""   
def switch24():
    global photo1,img1
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image = canvas.create_image(x,y, image=photo1,tags="Switch24")
    text=canvas.create_text(x+14,y+14, text=canvas.gettags(image), tags="texte")
    #canvas.tag_bind(text, "<B1-Motion>", lambda e: movetext(text, e))
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+14,event.y+14)
    
    def change():
        canvas.itemconfig("Switch24", image=img1)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#######################################################################################""        
def routeur_f():
    global photo2,img2
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image = canvas.create_image(x,y, image=photo2,tags="routeur_avec_fil")
    text=canvas.create_text(x+3,y+26, text=canvas.gettags(image), tags="texte")
    #canvas.tag_bind(text, "<B1-Motion>", lambda e: movetext(text, e))
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+26)
    
    def change():
        canvas.itemconfig("routeur_avec_fil", image=img2)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
################################################################################################    
def routeur():
    global photo3,img3
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo3,tags="routeur_sans_fil")
    text=canvas.create_text(x+3,y+50, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+50)
    
    def change():
        canvas.itemconfig("routeur_sans_fil", image=img3)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
############################################################################################################
def pc_p():
    global photo4,img4
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo4,tags="pc_portable")
    text=canvas.create_text(x+3,y+50, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e,text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+50)
    
    def change():
        canvas.itemconfig("pc_portable", image=img4)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer",command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#############################################################################################################
def pc_f1():
    global photo5,img5
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo5,tags="ordinateur_fixe1")
    text=canvas.create_text(x+3,y+50, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+50)
    
    def change():
        canvas.itemconfig("ordinateur_fixe1", image=img5)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#############################################################################################################
def pc_f2():
    global photo6,img6
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo6,tags="ordinateur_fixe2")
    text=canvas.create_text(x+3,y+50, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+50)
    
    def change():
        canvas.itemconfig("ordinateur_fixe2", image=img6)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer",command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#############################################################################################################   
def telephone_f():
    global photo7,img7
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo7,tags="telephone_fixe")
    text=canvas.create_text(x+3,y+50, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+50)
    
    def change():
        canvas.itemconfig("telephone_fixe", image=img7)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer",command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#############################################################################################################   
def telephone_s_f():
    global photo8,img8
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo8,tags="telephone_sans_fil")
    text=canvas.create_text(x+3,y+50, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+50)
    
    def change():
        canvas.itemconfig("telephone_sans_fil", image=img8)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#############################################################################################################   
def iphone():
    global photo9,img9
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo9,tags="iphone")
    text=canvas.create_text(x+3,y+50, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+50)
    
    def change():
        canvas.itemconfig("iphone", image=img9)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#############################################################################################################    
def android():
    global photo10,img10
    #canvas.delete(ALL)
    x, y= randrange(SIDE),randrange(SIDE)
    image=canvas.create_image(x,y, image=photo10,tags="android")
    text=canvas.create_text(x+3,y+60, text=canvas.gettags(image), tags="texte")
    canvas.tag_bind(image, "<B1-Motion>", lambda e: [move(image, e), movetext(text, e)])
    canvas.tag_bind(image,"<Button-3>", lambda e: propriete(e, text))

    def movetext(text, event):
        canvas.coords(text, event.x+3,event.y+60)
    
    def change():
        canvas.itemconfig("android", image=img10)
    def propriete(e, text):
        global propri
        propri = Menu(menubar, tearoff=0)
        propri.add_command(label="Changer l'icone", command=change)
        propri.add_command(label="Supprimer", command= lambda : [clic0(e), clear(text)])
        propri.add_command(label="Renommer", command=create)
        propri.post(e.x_root, e.y_root)
    
    def clic0(event):
        global x1,y1
        x1=event.x
        y1=event.y
        t=canvas.find_closest(x1, y1)
        if t:
            canvas.delete(t[0])
    canvas.bind("<Button-2>",lambda e:clic0)
    
    monvar = StringVar()
    def create():
        top = Toplevel()
        Label_w = Label(top, text = "Entrer le nouveau nom:",bg ="Dark grey").place(x = 40, y = 60)
        entry = Entry(top,textvariable = monvar,width = 50).place(x = 40, y = 100)
        def close_btn():
            var = monvar.get()
            if var:
                canvas.itemconfig(text, text=var)
            top.destroy()
            top.update()
        Button(top,text ="Modifier", command=close_btn).place(x = 40, y = 160)
#####################################################################################################################
global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10,img,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10
photo = PhotoImage(file='switch12_b.png')
img = PhotoImage(file='s12.png')

photo1 = PhotoImage(file='switch24_b.png')
img1 = PhotoImage(file='s24.png')

photo2 = PhotoImage(file='routeur_filaire_b.png')
img2 = PhotoImage(file='router.png')

photo3 = PhotoImage(file='routeur_b.png')
img3 = PhotoImage(file='routeurr .png')

photo4 = PhotoImage(file='pc_portable_b.png')
img4 = PhotoImage(file='PC.png')

photo5 = PhotoImage(file='pc_fixe_b.png')
img5 = PhotoImage(file='pc_fixe2_b.png')

photo6 = PhotoImage(file='pc_fixe2_b.png')
img6 = PhotoImage(file='pc_fixe_b.png')

photo7 = PhotoImage(file='telephone_fixe_b.png')
img7 = PhotoImage(file='telephone_fixe.png')

photo8 = PhotoImage(file='telephone_s_fil_b.png')
img8 = PhotoImage(file='tel.png')

photo9 = PhotoImage(file='iphone_b.png')
img9 = PhotoImage(file='iphone.png')

photo10 = PhotoImage(file='android_b.png')
img10 = PhotoImage(file='Android.png')
############################################################ LABEL ########################""
my_label = Label(fenetre,text="")
my_label.pack(pady=20)
#################################### MENU #######################################
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Switch 12 ports",image=photo,compound=BOTTOM,accelerator="ALT +'S'", command=switch12)
menu1.add_separator()
#fenetre.iconphoto(False, PhotoImage(file='me.png'))
menu1.add_command(label="Switch 24 ports", image=photo1,compound=BOTTOM,accelerator="ALT +'s'",command=switch24)
menubar.add_cascade(label="Switchs", menu=menu1)
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Routeur filaire",image=photo2,compound=BOTTOM,accelerator="ALT +'R'", command=routeur_f)
menu2.add_separator()
menu2.add_command(label="Routeur sans fil",image=photo3,compound=BOTTOM,accelerator="ALT +'r'", command=routeur)
menubar.add_cascade(label="Routeurs", menu=menu2)
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="PC Portable",image=photo4,compound=BOTTOM,accelerator="ALT +'P'", command=pc_p)
menu3.add_separator()
menu3.add_command(label="PC Fixe M1",image=photo5,compound=BOTTOM,accelerator="Touche '1'", command=pc_f1)
menu3.add_separator()
menu3.add_command(label="PC Fixe M2",image=photo6,compound=BOTTOM,accelerator="Touche '2'" ,command=pc_f2)
menu3.add_separator()
menu3.add_command(label="Telephone fixe",image=photo7,compound=BOTTOM,accelerator="ALT +'T'", command=telephone_f)
menu3.add_separator()
menu3.add_command(label="Telephone sans fil",image=photo8,compound=BOTTOM,accelerator="ALT +'t'", command=telephone_s_f)
menu3.add_separator()
menu3.add_command(label="Android",image=photo10,compound=BOTTOM, accelerator="ALT +'A'",command=android)
menu3.add_separator()
menu3.add_command(label="Iphone",image=photo9,compound=BOTTOM, accelerator="ALT +'I'",command=iphone)
menu3.add_separator()
menubar.add_cascade(label="Clients", menu=menu3)
################################################################################################################
##############################   POUR MES RACCOURCIS   ##########################################
def raccourci():
    fenetre.bind_all("<Alt-S>", lambda x:switch12())
    fenetre.bind_all("<Alt-s>", lambda x:switch24())
    fenetre.bind_all("<Alt-R>", lambda x:routeur_f())
    fenetre.bind_all("<Alt-r>", lambda x:routeur())
    fenetre.bind_all("<Alt-P>", lambda x:pc_p())
    fenetre.bind_all("<KeyPress-1>", lambda x:pc_f1())
    fenetre.bind_all("<KeyPress-2>", lambda x:pc_f2())
    fenetre.bind_all("<Alt-T>", lambda x:telephone_f())
    fenetre.bind_all("<Alt-t>", lambda x:telephone_s_f())
    fenetre.bind_all("<Alt-A>", lambda x:android())
    fenetre.bind_all("<Alt-I>", lambda x:iphone())
raccourci()
###############################################################################################
b1 = Button(fenetre, text ='Quitter', command =fenetre.destroy)
b1.configure(bg='red')
b1.pack(side =BOTTOM)
# Création d'un widget Button (bouton effacer)
b2=Button(fenetre, text = 'Supprimer la derniére ligne', command = effacer)
b2.configure(bg='green')
b2.pack(side = LEFT)
b3=Button(fenetre, text = 'Effacer Tout', command = effacertout)
b3.configure(bg='blue')
b3.pack(side = RIGHT)
''' def changeState():
    if (btn1['state'] == NORMAL): btn1['state'] = DISABLED
    else:
        btn1['state'] = NORMAL
def changeState_raccourci():
    if (Toplevel['state'] == NORMAL): raccourci['state'] = DISABLED
    else:
        raccourci['state'] = NORMAL
btn1=Button(fenetre, text = 'Raccourcis', state = DISABLED, command = raccourci)
btn1.pack(side = RIGHT, padx=40, pady=0)
btn2 = Button(fenetre, text="Activer/Désactiver Raccourci", command=changeState)
btn2.pack(side = RIGHT) '''
fenetre.config(menu=menubar)

fenetre.mainloop()
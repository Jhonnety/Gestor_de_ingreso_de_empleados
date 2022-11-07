from ast import Num
from distutils.cmd import Command
from tkinter import*
from PIL import ImageTk, Image
import getpass
import csv
raiz=Tk()

#raiz primaria
raiz.title("Lector de tarjetas")
raiz.resizable(1,1)
raiz.iconbitmap("Partner.ico")
raiz.geometry("820x800")
raiz.config(background="#9ae8ad")
raiz.config(relief="sunken")
raiz.config(bd=10)
raiz.state("zoomed")



menubar = Menu(raiz)
raiz.config(menu=menubar)
registrosmenu = Menu(menubar)

menubar.add_cascade(label="Registros", menu=registrosmenu)

registrosmenu = Menu(menubar, tearoff=0)
registrosmenu.add_command(label="Abrir")
################################################


#primer frame 
primerframe=Frame()
primerframe.pack()


primerframe.config(background="white")
primerframe.config(width=1700, height=1000)
primerframe.config(relief="flat")
primerframe.config(bd=20)

#################################################

#segundo frame
segundoframe=Frame()
segundoframe.place(x=625,y=300)

segundoframe.config(background="#82f97c")
segundoframe.config(width=717, height=300)
segundoframe.config(relief="sunken")
segundoframe.config(bd=12)

###############################################
#tercer frame
tercerframe=Frame()
tercerframe.place(x=560,y=620)

tercerframe.config(background="#9ae8ad")
tercerframe.config(width=850, height=300)
tercerframe.config(relief="sunken")
tercerframe.config(bd=12)







#################################################
#labels

label1 = Label(primerframe, text="LECTOR DE TARJETAS \n PARTNER CHAT",background="#9ae8ad",bd=(15),font=("Arial",50),fg="black",relief="raised").place(x=470 , y=80)

label2 = Label(segundoframe, text="Pase su tarjeta por favor",background="#82f97c",font=("Arial",25),fg="black").place(x=164, y=40)

label3 = Label(tercerframe, text="Nombre:     ",fg="black",background="#9ae8ad",font=("Arial",18)).place(x=100,y=80)
label4 = Label(tercerframe, text="Hora de ingreso:     ",fg="black",background="#9ae8ad",font=("Arial",18)).place(x=100,y=120)
label5 = Label(tercerframe, text="Hora de salida:     ",fg="black",background="#9ae8ad",font=("Arial",18)).place(x=100,y=160)
label6 = Label(tercerframe, text="INFORMACION DE INGRESO",fg="black",background="#9ae8ad",font=("Arial",19)).place(x=240,y=20)


#Logo partner chat

imagen=ImageTk.PhotoImage(Image.open("PARTNER CHAT.gif").resize((250,250)))

ImagenPartner= Label(primerframe,image=imagen,bd=0,background="white").place(x=100, y=40)

#################################################
#txtbox's

num=IntVar()
TxtBox1= Entry(segundoframe,font=(29),width=34,show="*",justify="center",textvariable=num,bd=(4)).place(x=180,y=130)
TxtBox1= tagId = getpass.getpass
if(tagId != "horas"):
   RFidRegistered = False
   with open(r'Usuarios.csv') as csvfile:
      Dataset = csv.DictReader(csvfile)
      for idx in Dataset:
         if str(idx["RFid"]) == tagId:
            RFidRegistered = True
            print("Hola de nuevo, " + idx["Nombres"])
      if RFidRegistered == False:
        print("No se ha encontrado el usuario")     


raiz.mainloop()
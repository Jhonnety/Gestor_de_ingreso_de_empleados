#Ejemplo Introductorio para el cargue y visualización de datos .CSV

from msilib import text
from tkinter import*
from datetime import date
import datetime
import time
from turtle import left
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import getpass
import csv
import os
from email.message import EmailMessage
import smtplib
import ssl

              

raiz=Tk()
#raiz primaria
raiz.title("Lector de tarjetas")
raiz.resizable(1,1)
raiz.iconbitmap("Partner.ico")
raiz.geometry("1800x900+500+50")
raiz.config(background="#9ae8ad")
raiz.config(relief="sunken")
raiz.config(bd=10)
raiz.state("zoomed")



################################################


#primer frame 
primerframe=Frame()
primerframe.pack()


primerframe.config(background="white")
primerframe.config(width=1700, height=1000)
primerframe.config(relief="flat")
primerframe.config(bd=20)

def Horas():
      titulo.set("Informacion de horas")
      usuarioOn=False
      mensaje2 = StringVar()
      with open(r'Usuarios.csv') as csvfile:
         Dataset = csv.DictReader(csvfile)
         for idx in Dataset:
            if str(idx["RFid"]) == tagId.get():
               usuarioOn=True
            
               
               fechaH=tagId2.get()
               #str(input('Ingrese la fecha del cual quiere ver el total \nde horas trabajadas en formato (yyyy-mm-dd): '))


               
               totalMinutos = 0
               totalHoras = 0
               fechaEncontrada = False
               with open(r'Registros.csv') as csvfile2:
                  DataRegistros = csv.DictReader(csvfile2)
                  for fecha in DataRegistros:
                     if (str(fecha["RFid"]) == str(idx["RFid"])) & (str(fecha["Fecha"]) == fechaH):
                        fechaEncontrada = True
                        
                        horas = str(fecha["Tiempo"])
                        if(len(horas) == 7):          #11:02:00
                           totalMinutos = totalMinutos + int(horas[2:4])
                           totalHoras = totalHoras + int(horas[0:1])
                        if(len(horas) == 8):
                           totalMinutos = totalMinutos+ int(horas[3:5])
                           totalHoras = totalHoras + int(horas[0:2])
                  
                  if(fechaEncontrada == False):
                     mensaje2 = "Fecha no encontrada"
                  else:
                     mensaje2=str(idx["Nombres"]) +" el " + str(fechaH) + " trabajaste: " + str(totalHoras) + " hora/s y " + str(totalMinutos) + " minuto/s"
                     
                     

                     email_emisor='partnerchat22@gmail.com'
                     email_contraseña = 'jvcqamclcqmuijeq'

                     email_receptor = str(idx["Correo"])

                     asunto = 'Horas trabajadas'
                     cuerpo = """
                     Buen dia, cordial saludo 
                     Señor@ """ +" "+ str(idx["Nombres"]) + " "+"se le informa que el dia" +" "+ str(fechaH)+" "+"trabajo un total de " +" "+ str(totalHoras) + " "+ "hora/s" + " "+ "con"+ " "+ str(totalMinutos) + " "+"minutos"
                     

                  
                     en = EmailMessage()
                     en['From'] = email_emisor
                     en['To'] = email_receptor
                     en['subject'] = asunto
                     en.set_content (cuerpo) 

                     contexto = ssl.create_default_context()

                     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= contexto) as smtp:
                        smtp.login(email_emisor, email_contraseña)
                        smtp.sendmail(email_emisor,email_receptor, en.as_string())

                           #Balcero
                           #nombre el usuario  str(idx["Nombres"])
                           #fecha trabajada str(fechaH)
                           #horas  str(totalHoras)
                           #Minutos str(totalMinutos)
                           #Correo de la persona str(idx["Correo"]


         if(usuarioOn==False):
            mensaje2 = "No se ha encontrado el usuario"
      inf.set(mensaje2)#xd


def Clícame():
   titulo.set("Informacion de ingreso")
   if(tagId.get() != "horas"):
      mensaje = StringVar()
      RFidRegistered = False
      with open(r'Usuarios.csv') as csvfile:
         Dataset = csv.DictReader(csvfile)
         for idx in Dataset:
            if str(idx["RFid"]) == tagId.get():
               RFidRegistered = True
               mensaje = "Hola de nuevo, " + idx["Nombres"]
               #print("Hola de nuevo, " + idx["Nombres"])
               idPrueba = 1
               Rf = ''
               Nombres=''
               fechaB = ''
               
               with open(r'Registros.csv') as csvfile2:
                     DataRegistros = csv.DictReader(csvfile2)
                     tipo = 'Salida'
                     for fecha in DataRegistros:
                        idPrueba = idPrueba + 1
                        if (str(fecha["RFid"]) == str(idx["RFid"])) & (str(fecha["Fecha"]) == str(date.today())):
                           tipo= str(fecha["Tipo"])
                           fechaB = str(fecha["Fecha"]) +" "+ str(fecha["Hora"])

                     if tipo  == 'Entrada': #ultimo
                        mensaje = mensaje + "\n" + "Salida - Dia : " + str(date.today()) + " Hora: " + time.strftime("%H:%M")
                        #print("Salida - Dia : " + str(date.today()) + " Hora: " + time.strftime("%H:%M"))
                        fechaA = str(date.today()) + " " + str(time.strftime("%H:%M"))
                        fecha1 = datetime.strptime(fechaB, '%Y-%m-%d %H:%M')
                        fecha2 = datetime.strptime(fechaA, '%Y-%m-%d %H:%M')
                        res = fecha2 - fecha1
                        datos = [(idPrueba+1),idx["RFid"],idx["Nombres"],str(date.today()),str(time.strftime("%H:%M")), "Salida",str(res)]
                        with open(r'Registros.csv', 'a') as f:
                              writer = csv.writer(f)
                              writer.writerow(datos)
                     else:
                        mensaje = mensaje + "\n" + "Entrada - Dia :"+ str(date.today()) + " Hora: "  + time.strftime("%H:%M")
                        print("Entrada - Dia :"+ str(date.today()) + " Hora: "  + time.strftime("%H:%M"))
                        datos = [(idPrueba+1),idx["RFid"],idx["Nombres"],str(date.today()),time.strftime("%H:%M"), "Entrada","0"]
                        with open(r'Registros.csv', 'a') as f:
                                 writer = csv.writer(f)
                                 writer.writerow(datos)
         if RFidRegistered == False: 
            mensaje = "No se ha encontrado el usuario" 
      inf.set(mensaje)


#################################################

#segundo frame


###############################################
#tercer frame

tagId = StringVar()

tagId2 = StringVar()
inf = StringVar()
titulo = StringVar()


#################################################
#labels

label1 = Label(primerframe, text="LECTOR DE TARJETAS \n PARTNER CHAT",background="#9ae8ad",bd=(15),font=("Arial",50),fg="black",relief="raised").place(x=470 , y=60)

label2 = Label(primerframe, text="Pase su tarjeta por favor",background="#82f97c",font=("Arial",25),fg="black").place(x=700, y=250)

label3 = Label(primerframe, text="",fg="black",background="#9ae8ad",font=("Arial",18), textvariable=inf).place(x=200,y=530,height=100,width=1000)


label7 = Label(primerframe, text="INFORMACION DE INGRESO",fg="black",background="#9ae8ad",font=("Arial",19), textvariable=titulo).place(x=200,y=450,height=100,width=1000)


#Logo partner chat

imagen=ImageTk.PhotoImage(Image.open("PARTNER CHAT.gif").resize((250,250)))
ImagenPartner= Label(primerframe,image=imagen,bd=0,background="white").place(x=100, y=40)

#################################################
#txtbox's

Button(primerframe, text="Ingresar",font=("Arial",10), command=Clícame).place(x=790,y=360)
Button(primerframe, text="Horas trabajas",font=("arial",10), command=Horas).place(x=880,y=360)
TxtBox1= Entry(primerframe,font=(29),width=20,show="*",justify="center",bd=(4), textvariable=tagId).place(x=790,y=300)
TxtBox2= Entry(primerframe,font=(29),fg="black",width=20,justify="center",bd=(4), textvariable=tagId2).place(x=790,y=330)
  

raiz.mainloop()


#Cargando datos del dataset
dataset = pd.read_csv(r'Usuarios.csv',encoding="latin9", sep=",")
dataRegistros = pd.read_csv(r'Registros.csv',encoding="latin9", sep=",")

#resumen de los datos
dataset.head()
dataRegistros.head()
#Algoritmo para lectura y búsqueda de usuarios
import getpass
import csv

#Menu
print("--Ingrese 'horas' si quiere conocer el numero de horas trabajadas en determinado dia--")
print("-----------------------------Bienvenido-------------------------------")
#desicion = str(input(print("Ingresa 1 para ingresar con carnet o 2 para buscar horas trabajadas un dia determinado")))
#tagId=str(input('Acerque su carnet al lector: '))



#tagId='0008712312'


   
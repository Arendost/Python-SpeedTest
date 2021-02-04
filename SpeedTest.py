import threading
import tkinter as tk
from tkinter import ttk
import speedtest
from tkinter import *
from tkinter import messagebox


h=1

root = tk.Tk()
#root.iconbitmap("Rayo.ico")

###################################### funciones ###################################################
def Informacion():
    messagebox.showinfo("Informacion","Medidor de volcidad de carga y descarga de internet,")

def Contribucion():
    messagebox.showinfo("Contribucion","programa realizado con la ayuda de Juan el de Conatel")

def infoadicional():
    messagebox.showinfo("Aceca de","Redes: todos estan en mis redes")

def avisolicencia():
    messagebox.showwarning("licencia","producto bajo licencia GNU")  

def saliraplicacion():
    #valor=messagebox.askquestion("salr","deseas salir de la aplicacion") 
    valor=messagebox.askokcancel("salr","deseas salir de la aplicacion") 
    
    if valor==TRUE:    #yes
        root.destroy()

def cerrardocumento():
    valor=messagebox.askretrycancel("reintentar","deseas salir de la aplicacion") 
    if valor==FALSE:
        root.destroy()

def download_file_worker():
    try:
        test_speed = speedtest.Speedtest()
        test_speed.get_best_server()
        ping = test_speed.results.ping
        download = test_speed.download()
        upload = test_speed.upload()
        m_download = convert_to_Mbps(download)
        m_upload = convert_to_Mbps(upload)
        Label(frame,text=str(ping) + "ms",fg="black",font=("Arial", 10),bg="white" ).place(x=10,y=100)
        Label(frame,text=str(m_download) + "Mb/s",fg="black",font=("Arial", 10),bg="white" ).place(x=110,y=100)
        Label(frame,text=str(m_upload) + "Mb/s",fg="black",font=("Arial", 10),bg="white" ).place(x=200,y=100)

    except speedtest.ConfigRetrievalError :
        global h
        h=0
        etq.config(text="Revisa tu conexion y vuelve a iniciar") 

def convert_to_Mbps(bits):

    return round(bits/10**6, 2)

def convert_to_Kbps(bits):
    return round(bits/10**3, 2)       

def schedule_check(t):
        root.after(1000, check_if_done, t)

def check_if_done(t):
    global h    
    if not t.is_alive():
        if  h==1:
            etq.config(text="test realizado con exito")
            h=1
            btn["state"] = "normal"    
    else:
        schedule_check(t)

def download_file():
        etq.config(text="Espere mientras se realiza el test")
        btn["state"] = "disabled"
        t = threading.Thread(target=download_file_worker)
        t.start()
        schedule_check(t)

######################################## Settings ########################################################

barraMenu=Menu(root)
root.config(bg="#03A9F4",menu=barraMenu,width=300,height=300)
root.title("Speed Test")
root.resizable(0,0)
root.geometry("300x300")

Label(root,text="Speed Test",fg="white",font=("Arial", 20),bg="#03A9F4" ).place(x=80,y=25)


frame=Frame(root)
frame.config(bg="white",width=300,height=200)
frame.pack(side="bottom",anchor="s")

Label(frame,text="Ping",fg="black",font=("Arial", 12),bg="white" ).place(x=20,y=30)
Label(frame,text="Down Speed",fg="black",font=("Arial", 12),bg="white" ).place(x=90,y=30)
Label(frame,text="Up Speed",fg="black",font=("Arial", 12),bg="white" ).place(x=210,y=30)
 
################################### Botton  ##############################################################

btn = Button(frame,text="Test", command=download_file,padx="100")
btn.place(x=30,y=140)

etq= Label(frame,text="Preciona el botton para iniciar el test",fg="black",font=("Arial", 10),bg="white" )
etq.place(x=40,y=170)

################################ Menu Superior ################################################################

AAyuda=Menu(barraMenu)
AAyuda=Menu(barraMenu,tearoff=0)

AAyuda.add_command(label="Informacion",command=Informacion)
AAyuda.add_command(label="Contribucion",command=Contribucion)
AAyuda.add_command(label="acerca de",command=infoadicional)

barraMenu.add_cascade(label="ayuda",menu=AAyuda)

####################################################################

root.mainloop()

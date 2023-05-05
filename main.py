from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql

#functionality part

def add_Voitures():
    def add_data():
        if idEntry.get()=='' or marqueEntry.get()=='' or transmissionEntry.get()=='' or placesEntry.get()=='' or prixEntry.get()=='' or carburantEntry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=add_window)
        else:
            currentdate = time.strftime('%d/%m/%Y')
            currenttime = time.strftime('%H:%H:%S')
            query='INSERT INTO Voitures VALUES(%d,%s,%s,%d,%s,%s)'
            mycursor.execute(query,(idEntry.get(),marqueEntry.get(),carburantEntry.get()
                                    ,placesEntry.get(),transmissionEntry.get()
                                    ,prixEntry.get(),currentdate,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data addded successfully. Do you want to clean the form? ',parent=add_window)
            print(result)
            if result:
                idEntry.delete(0,END)
                marqueEntry.delete(0, END)
                transmissionEntry.delete(0, END)
                placesEntry.delete(0, END)
                carburantEntry.delete(0, END)
                prixEntry.delete(0, END)
            else:
                pass

            query='select *from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            for data in fetched_data:
                datalist=list(data)
                studentTable.insert('',END,values=datalist)

    add_window = Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)


    idLabel=Label(add_window,text='id',font=('SF Pro',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=w)
    idEntry=Entry(add_window,font=('SF Pro',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    marqueLabel = Label(add_window, text='marque', font=('SF Pro', 20, 'bold'))
    marqueLabel.grid(row=1, column=0, padx=30, pady=15,sticky=w)
    marqueEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    marqueEntry.grid(row=1, column=1, pady=15, padx=10)

    carburantLabel = Label(add_window, text='Type Carburant', font=('SF Pro', 20, 'bold'))
    carburantLabel.grid(row=2, column=0, padx=30, pady=15,sticky=w)
    carburantEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    carburantEntry.grid(row=2, column=1, pady=15, padx=10)

    placesLabel = Label(add_window, text='Nombre Places', font=('SF Pro', 20, 'bold'))
    placesLabel.grid(row=3, column=0, padx=30, pady=15,sticky=w)
    placesEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    placesEntry.grid(row=3, column=1, pady=15, padx=10)

    transmissionLabel = Label(add_window, text='Transmission', font=('SF Pro', 20, 'bold'))
    transmissionLabel.grid(row=4, column=0, padx=30, pady=15,sticky=w)
    transmissionEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    transmissionEntry.grid(row=4, column=1, pady=15, padx=10)

    prixLabel = Label(add_window, text='Transmission', font=('SF Pro', 20, 'bold'))
    prixLabel.grid(row=5, column=0, padx=30, pady=15,sticky=w)
    prixEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    prixEntry.grid(row=5, column=1, pady=15, padx=10)

    add_Voitures_button=ttk.Button(add_window,text='Ajouter Voiture',command=add_data)
    add_Voitures_button.grid(row=7,columnspan=2,pady=15)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo('Success','Database Connection Was Successful',parent=connectWindow)
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='CREATE DATABASE Location'
            mycursor.execute(query)
            query='USE Location'
            mycursor.execute(query)
            query='CREATE TABLE Voitures(id int auto_increment primary key not null,marque varchar(50) not null,type_carburant varchar(50) not null,nombre_de_places int not null,transmission varchar(50) not null,prix_de_location varchar(50) not null)'
            mycursor.execute(query)
        except:
            query='USE Location'
            mycursor.execute(query)
        messagebox.showinfo('Succes','Database Connection Was Successful',parent=connectWindow)
        connectWindow.destroy()
        searchButton.config(state=NORMAL)
        showButton.config(state=NORMAL)
        deleteButton.config(state=NORMAL)
        modifyButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('SF PRO',18))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostEntry=Entry(connectWindow,font=('SF Pro',15),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='Username', font=('SF PRO', 18))
    usernameLabel.grid(row=1, column=0,padx=20)
    usernameEntry = Entry(connectWindow, font=('SF Pro', 15), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('SF PRO', 18))
    passwordLabel.grid(row=2, column=0,padx=20)
    passwordEntry = Entry(connectWindow, font=('SF Pro', 15), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=Button(connectWindow,text='CONNECT', command=connect)
    connectButton.grid(row=3,columnspan=2)

def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%H:%S')
    datetimeLabel.config(text=f'     Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

count=0
text=''
def slider():
    global  text,count
    if count==len(l):
        count=0
        text=''
    text=text+l[count] #L
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(150,slider)

#GUI PART
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('kroc')

root.geometry('1174x680+50+20')
root.resizable(0,0)
root.title('Location De Voiture Application')

datetimeLabel = Label(root,text='hello',font=('SF Pro',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
l='Location De Voiture Application'
sliderLabel=Label(root,font=('The Bold Font',25,'italic bold'),width=30)
sliderLabel.place(x=320,y=0)
slider()

connectButton=ttk.Button(root,text='Connect Database',command=connect_database)
connectButton.place(x=1000,y=0)

leftFrame=Frame(root,bg='dark Orchid')
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='side-car.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

searchButton=ttk.Button(leftFrame,text="Ajouter une voiture",width=15)
searchButton.grid(row=1,column=0,pady=20)

showButton=ttk.Button(leftFrame,text="Voir les voitures",width=15)
showButton.grid(row=2,column=0,pady=20)

deleteButton=ttk.Button(leftFrame,text="Supprimer une voitures",width=15)
deleteButton.grid(row=3,column=0,pady=20)

modifyButton=ttk.Button(leftFrame,text="Modifier une voitures",width=15)
modifyButton.grid(row=4,column=0,pady=20)

clientButton=ttk.Button(leftFrame,text="Ajouter un client",width=15)
clientButton.grid(row=5,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text="Quitter le systeme",width=15)
exitButton.grid(row=6,column=0,pady=20,padx=77)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

VoituresTable=ttk.Treeview(rightFrame,columns=('id', 'marque', 'type_carburant','nombre_de_places', 'transmission', 'prix_de_location')
                       ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=VoituresTable.xview)
scrollBarY.config(command=VoituresTable.yview)


scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

VoituresTable.pack(fill=BOTH,expand=1)

VoituresTable.heading('id',text='id')
VoituresTable.heading('marque',text='marque')
VoituresTable.heading('type_carburant',text='type_carburant')
VoituresTable.heading('nombre_de_places',text='nombre_de_places')
VoituresTable.heading('transmission',text='transmission')
VoituresTable.heading('prix_de_location',text='prix_de_location')

VoituresTable.config(show='headings')

root.mainloop()
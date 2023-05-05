from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
#functionality part
def update_Voiture():

    def update_data():
        query='update Voitures set marque=%s,type_carburant=%s,nombre_de_places=%s,transmission=%s,prix_de_location=%s where id=%s'
        mycursor.execute(query,(marqueEntry.get(),carburantEntry.get(),placesEntry.get(),transmissionEntry.get(),prixEntry.get(),idEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'The car with the id{idEntry.get()} is modified successfully',parent=update_window)
        update_window.destroy()

    update_window = Toplevel()
    update_window.title('Modifier Une Voiture')
    update_window.grab_set()
    update_window.resizable(False, False)

    idLabel = Label(update_window, text='Id', font=('SF Pro', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('SF Pro', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    marqueLabel = Label(update_window, text='Marque Souhaitée', font=('SF Pro', 20, 'bold'))
    marqueLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    marqueEntry = Entry(update_window, font=('SF Pro', 15, 'bold'), width=24)
    marqueEntry.grid(row=1, column=1, pady=15, padx=10)

    carburantLabel = Label(update_window, text='Type Carburant Souhaité', font=('SF Pro', 20, 'bold'))
    carburantLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    carburantEntry = Entry(update_window, font=('SF Pro', 15, 'bold'), width=24)
    carburantEntry.grid(row=2, column=1, pady=15, padx=10)

    placesLabel = Label(update_window, text='Nombre Places Souhaité', font=('SF Pro', 20, 'bold'))
    placesLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    placesEntry = Entry(update_window, font=('SF Pro', 15, 'bold'), width=24)
    placesEntry.grid(row=3, column=1, pady=15, padx=10)

    transmissionLabel = Label(update_window, text='Transmission Souhaitée', font=('SF Pro', 20, 'bold'))
    transmissionLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    transmissionEntry = Entry(update_window, font=('SF Pro', 15, 'bold'), width=24)
    transmissionEntry.grid(row=4, column=1, pady=15, padx=10)

    prixLabel = Label(update_window, text='Prix Par jour Souhaité', font=('SF Pro', 20, 'bold'))
    prixLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    prixEntry = Entry(update_window, font=('SF Pro', 15, 'bold'), width=24)
    prixEntry.grid(row=5, column=1, pady=15, padx=10)

    modifyButton = ttk.Button(update_window, text='Modifier Une Voiture', command=update_data)
    modifyButton.grid(row=7, columnspan=2, pady=15)

    indexing=VoituresTable.focus()
    print(indexing)
    content=VoituresTable.item(indexing)
    listdata=content['values']
    print(listdata)
    idEntry.insert(0,listdata[0])
    marqueEntry.insert(0,listdata[1])
    carburantEntry.insert(0,listdata[2])
    placesEntry.insert(0,listdata[3])
    transmissionEntry.insert(0,listdata[4])
    prixEntry.insert(0,listdata[5])


def afficher_Voitures():
    query = 'select * from Voitures'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    VoituresTable.delete(*VoituresTable.get_children())
    for data in fetched_data:
        VoituresTable.insert('', END, values=data)

def delete_Voiture():
    indexing = VoituresTable.focus()
    print(indexing)
    content=VoituresTable.item(indexing)
    content_id=content['values'][0]
    query='delete from Voitures where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'This Car with the id ({content_id}) is DELETED successfully')
    query='select * from Voitures'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    VoituresTable.delete(*VoituresTable.get_children())
    for data in fetched_data:
        VoituresTable.insert('',END,values=data)

def chercher_voiture():
    def chercher_data():
        query = 'select * from Voitures where id=%s or marque=%s or type_carburant=%s or nombre_de_places=%s or transmission=%s or prix_de_location =%s '
        mycursor.execute(query, (idEntry.get(),marqueEntry.get(),carburantEntry.get(),
                                 placesEntry.get(),transmissionEntry.get(),prixEntry.get()))
        VoituresTable.delete(*VoituresTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            VoituresTable.insert('', END, values=data)



    chercher_window = Toplevel()
    chercher_window.title('Chercher Une Voiture')
    chercher_window.grab_set()
    chercher_window.resizable(False, False)

    idLabel = Label(chercher_window, text='Id', font=('SF Pro', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(chercher_window, font=('SF Pro', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    marqueLabel = Label(chercher_window, text='Marque Souhaitée', font=('SF Pro', 20, 'bold'))
    marqueLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    marqueEntry = Entry(chercher_window, font=('SF Pro', 15, 'bold'), width=24)
    marqueEntry.grid(row=1, column=1, pady=15, padx=10)

    carburantLabel = Label(chercher_window, text='Type Carburant Souhaité', font=('SF Pro', 20, 'bold'))
    carburantLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    carburantEntry = Entry(chercher_window, font=('SF Pro', 15, 'bold'), width=24)
    carburantEntry.grid(row=2, column=1, pady=15, padx=10)

    placesLabel = Label(chercher_window, text='Nombre Places Souhaité', font=('SF Pro', 20, 'bold'))
    placesLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    placesEntry = Entry(chercher_window, font=('SF Pro', 15, 'bold'), width=24)
    placesEntry.grid(row=3, column=1, pady=15, padx=10)

    transmissionLabel = Label(chercher_window, text='Transmission Souhaitée', font=('SF Pro', 20, 'bold'))
    transmissionLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    transmissionEntry = Entry(chercher_window, font=('SF Pro', 15, 'bold'), width=24)
    transmissionEntry.grid(row=4, column=1, pady=15, padx=10)

    prixLabel = Label(chercher_window, text='Prix Par jour Souhaité', font=('SF Pro', 20, 'bold'))
    prixLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    prixEntry = Entry(chercher_window, font=('SF Pro', 15, 'bold'), width=24)
    prixEntry.grid(row=5, column=1, pady=15, padx=10)

    showButton = ttk.Button(chercher_window, text='Chercher Votre Voiture', command=chercher_data)
    showButton.grid(row=7, columnspan=2, pady=15)

def close_window():
    root.destroy()
def add_Voitures():
    def add_data():
        if idEntry.get()=='' or marqueEntry.get()=='' or transmissionEntry.get()=='' or placesEntry.get()=='' or prixEntry.get()=='' or carburantEntry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=add_window)
        else:
            currentdate = time.strftime('%d/%m/%Y')
            currenttime = time.strftime('%H:%H:%S')
            try:
                query='INSERT INTO Voitures VALUES(%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (idEntry.get(), marqueEntry.get(),carburantEntry.get(),placesEntry.get(),transmissionEntry.get(),prixEntry.get()))

                con.commit()
                result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form? ',parent=add_window)
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
            except:
                messagebox.showerror('ERROR','ID already exists!',parent=add_window)
                return

            query='SELECT *FROM Voitures'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            VoituresTable.delete(*VoituresTable.get_children())
            for data in fetched_data:
                VoituresTable.insert('',END,values=data)

    add_window = Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)

    idLabel=Label(add_window,text='Id',font=('SF Pro',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('SF Pro',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    marqueLabel = Label(add_window, text='Marque', font=('SF Pro', 20, 'bold'))
    marqueLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    marqueEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    marqueEntry.grid(row=1, column=1, pady=15, padx=10)

    carburantLabel = Label(add_window, text='Type Carburant', font=('SF Pro', 20, 'bold'))
    carburantLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    carburantEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    carburantEntry.grid(row=2, column=1, pady=15, padx=10)

    placesLabel = Label(add_window, text='Nombre Places', font=('SF Pro', 20, 'bold'))
    placesLabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    placesEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    placesEntry.grid(row=3, column=1, pady=15, padx=10)

    transmissionLabel = Label(add_window, text='Transmission', font=('SF Pro', 20, 'bold'))
    transmissionLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    transmissionEntry = Entry(add_window, font=('SF Pro', 15, 'bold'), width=24)
    transmissionEntry.grid(row=4, column=1, pady=15, padx=10)

    prixLabel = Label(add_window, text='Prix Par jour', font=('SF Pro', 20, 'bold'))
    prixLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
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

        addButton.config(state=NORMAL)
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

addButton=ttk.Button(leftFrame,text="Ajouter une voiture",width=15,state=DISABLED,command=add_Voitures)
addButton.grid(row=1,column=0,pady=20)

showButton=ttk.Button(leftFrame,text="Chercher une voiture",width=15,command=chercher_voiture)
showButton.grid(row=2,column=0,pady=20)

deleteButton=ttk.Button(leftFrame,text="Supprimer une voiture",width=15,state=DISABLED,command=delete_Voiture)
deleteButton.grid(row=3,column=0,pady=20)

modifyButton=ttk.Button(leftFrame,text="Modifier une voiture",width=15,state=DISABLED,command=update_Voiture)
modifyButton.grid(row=4,column=0,pady=20)

afficherButton=ttk.Button(leftFrame,text="Afficher les voitures",width=15,command=afficher_Voitures)
afficherButton.grid(row=5,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text="Quitter le systeme",width=15,command=close_window)
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

VoituresTable.column('id',width=50,anchor=CENTER)
VoituresTable.column('marque',width=300,anchor=CENTER)
VoituresTable.column('type_carburant',width=400,anchor=CENTER)
VoituresTable.column('nombre_de_places',width=200,anchor=CENTER)
VoituresTable.column('transmission',width=400,anchor=CENTER)
VoituresTable.column('prix_de_location',width=100,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('SF Pro',15),
                foreground='VioletRed1',background='yellow green')
style.configure('Treeview.Heading',font=('The Bold Font',15))
VoituresTable.config(show='headings')

root.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Should Be Filled')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Unmatching Passwords')
    elif check.get()==0:
        messagebox.showerror('Error','Please Agree To The Terms & Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='driss123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connection Error,Try in few minutes')
            return
        try:
            query='create database Location'
            mycursor.execute(query)
            query='use Location'
            mycursor.execute(query)
            query='create table utilisateur(id int auto_increment primary key not null,email varchar(50),username varchar(40),password varchar(32))'
            mycursor.execute(query)
        except:
            mycursor.execute('use Location')

        query='select * from utilisateur where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username Already Exists')
        else:
            query='insert into utilisateur(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Succes','Registration Was Succesful!')
            clear()
            signup_window.destroy()
            import signin


def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='background.png')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()


frame=Frame(signup_window)
frame.place(x=554,y=100)


heading=Label(frame,text="Create An Account",font=("The Bold Font",26,'bold')
              ,bg='white',fg='goldenrod1')
heading.grid(row=0,column=0,padx=50,pady=10)


emailLabel=Label(frame,text="Email",font=("The Bold Font",10),bg='white'
                 ,fg='goldenrod1')
emailLabel.grid(row=1,column=0,sticky='w',padx=75,pady=(10,0))

emailEntry=Entry(frame,width=30,font=("SF Pro",10)
                 ,fg='white',bg='goldenrod1')
emailEntry.grid(row=2,column=0,sticky='w',padx=75)


usernameLabel=Label(frame,text="Username",font=("The Bold Font",10),bg='white'
                 ,fg='goldenrod1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=75,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=("SF Pro",10)
                 ,fg='white',bg='goldenrod1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=75)


passwordLabel=Label(frame,text="Password",font=("The Bold Font",10),bg='white'
                 ,fg='goldenrod1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=75,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=("SF Pro",10)
                 ,fg='white',bg='goldenrod1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=75)


confirmLabel=Label(frame,text="Confirm Password",font=("The Bold Font",10),bg='white'
                 ,fg='goldenrod1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=75,pady=(10,0))

confirmEntry=Entry(frame,width=30,font=("SF Pro",10)
                 ,fg='white',bg='goldenrod1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=75)

check=IntVar()
termsandconditions=Checkbutton(frame,text="I Agree To The Terms & Conditions",font=("SF Pro",10,"bold")
                               ,fg='goldenrod1',bg='white',activebackground='white',activeforeground='goldenrod1'
                               ,cursor="hand2",variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=45)

signupButton=Button(frame,text="Sign UP",font=("The Bold Font",16,'bold'),bd=0,bg='goldenrod1',fg='white'
                    ,activebackground='goldenrod1',activeforeground='goldenrod1',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)


alreadyaccount=Label(frame,text="Already Have An Account ?",font=("SF Pro",10,'bold')
                     ,bg='white',fg='goldenrod1')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton=Button(frame,text='Log in',font=('SF Pro',10,'bold underline')
                   ,bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.grid(row=11,column=4)




signup_window.mainloop()

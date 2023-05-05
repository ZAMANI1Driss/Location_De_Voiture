from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


#Functionality Part

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Should Be Filled')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='driss123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection failed, try again later')
            return
        query='use Location'
        mycursor.execute(query)
        query='select * from Clients where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username Or Password')
        else:
            messagebox.showinfo('Succes ','Welcome!')
        window.destroy()
        import main


def signup_page():
    login_window.destroy()
    import signup
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#GUI Part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='background.png')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(login_window,text='USER LOGIN',font=('The Bold Font',30,'bold')
              ,bg='white',fg='goldenrod1')
heading.place(x=680,y=120)

usernameEntry=Entry(login_window,width=25,font=('SF Pro',11,'bold')
                    ,bd=0,fg='goldenrod1')
usernameEntry.place(x=650,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)


frame1=Frame(login_window,width=250,height=2,bg='goldenrod1')
frame1.place(x=650,y=222)

passwordEntry=Entry(login_window,width=25,font=('SF Pro',11,'bold')
                    ,bd=0,fg='goldenrod1')
passwordEntry.place(x=650,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='goldenrod1')
frame2.place(x=650,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',
                 cursor='hand2',command=hide)
eyeButton.place(x=860,y=255)
forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',
                 cursor='hand2',font=('SF Pro',9,'bold'),fg='goldenrod1',activeforeground='goldenrod1')
forgetButton.place(x=775,y=295)


loginButton=Button(login_window,text='Login',font=('The Bold Font',16,'bold'),
                   fg='goldenrod1',bg='goldenrod1',activeforeground='goldenrod1'
                   ,activebackground='goldenrod1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=625,y=350)

orLabel=Label(login_window,text='--------------- OR --------------',font=('SF Pro',16),fg='goldenrod1',bg='white')
orLabel.place(x=653,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=700,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=750,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=800,y=440)

singupLabel=Label(login_window,text="Don't have an account ?",font=('SF Pro',10),fg='goldenrod1',bg='white')
singupLabel.place(x=650,y=500)

newaccountButton=Button(login_window,text='Create New One',font=('The Bold Font',10,'underline'),
                   fg='blue',bg='white',activeforeground='blue'
                   ,activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=787,y=500)

login_window.mainloop()

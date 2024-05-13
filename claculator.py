from tkinter import*
w = Tk()
w.configure(bg = 'grey')
w.geometry('300x400')
w.resizable(False,False)
w.title('simple calculator for hakim')


###################################################
#this parti the progaraming
###################################################

varF = StringVar()
varS = StringVar()
varT = StringVar()


def plus():
    varT.set('+')
def moins():
    
    varT.set('-')
def multi():
    varT.set('x')
def div():
    varT.set('/')

def total():
    try:
        
        if varT.get() == '+' :
            varT.set(int(varS.get())+int(varF.get()))
            varS.set('')
            varF.set('')
        elif varT.get() == '-':
            varT.set(int(varS.get())-int(varF.get()))
            varS.set('')
            varF.set('')
        elif varT.get() == 'x':
            varT.set(int(varS.get())*int(varF.get()))
            varS.set('')
            varF.set('')
        elif varT.get() == '/':
            varT.set(int(varS.get())/int(varF.get()))
            varS.set('')
            varF.set('')
    except:
        pass








###################################################
#this parti the desighne
###################################################

lb1 = Label(w,text = 'First',
            bg = 'grey',
            fg = 'white' ,
            font = ('arial',8,'bold'))
lb2 = Label(w,text = 'Second',
            bg = 'grey',
            fg = 'white' ,
            font = ('arial',8,'bold'))
lb3 = Label(w,text = 'Total',
            bg = 'grey',
            fg = 'white' ,
            font = ('arial',8,'bold'))

lb1.place(x = 10 , y =50)
lb2.place(x = 10 , y =100)
lb3.place(x = 10 , y =300)

ent1 = Entry(w,textvariable = varS)
ent2 = Entry(w,textvariable = varF)
ent3 = Entry(w,textvariable = varT)

ent1.place(x = 90 , y = 50,width = 200)
ent2.place(x = 90 , y = 100,width = 200)
ent3.place(x = 90 , y = 300,width = 200)

bt1 = Button(w,text = 'go',
             font = ('arial' , 8 , 'bold'),
             bd = 5  ,
             command = total,
             relief = 'groove')
bt2 = Button(w,text = '+',
             width = 5,
             font = ('arial' , 8 , 'bold'),
             bd = 5  ,
             command = plus,
             relief = 'groove')
bt3 = Button(w,text = '/',
             width = 5 ,
             font = ('arial' , 8 , 'bold'),
             bd = 5,
             command = div,
             relief = 'groove')
bt4 = Button(w,text = '-',
             width = 5 ,
             font = ('arial' , 8 , 'bold'),
             bd = 5  ,
             command = moins,
             relief = 'groove')
bt5 = Button(w,text = 'x',
             width = 5 ,
             command = multi,
             font = ('arial' , 8 , 'bold'),
             bd = 5  ,
             relief = 'groove')

bt1.place(x = 120 , y = 350 ,width = 60)
bt2.place(x = 50 , y = 200)
bt3.place(x = 100 , y = 200)
bt4.place(x = 150 , y = 200)
bt5.place(x = 200,y = 200)


from tkinter import *

win = Tk()
win.title('calculatrice')
win.resizable(False , False )


#string = StringVar()
number = StringVar()

ent1 = Entry(win , bd= 7 , width = 13, font ='arial 25 bold' ,
             textvariable = number, relief = SUNKEN ,bg = 'lightblue',
             )
ent1.grid(row = 0 , column = 0, pady = 15 , columnspan = 30)

number.set('')

def click(txt):
        ent1.insert(END, txt)

def zero():
        ent1.insert(END,'0')


def equal():
        try:
                n = number.get()
                number.set('')
                number.set(eval(n))
        except:
                pass

    
def clear():
        a = 0
        b = 0
        number.set('')
        


class button:
        def __init__(self , tx , x , y ):
                bt = Button(win  , text = tx ,command = lambda: click(tx) ,width = 5 ,
                        height = 2 , relief = 'raised' , bd = 5  )
                bt.grid(row = x , column = y)
       
b1 = button('1' , 1 , 0 )
b2 = button('2' , 1 , 1)
b3 = button('3' , 1 , 2)
b4 = button ('4' , 2, 0 )
b5 = button ('5' , 2, 1 )
b6 = button ('6' , 2, 2 )
b7 = button ('7' , 3, 0 )
b9 = button ('9' , 3, 2 )
b8 = button ('8' , 3, 1 )
b10 = button('/' , 1, 3 )
b10 = button('.' , 4 , 2 )


equalbt = Button(win , text = '=' , command = equal , width = 5 ,
                 height = 5 , relief = 'raised' , bd = 5 )

equalbt.grid(row = 3, column = 4 ,rowspan = 2 )

addbt= Button(win  , text = '+'  ,command =lambda:click('+') ,width = 5 ,
                    height = 2 , relief = 'raised' , bd = 5 )
addbt.grid(row = 4 , column = 3)


mbt= Button(win  , text = '-'  ,command =lambda:click('-') ,width = 5 ,
                    height = 2 , relief = 'raised' , bd = 5 )
mbt.grid(row = 3 , column = 3)

clbt = Button(win , text = 'C' ,command = clear , width = 5 ,
              height = 5 , relief = 'raised' , bd = 5)
clbt.grid(row = 1 , column = 4 , rowspan = 2)

prodbt = Button(win , text = 'x' , command = lambda : click('*') , width = 5,
                height =2 , relief = 'raised' , bd = 5)

prodbt.grid(row =2 , column = 3 )

zerobt = Button(win , text = 0 , command  = zero , width = 12 , height = 2 ,
                relief = 'raised' , bd = 5 )
zerobt.grid(row = 4 ,column = 0 , columnspan = 2 )

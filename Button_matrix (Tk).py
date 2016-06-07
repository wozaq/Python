from tkinter import *
from tkinter import messagebox as mb

############
def main():
    global okno
    okno=Tk()
    Label(okno,text="Choose your layout:").grid(row=1,columnspan=3)
    Button(okno,text="Pack",command=window_pack).grid(column=0,row=2)
    Button(okno,text="Rectangle", command=window_rectangle).grid(column=1,row=2)
    Button(okno,text="Diamond", command=window_diamond).grid(column=2,row=2)
    okno.mainloop()

############
def create_buttons(win,num_buttons):
    button_list=[]

    for z in range (num_buttons):
        if z<=8:
            txt="Button 0"+str(z+1)
        else:
            txt="Button "+str(z+1)
        button=Button(win,text=txt,bg="cyan")
        button_list.append(button)
        
    return button_list

############
def window_input():
    global okno_input
    okno_input=Tk()

    okno_input.focus_force()
    Label(okno_input,text="Specify a number of buttons to create (4-99):").grid(row=1,columnspan=2)
    global inpt
    inpt=Entry(okno_input,width=10)
    inpt.grid(column=0,row=2)
    inpt.bind("<Return>",confirm)
    OK=Button(okno_input, text="OK")
    OK.grid(column=1,row=2)
    OK.bind("<Button-1>",confirm)

    okno_input.mainloop()

def confirm(event):
    global num_buttons
    num_buttons=0
    try:
        num_buttons=int(inpt.get())

        if num_buttons>=4 and num_buttons<=99:
            okno_input.destroy()
            okno.destroy()
        else:
            mb.showwarning("Error!","Number must be from range 4-99! Try again!")

    except:
        mb.showwarning("Error!","Please specify a number!")
    
############
def window_pack():
    window_input()
    
    okno_pack=Tk()
    okno_pack.focus_force()
    button_list=create_buttons(okno_pack,num_buttons)

    for z in (button_list):
        z.pack()

    okno_pack.mainloop()

##############
def window_rectangle():
    window_input()

    okno_rectangle=Tk()
    okno_rectangle.focus_force()
    button_list=create_buttons(okno_rectangle,num_buttons)

    side=len(button_list)//4
    rest=(len(button_list)%4)//2
    
    if rest!=0:
        add=1
    else:
        add=0

    c=0
    r=1
    count=0

    if side==1:
        for z in (button_list):
            if count+1<=side+1:
                z.grid(row=0,column=c,sticky=W+E)
                count+=1
                c+=1
            elif count+1>side+1 and count+1<=2*side+rest+1:
                z.grid(row=r,column=c-1)
                r+=1
                count+=1
            elif count+1>2*side+rest+1 and count+1<=3*side+rest+2:
                z.grid(row=r-1,column=c-2)
                r-=1
                count+=1
        
    else:
        for z in (button_list):
            #w prawo
            if count+1<=side:
                z.grid(row=0,column=c,sticky=W+E)
                c+=1
                count+=1
        
            #w dol
            elif count+1>side and count+1<=2*side+rest+add:
                z.grid(row=r,column=c-1,sticky=W+E)
                r+=1
                count+=1
            
            #w lewo    
            elif count+1>2*side+rest+add and count+1<=3*side+add:
                z.grid(row=r-1,column=c-1)
                c-=1
                count+=1

            #w gore
            elif count>=3*side+add and count<=4*side+2*add:
                c=0
                z.grid(row=r-1,column=c)
                r-=1
                count+=1

        okno_rectangle.mainloop()

##############    
def window_diamond():
    window_input()
    okno_diamond=Tk()

    okno_diamond.focus_force()
    button_list=create_buttons(okno_diamond,num_buttons)

    side=len(button_list)//4
    c=2*side//2+1
    r=0
    count=0

########dodac dla mniej niz 8 buttonow

    for z in (button_list):
        #prawy-dol
        if count+1<=side:     
            z.grid(row=r,column=c,sticky=W+E)
            r+=1
            c+=1
            count+=1
            
        #lewy-dol
        elif count+1>side and count+1<=2*side-1:
            z.grid(row=r,column=c-2)
            r+=1
            c-=1
            count+=1

        #lewy-gora
        elif count+1>2*side-1 and count<=3*side-3:
            z.grid(row=r-2,column=c-2)
            r-=1
            c-=1
            count+=1

        #prawy-gora
        elif count+1>3*side-3 and count+1<=4*side-3:
            z.grid(row=r-2,column=c)
            r-=1
            c+=1
            count+=1

    okno_diamond.mainloop()

##############
main()

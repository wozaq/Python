from tkinter import *
from time import sleep

####Main####
def main():
    
    kolumna()
    wiersz()
    mnozenie()
    global status_bar
    status_bar = Label(okno, text="Tu beda współrzędne wciskanego przycisku", bo=1, relief=SUNKEN)
    status_bar.grid(row=12,columnspan=12,sticky=E+W)

def kolumna():
    for z in range(1,11):
            kolumna=Button(okno,bg="green", text=str(z))
            kolumna.grid(column=0,row=z,sticky=E+W)


def wiersz():
    for z in range(1,11):
            wiersz=Button(okno,bg="green", text=str(z))
            wiersz.grid(column=z,row=0,sticky=E+W)

def mnozenie():
    a=1
    b=1
    for i in range(10):
        for z in range(10):
            liczba=a*b

            przycisk=Button(okno,text=str(liczba))
            przycisk.grid(column=a,row=b, sticky=E+W)
                                
            a+=1
        b+=1
        a=1
        
    przycisk.bind_class("Button","<Button-1>",podswietl)

def podswietl(zdarzenie):
    
    grid_info = zdarzenie.widget.grid_info()
    row=grid_info["row"]
    column=grid_info["column"]
    status="Współrzędne przycisku to: K"+str(column)+";W"+str(row)
    

    c=1
    r=1

    if row>0 and column>0:
        status_bar.config(text=status)

        for z in range(1,11):
            text1=column*r
            baton1=Button(okno,bg="cyan",relief="sunken",text=text1)
            baton1.grid(column=column,row=r,sticky=E+W)
            text2=c*row
            baton2=Button(okno,bg="cyan",relief="sunken",text=text2)
            baton2.grid(column=c,row=row,sticky=E+W)
            r+=1
            c+=1

    else:
        status_bar.config(text="Tu będą współrzędne wciskanego przycisku")

##    sleep(0.5)
##    Przycisk.config(self,bg="gray",relief="raised")
        
##############
okno=Tk()

main()



okno.mainloop()

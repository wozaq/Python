from tkinter import *

####Rectangles####
width=30
pad_rect=15
##################

#######Fonts######
str_font=width-width//2
font="Tahoma "+str(str_font)+" bold"
str_font100=str_font-width//7
font100="Tahoma "+str(str_font100)+" bold"
##################

##################
def main():
    okno=Tk()

    ramka1=Frame(okno)
    ramka1.pack()
    Label(ramka1, text="Tabliczka mnożenia", font="Tahoma 16 bold").pack(fill=X)

    ramka2=Frame(okno)
    global rysunek
    rysunek=Canvas(ramka2, bg="cyan",width=11*(width+pad_rect),\
            height=11*(width+pad_rect))
    ramka2.pack()
    rysunek.pack(fill=X)

    rectangles(width,pad_rect)

    okno.mainloop()

##################    
def rectangles(width,pad_rect):
    
    startX=width+pad_rect+10
    startY=10
    endX=startX+width
    endY=startY+width
    offset=width+pad_rect
    pad_text=width-(width-width//2)
    
    ###############
    #naglowek (1-10)
    
    for z in range (10):
        text=z+1
        rysunek.create_rectangle(startX,startY,endX,endY,fill="yellow")
        rysunek.create_text(startX+pad_text,startY+pad_text,\
                            text=text, font=font)
        startX+=offset
        endX+=offset
        
    #######
    #reszta
    startX=10
    startY=startY+offset
    endX=startX+width
    endY=startY+width
    count=1
    
    for z in range (10):
        for k in range (11):
            if k==0:
                text=count
                fill="yellow"
            else:
                text=k*count
                fill="wheat"
            
            rysunek.create_rectangle(startX,startY,endX,endY,fill=fill)
            if text<100:
                rysunek.create_text(startX+pad_text,startY+pad_text,\
                                    text=text, font=font)
            else:
                rysunek.create_text(startX+pad_text,startY+pad_text,\
                                    text=text, font=font100)
            startX+=offset
            endX+=offset
            
        startY+=offset
        endY+=offset
        startX=10
        endX=startX+width
        count+=1

############
main()

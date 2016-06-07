from tkinter import *

##############
class Buttons:

    def Confirm(self,event):
        try:
            self.num_buttons=int(self.inpt1.get())
            self.num_columns=int(self.inpt2.get())

            self.window_input.destroy()
            self.CreateButtons()

        except:
            pass

    def Input(self):
        self.window_input=Tk()
        
        Label(self.window_input,text="How many buttons to create?").pack()
        self.inpt1=Entry(self.window_input,width=10)
        self.inpt1.pack()

        Label(self.window_input,text="How many columns?").pack()
        self.inpt2=Entry(self.window_input,width=10)
        self.inpt2.pack()
        
        self.OK=Button(self.window_input,text="OK")
        self.OK.bind("<Button-1>",self.Confirm)
        self.OK.pack()

    def ButtonPressed(self,event):
        self.grid_info=event.widget.grid_info()
        self.r=self.grid_info["row"]
        self.c=self.grid_info["column"]
        self.label="You've clicked Button "

        self.text=self.label+str(self.num_columns*(self.r-1)+self.c+1)
        self.output.config(text=self.text)
            
    def CreateButtons(self):
        self.window_grid=Tk()
        self.buttons_list=[]
        self.count=1

        for z in range (self.num_buttons):
            if self.count%2==0:
                button=Button(self.window_grid,bg="cyan",text="Button "+str(z+1))
                self.buttons_list.append(button)
                self.count+=1
            else:
                button=Button(self.window_grid,bg="wheat",text="Button "+str(z+1))
                self.buttons_list.append(button)
                self.count+=1
                      
        Label(self.window_grid,text="Buttons matrix:", font="Tahoma 12 bold")\
                                             .grid(columnspan=self.num_columns)
        self.column=0
        self.row=1

        for z in self.buttons_list:
            z.grid(row=self.row,column=self.column,sticky=W+E)

            if self.column==self.num_columns-1:
                self.column=0
                self.row+=1
            else:
                self.column+=1

        self.output=Label(self.window_grid,font="Tahoma 12 bold",\
                          text="I will show here which button has been pressed!")
        self.output.grid(row=self.row+1,column=0,columnspan=self.num_columns)

        button.bind_class("Button","<Button-1>",self.ButtonPressed)

##############
def main():
    
    buttons=Buttons()
    buttons.Input()

##############
main()
    

from tkinter import *
from tkinter import messagebox as mb

####################################################################
class Interface:
####################################################################    
    def RefreshFrame(self,event,account_type,cond):
##        print(account_type)
        if self.frame!=0:
            self.frame.destroy()
        
        self.frame=Frame(self.window_input,relief=SUNKEN)
        self.frame.grid(row=4,columnspan=2)

        Label(self.frame,text="Account number:").grid(columnspan=2)
            
        self.account_num_entry=Entry(self.frame,width=28)
        self.account_num_entry.grid(row=1,columnspan=2)

        if account_type==1:         
            Label(self.frame,text="Name:").grid(row=2,column=0,sticky=E)
            self.name_entry=Entry(self.frame,width=18)
            self.name_entry.grid(row=2,column=1)

            Label(self.frame,text="Surname:").grid(row=3,column=0,sticky=E)
            self.surname_entry=Entry(self.frame,width=18)
            self.surname_entry.grid(row=3,column=1)

            Label(self.frame,text="Money:").grid(row=4,column=0,sticky=E)
            self.account_money_entry=Entry(self.frame,width=10)
            self.account_money_entry.grid(row=4,column=1)

            self.baton1=Button(self.frame,text="Next")
            self.baton1.bind("<Button-1>",\
                            lambda event:self.Confirm(event,account_type=1))
            self.baton1.grid(row=5,column=0,sticky=W)

            self.baton2=Button(self.frame,text="Save and exit")
            self.baton2.bind("<Button-1>",\
                             lambda event:self.SaveExit(event,cond=cond,account_type=1))
            self.baton2.grid(row=5,column=1,sticky=E)

        elif account_type==2:          
            self.account_num_entry=Entry(self.frame,width=28)
            self.account_num_entry.grid(row=1,columnspan=2)

            Label(self.frame,text="Company name:").grid(row=2,column=0,sticky=E)
            self.company_name_entry=Entry(self.frame,width=12)
            self.company_name_entry.grid(row=2,column=1)

            Label(self.frame,text="Money:").grid(row=3,column=0,sticky=E)
            self.account_money_entry=Entry(self.frame,width=10)
            self.account_money_entry.grid(row=3,column=1)

            self.baton1=Button(self.frame,text="Next")
            self.baton1.bind("<Button-1>",\
                            lambda event,:self.Confirm(event,account_type=2))
            self.baton1.grid(row=4,column=0,sticky=W)

            self.baton2=Button(self.frame,text="Save and exit")
            self.baton2.bind("<Button-1>",\
                             lambda event:self.SaveExit(event,cond=cond,account_type=2))
            self.baton2.grid(row=4,column=1,sticky=E)
            
############
    def NextPage(self):
        self.frame.destroy()
        self.number+=1
        self.text="Specify account number "+str(self.number)+":"
        self.label.config(text=self.text)
        
############
    def Confirm(self,event,account_type):
        if self.account_money_entry.get()=="":
            account_money=0
        else:
            account_money=self.account_money_entry.get()
        if self.account_num_entry.get()!="":
            try:
                account_num=int(self.account_num_entry.get())
                try:
                    account_money=int(account_money)
                        
                    if len(self.account_num_entry.get())==26:
                        if account_type==1: #private
                            name=self.name_entry.get()
                            surname=self.surname_entry.get()
                            

                            if name!="" and surname!="":
                                private_account_obj=PrivateAccount(name,account_num,account_money,\
                                                                   surname,account_type="Private")
                                Accounts_table.append(private_account_obj)
                                self.NextPage()
                                print(private_account_obj.__dict__)
                                return True
                            else:
                                mb.showwarning("Error!","Name and surname cannot be blank!")
                                return False
                                                    
                        elif account_type==2:#company
                            company_name=self.company_name_entry.get()

                            if company_name!="":
                                company_account_obj=CompanyAccount(company_name,account_num,account_money,\
                                                                   account_type="Company")
                                Accounts_table.append(company_account_obj)
                                self.NextPage()
                                print(company_account_obj.__dict__)
                                return True
                            else:
                                mb.showwarning("Error!","Company name cannot be blank!")
                                return False
                    else:
                        self.account_num_entry.config(bg="tomato")
                        mb.showwarning("Error!","Account number must have 26 digits!")
                        return False

                except ValueError:
                    mb.showwarning("Error!","Money must consist of digits only!")
                    return False
                                   
            except ValueError:
                    self.account_num_entry.config(bg="tomato")
                    mb.showwarning("Error!","Account number must consist of digits only!")
                    return False
        else:
            self.account_num_entry.config(bg="tomato")
            mb.showwarning("Error!","Account number cannot be blank!")
            return False

############
    def SaveExit(self,event,account_type,cond=0):
        var=self.Confirm(event,account_type)
        if var==True and cond==0:
            self.window_input.destroy()
            self.MainMenu()
        else:
            pass
              
##Windows###
############                
    def InputWindow(self,number=1,cond=0):
        self.window_input=Tk()
        self.number=number
        self.text="Specify account number "+str(self.number)+":"
        self.account_type=IntVar()
        self.frame=0

        self.label=Label(self.window_input,text=self.text)
        self.label.grid(row=1,columnspan=2)

        Label(self.window_input,text="Account type: ").grid(row=2,columnspan=2)
        rad_button1=Radiobutton(self.window_input,text="Private",\
                                variable=self.account_type,value=1)
        rad_button1.bind("<Button-1>",\
                         lambda event:self.RefreshFrame(event,1,cond))
        rad_button1.grid(row=3,column=0)

        rad_button2=Radiobutton(self.window_input,text="Company",\
                                variable=self.account_type,value=2)
        rad_button2.bind("<Button-1>",\
                         lambda event:self.RefreshFrame(event,2,cond))
        rad_button2.grid(row=3,column=1)

        self.baton0=Button(self.window_input,text="Create objects from Accounts.txt")
        self.baton0.bind("<Button-1>",\
                         lambda event:Account.CreateObjects(self))
        self.baton0.grid(row=5,columnspan=2)

        self.window_input.mainloop()

############
    def MainMenu(self):
        self.main_menu=Tk()
        self.obj_num=int(len(Accounts_table))+1

        Label(self.main_menu,text="MAIN MENU").pack()

        self.b1=Button(self.main_menu,text="1.Money transfer")
        self.b1.bind("<Button-1>",\
                     lambda event:Account.MoneyTransfer(self,event,win=1))
        self.b1.pack(fill=X)

        self.b2=Button(self.main_menu,text="2.Show objects")
        self.b2.bind("<Button-1>",\
                     lambda event:Account.ShowObjects(self,event,win=2))
        self.b2.pack(fill=X)

        self.b4=Button(self.main_menu,text="3.Add account")
        self.b4.bind("<Button-1>",\
                     lambda event:self.InputWindow(self.obj_num,1))
        self.b4.pack(fill=X)

        self.b4=Button(self.main_menu,text="4.Exit")
        self.b4.bind("<Button-1>",\
                     lambda event:self.main_menu.destroy())
        self.b4.pack(fill=X)


##    def Show(self):
##        print(self.F)
##        print(self.T)
##############
    def OutputWindow(self,event,win):
        self.window_output=Tk()

        self.root_frame=Frame(self.window_output)
        self.root_frame.pack()

        if win==1:
            Label(self.root_frame,text="Money transfer").grid(row=0,columnspan=3)
            Label(self.root_frame,text="From:").grid(row=2,column=0)
            Label(self.root_frame,text="To:").grid(row=2,column=2)

            table=[]
            for obj in Accounts_table:
                surname=""
                try:
                    surname=obj.surname
                except AttributeError:
                    pass
                table.append(obj.name+" "+surname)

            self.F=StringVar()
            self.T=StringVar()
            self.From=OptionMenu(self.root_frame,self.F,*table).grid(row=3,column=0)
            self.To=OptionMenu(self.root_frame,self.T,*table).grid(row=3,column=2)
                
        elif win==2:
            Label(self.root_frame,text="Name").grid(row=0,column=0)
            Label(self.root_frame,text="Surname").grid(row=0,column=1)
            Label(self.root_frame,text="Account number").grid(row=0,column=2)
            Label(self.root_frame,text="Money").grid(row=0,column=3)
            Label(self.root_frame,text="Account type").grid(row=0,column=4)
            
            self.output_text1=Text(self.root_frame,height=20,width=10)
            self.output_text1.grid(row=1,column=0,sticky=W+E)

            self.output_text2=Text(self.root_frame,height=20,width=18)
            self.output_text2.grid(row=1,column=1,sticky=W+E)

            self.output_text3=Text(self.root_frame,height=20,width=26)
            self.output_text3.grid(row=1,column=2,sticky=W+E)

            self.output_text4=Text(self.root_frame,height=20,width=10)
            self.output_text4.grid(row=1,column=3,sticky=W+E)

            self.output_text5=Text(self.root_frame,height=20,width=10)
            self.output_text5.grid(row=1,column=4,sticky=W+E)

            self.bb1=Button(self.root_frame,text="Save to Accounts.txt")
            self.bb1.bind("<Button-1>",lambda event:Account.WriteToFile(self,event))
            self.bb1.grid(row=2,column=0,sticky=W)

            self.bb2=Button(self.root_frame,text="Close")
            self.bb2.bind("<Button-1>",lambda event:self.window_output.destroy())
            self.bb2.grid(row=2,column=4,sticky=E)

            for account in Accounts_table:
                self.output_text1.insert(END,str(account.name)+"\n")
                try:
                    self.output_text2.insert(END,str(account.surname)+"\n")
                except AttributeError:
                    self.output_text2.insert(END,"\n")
                self.output_text3.insert(END,str(account.account_num)+"\n")
                self.output_text4.insert(END,str(account.account_money)+"\n")
                self.output_text5.insert(END,str(account.account_type)+"\n")

            self.output_text1.config(state=DISABLED)
            self.output_text2.config(state=DISABLED)
            self.output_text3.config(state=DISABLED)
            self.output_text4.config(state=DISABLED)

        self.window_output.mainloop()       
        
################################################################################
class Account:
################################################################################
    def __init__ (self,name,account_num,account_money,account_type):
        self.name=name
        self.account_num=account_num
        self.account_money=account_money
        self.account_type=account_type
        
############
    def MoneyTransfer(self,event,win):
        Interface.OutputWindow(self,event,win)

############
    def MaxLenght(self):
        self.max_name=0
        self.max_surname=0
        self.max_money=0
        
        for account in Accounts_table:
            self.name_lenght=int(len(account.name))
            try:
                self.surname_lenght=int(len(account.surname))
            except AttributeError:
                pass
            self.money_lenght=int(len(str(account.account_money)))

            if self.name_lenght>self.max_name:
                self.max_name=self.name_lenght
            if self.surname_lenght>self.max_surname:
                self.max_surname=self.surname_lenght
            if self.money_lenght>self.max_money:
                self.max_money=self.money_lenght

##        print("max name lenght",self.max_name)
##        print("max surname lenght",self.max_surname)
    
############
    def WriteToFile(self,event):
        self.file=open("Accounts.txt","w")
        self.lenght=int(len(Accounts_table))
        self.count=0
        Account.MaxLenght(self)
        try:
            for account in Accounts_table:
                self.count+=1
                surname=""
                try:
                    surname=str(account.surname)
                except AttributeError:
                    pass

                name_lenght=int(len(account.name))
                name_space=self.max_name-name_lenght
                surname_lenght=int(len(surname))
                surname_space=self.max_surname-surname_lenght
                money_lenght=int(len(str(account.account_money)))
                money_space=self.max_money-money_lenght

##                print("name space",account.name,name_space)
##                print("surname space",surname,surname_space)
                
                if self.count!=self.lenght:
                    self.file.write(str(account.name)+" "+" "*name_space\
                                    +surname+" "+" "*surname_space+str(account.account_num)+\
                       " "+" "*money_space+str(account.account_money)+" "+str(account.account_type)+"\n")
                else:
                    self.file.write(str(account.name)+" "+" "*name_space\
                                    +surname+" "+" "*surname_space+str(account.account_num)+\
                       " "+" "*money_space+str(account.account_money)+" "+str(account.account_type))
                   
            Account.ShowInfo(self)
            
        finally:
            self.file.close()
            
    def ShowInfo(self):
        mb.showinfo("OK!","Output written to Accounts.txt!")

############
    def ShowObjects(self,event,win):
        Interface.OutputWindow(self,event,win)

############
    def CreateObjects(self):
        self.objects=[]
        self.attributes=[]
        del Accounts_table[:]
        
        try:
            self.file=open("Accounts.txt")
            self.txt=self.file.read()

            for obj in self.txt.split("\n"):    
                self.objects.append(obj)

            for obj in self.objects:
                del self.attributes[:]

                self.attributes=obj.split()
                if len(self.attributes)==4: #company
                    account=CompanyAccount(self.attributes[0],self.attributes[1],\
                                           self.attributes[2],self.attributes[3])
                elif len(self.attributes)==5: #private
                    account=PrivateAccount(self.attributes[0],self.attributes[2],\
                                           self.attributes[3],self.attributes[1],self.attributes[4])
                Accounts_table.append(account)

            self.window_input.destroy()
            self.MainMenu()                
            
        finally:
            self.file.close()

############        
class CompanyAccount(Account):
############
    def __init__(self,company_name,account_num,account_money,account_type):
        super().__init__(company_name,account_num,account_money,account_type)

############
class PrivateAccount(Account):
############
    def __init__(self,name,account_num,account_money,surname,account_type):
        super().__init__(name,account_num,account_money,account_type)
        self.surname=surname

############
def Main():
    global Accounts_table
    Accounts_table=[]
    Accounts=Interface()
    Accounts.InputWindow()

############
Main()

##dodac przelewanie z jednego do drugiego

class Calendar:
    #init wczytujacy rok i miesiac
    def __init__(self,rok,miesiac):
        self.rok=rok
        self.miesiac=miesiac
        
    #metoda sprawdzajaca czy podany rok jest przestepny
    def CzyPrzestepny(self):
        if rok%4==0: 
            return True
        else:
            return None
        
    #metoda zwracajaca liczbe dni dla podanego miesiaca
    def LiczbaDni(self):
        if self.miesiac==1 or self.miesiac==3 or self.miesiac==5 or self.miesiac==7 \
           or self.miesiac==8 or self.miesiac==10 or self.miesiac==12:
            return 31
        elif self.miesiac==2 and self.CzyPrzestepny()==True:
            return 29
        elif self.miesiac==2 and self.CzyPrzestepny()==None:
            return 28
        elif self.miesiac==4 or self.miesiac==6 or self.miesiac==9 or self.miesiac==11:
            return 30

    #metoda zwracajaca ktorym dniem tygodnia jest 1 dzien podanego miesiaca
    def DzienTygodnia(self):

        miesiac=self.miesiac
        rok=self.rok
        
        #krok 1
        miesiac=miesiac-2

        #krok 2
        if miesiac<=0:
            miesiac=miesiac+12
            rok=rok-1

        #krok 3
        self.wynik=(83*miesiac)//32

        #krok 4
        self.wynik=self.wynik+1

        #krok 5
        self.wynik=self.wynik+rok

        #krok 6
        self.wynik=self.wynik+(rok//4)

        #krok 7
        self.wynik=self.wynik-(rok//100)

        #krok 8
        self.wynik=self.wynik+(rok//400)

        self.wynik=self.wynik%7

        return self.wynik
    
    #metoda zwracajaca slownie nazwe pierwszego dnia podanego miesiac
    def NazwaDnia(self):
        if self.wynik==0:
            return "Podany miesiac zaczyna sie w niedziele.\n"
        elif self.wynik==1:
            return "Podany miesiac zaczyna sie w poniedzialek.\n"
        elif self.wynik==2:
            return "Podany miesiac zaczyna sie we wtorek.\n"
        elif self.wynik==3:
            return  "Podany miesiac zaczyna sie w srode.\n"
        elif self.wynik==4:
            return  "Podany miesiac zaczyna sie w czwartek.\n"
        elif self.wynik==5:
            return "Podany miesiac zaczyna sie w piatek.\n"
        elif self.wynik==6:
            return "Podany miesiac zaczyna sie w sobote.\n"

    def NazwaMiesiaca(self):
        if self.miesiac==1:
            return "STYCZEN\n".center(20)
        elif self.miesiac==2:
            return "LUTY\n".center(20)
        elif self.miesiac==3:
            return "MARZEC\n".center(20)
        elif self.miesiac==4:
            return "KWIECIEN\n".center(20)
        elif self.miesiac==5:
            return "MAJ\n".center(20)
        elif self.miesiac==6:
            return "CZERWIEC\n".center(20)
        elif self.miesiac==7:
            return "LIPIEC\n".center(20)
        elif self.miesiac==8:
            return "SIERPIEN\n".center(20)
        elif self.miesiac==9:
            return "WRZESIEN\n".center(20)
        elif self.miesiac==10:
            return "PAZDZIERNIK\n".center(20)
        elif self.miesiac==11:
            return "LISTOPAD\n".center(20)
        elif self.miesiac==12:
            return "GRUDZIEN\n".center(20)

    #glowna metoda pokazujaca liczbe dni dla danego miesiaca w blokach po 7 dni    
    def Miesiac(self):

        CalTab=[]
        
        if self.wynik==0:
            index=6
        else:
            index=self.wynik-1
            
        for z in range(index):
            CalTab.append(" ")
                   
        dzien=1
        liczba_dni=self.LiczbaDni()

        for z in range (liczba_dni):
            CalTab.append(dzien)
            dzien+=1
       
        for z in range(len(CalTab)):
            
            if CalTab[z]==" ":
                print (str(CalTab[z]),end="  ")

            elif int(CalTab[z])<=9:
                print(" "+str(CalTab[z]),end=" ")
            else:
                print(str(CalTab[z]),end=" ")
            dzien+=1

            if z==6 or z==13 or z==20 or z==27 or z==34:

                print("\n"+"-"*20)
                
#glowna petla programu                
while True:
    try:
        rok=int(input("Podaj rok:"))
        
    except ValueError:
        print("Rok musi byc wartoscia liczbowa!")
        break
    
    try:
        while True:
            miesiac=int(input("\nPodaj miesiac:"))

            if miesiac>=1 and miesiac<=12:
                break
            else:
                print("Miesiac musi byc z zakresu 1-12, jeszcze raz...")

    except ValueError:
        print("Miesiac musi byc wartoscia liczbowa!")
        break
    
    try:
        while True:
            wybor=int(input("\nWyswietlic kalendarz dla:\n1-caly rok\n2-tylko wybrany miesiac\nTwoj wybor (1 lub 2):"))

            if wybor==1 or wybor==2:
                break
            else:
                print("\nPodaj 1 lub 2, jeszcze raz...")
                
    except ValueError:
        print("Twoj wybor musi byc wartoscia liczbowa!")
        break

    if wybor==1:

        Cal=Calendar(rok,1)

        if Cal.CzyPrzestepny()==True:
            print("\nPodany rok jest przestepny!\n")

        print("Kalendarz danego roku:\n")

        for z in range (12):

            Cal.DzienTygodnia()
   
            print("\n\n"+Cal.NazwaMiesiaca())

            print("pn wt sr cz pt sb nd")

            print("-"*20)
    
            Cal.Miesiac()

            Cal.miesiac+=1

        break

    elif wybor==2:

        Cal=Calendar(rok,miesiac)

        if Cal.CzyPrzestepny()==True:
            print("\nPodany rok jest przestepny!\n")

        Cal.DzienTygodnia()

        print(Cal.NazwaDnia())

        print("Kalendarz danego miesiaca:\n")
    
        print(Cal.NazwaMiesiaca())

        print("pn wt sr cz pt sb nd")

        print("-"*20)
    
        Cal.Miesiac()
        
        break

class Planets:
    def __init__(self, name, distance, question):
        self.name=name
        self.distance=distance
        self.question=question

    def Create(self,ex):
        self.ex=ex
        au=149597870700
        if ex==0:
            return "[ "+str(self.name).center(10)+str(self.distance*au).center(15)+" "+str(self.question).center(5)+" ]"
        elif ex==1:
            return "[ "+str(self.name).center(10)+str(self.distance).center(15)+" "+str(self.question).center(5)+" ]"


planet_name=["Wulkan","Merkury","Wenus","Ziemia","Mars","Faeton",
             "Jowisz","Saturn","Uran","Neptun","Pluton"]

planet_distance=[0.03,0.38,0.72,1.0,1.52,2.7,5.2,9.53,19.19,30.06,39.48]

planet_question=[False,True,True,True,True,False,True,True,True,True,False]

planets=[]

planets_true=[]

planets_false=[]

objects=[]

#Main function
def Main():
        
    for k in range (11):
        x=Planets(planet_name[k],planet_distance[k],planet_question[k])
        planets.append(x.Create(0))

        if planet_question[k]==True:
            planets_true.append(x.Create(0))
        elif planet_question[k]==False:
            planets_false.append(x.Create(0))

    Show(0)

    Write()

    Read()

    CreateFromFile()

#Show all objects
def Show(ex):

    if ex==0:

        print("Wszystkie:")
    
        for k in range(len(planets)):
            print(planets[k])

        print("\nPrawdziwe:")

        for k in range(len(planets_true)):
            print(planets_true[k])

        print("\nNieprawdziwe:")

        for k in range(len(planets_false)):
            print(planets_false[k])

    elif ex==1:

        print("\nUtworzone z pliku:")
    
        for k in range(len(planets)):
            print(planets[k])

#Write true planets to txt file        
def Write():
    file=open("planets.txt","w")
    try:
        file.write("Prawdziwe:\n")
        for k in range(len(planets_true)):
            file.write(str(planets_true[k])+"\n")
    finally:
        file.close()

#Read objects from txt file
def Read():
    file=open("planets.txt")
    try:
        txt=file.read()
    finally:
        file.close()

    for k in txt.split():
       if k!="Prawdziwe:" and k!="[" and k!="]":     
            objects.append(k)

#Create objects from txt file
def CreateFromFile():
    choice=str(input("\nCreate new objects from exported file? (y/n)"))
    if choice=="y":
        del planets[:]
        step=[0,3,6,9,12,15,18,21]

        for k in step:
            x=Planets(objects[k],float(objects[k+1]),objects[k+2])
            planets.append(x.Create(1))
            
        Show(1)
    else:
        pass

#Main function                   
Main()


             

# rodičovská třída
class Bird:
    #vypisujici 
    def __init__(self):
        print("Bird je připraven")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Plav rychleji")

# child třída
class Penguin(Bird):
  #vypisujici funkce ktere jsou na sobě zavisle
    def __init__(self):
        # zavolá super() funkci
        super().__init__()
        print("Penguin je připraven") 

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("útíkej rychleji")
#tato část volá funkce viz níže
peggy = Penguin() 
peggy.whoisThis()
peggy.swim()
peggy.run()
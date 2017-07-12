class Taco():
        def __init__(self,meat,topping):
            self.meat = "meat"
            self.topping = "topping"
        def makeTaco(self):
            print("Tsss")
            print("Ready")

userInput=0
tacoList={1,2}
menu="1.Make a taco \n 2.Finish"

while(userInput !="2" ):
    print(menu)
    userInput = input("What would you like?")
    if'(userInput="1")':
        userInput = input("What topping would you like?")
        userInput = input("What meat would you like?")



    myTaco = Taco("Asada","Cilantro",)
print(myTaco.meat)
print(myTaco.topping)
myTaco.makeTaco()

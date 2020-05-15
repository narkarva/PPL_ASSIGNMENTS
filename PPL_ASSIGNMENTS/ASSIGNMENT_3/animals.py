class cat:
    def __init__(self, c="black"):
        self.__legs = 4
        self.__eyes = 2
        self.__eyecolor = c
    def set_furcolor(self, c):
        self.__furcolor = c
    def get_furcolor(self):
        return self.__furcolor
    def set_legs(self, n = 4):
        self.__legs = n
    def get_legs(self):
        return self.__legs
    def get_eyecolor(self):
        return self.__eyecolor
    def speak(self):
        print("Meow")
    def walk(self):
        print("It can climb the trees")
    def eat(self):
        print("It chases mice and eats them") 
class dog:
    def __init__(self, c="brown"):
        self.__legs = 4
        self.__eyes = 2
        self.__furcolor = c
    def setEyecolor(self, c = "brown"):
        self.__eyecolor = c
    def set_legs(self, n):
        self.__legs = n
    def get_legs(self):
        return self.__legs
    def get_eyecolor(self):
        return self.__eyecolor
    def get_furcolor(self):
        return self.__furcolor
    def speak(self):
        print("Bark")
    def eat(self):
        print("It eats bones , grass, fruits, meat")
class tiger:
    def __init__(self, c = "brownish orange"):
        self.__color = c
        self.__eyes = 2
        self.__legs = 4
        if c == "white":
            self.__eyecolor = "blue"
        else:
            self.__eyecolor = "brown"            
    def setEyecolor(self, e):
        self.__eyecolor = e
    def getEyecolor(self):
        return self.__eyecolor
    def speak(self):
        print("Roar")
    def set_legs(self, n):
        self.__legs = n
    def get_legs(self):
        return self.__legs
    def eat(self):
        print("Eats large and medium sized mammals like deer, barshinga")
    def getColor(self):
        return self.__color
class whale:
    def __init__(self, c = "blue"):
        self.__color = c
        self.__eyecolor = "blue"
        self.__fins = 4
    def setEyecolor(self, e):
        self.__eyecolor = e
    def getEyecolor(self):
        return self.__eyecolor
    def speak(self):
        print("They speak through ultrasonic sound")
    def swim(self):
        print("They can swim")
    def breathe(self):
        print("They can't breath underwater like fish and instead breath air into their lungs")
    def getColor(self):
        return self.__color
    def getFins(self):
        return self.__fins
    def speak():
        print("Sing")
class parrot:
    def __init__(self, c = "green"):
        self.__color = c
        self.__wings = 2
        self.__beakcolor = "red"
        self.__legs = 2
        self.__wingscolor = "green"
    def speak(self):
        print("Mithu Mithu")
    def setBeakColor(self, b):
        self.__beakcolor = b
    def getBeakColor(self):
        return self.__beakcolor
    def getWings(self):
        return self.__wings
    def setWingsColor(self, w):
        self.__wingscolor = w
    def getWingsColor(self):
        return self.__wingscolor
    def getColor(self):
        return self.__color
class fox:
    def __init__(self, c = "red"):
        self.__color = c
        self.__eyes = 2
        self.__legs = 4
    def getLegs(self):
        return self.__legs
    def setLegs(self, c = 4):
        self.__legs = c
    def setFurcolor(self, c = "brownish red"):
        self.__furcolor = c
    def getFurcolor(self):
        return self.__furcolor
    def speak(self):
        print("bark or yelp")
    def getColor(self):
        return self.__color
    def setEyecolor(self, c = "brown"):
        self.__eyecolor = c
    def getEyecolor(self):
        return self.__eyecolor
    def eat(self):
        print("It eats fruits, grass, rabbits, mice")
class monkey:
    def __init__(self, c = "brown"):
        self.__hands = 2
        self.__furcolor = c
        self.__eyes = 2
        self.__legs = 2
    def speak(self):
        print("chatter or gibber or whop")
    def set_legs(self, n):
        self.__legs = n
    def get_legs(self):
        return self.__legs
    def get_hands(self):
        return self.__hands
    def get_furcolor(self):
        return self.__furcolor
    def set_eyecolor(self, c = "black"):
        self.__eyecolor = c
    def get_eyecolor(self):
        return self.__eyecolor
    def eat(self):
        print("It eats nuts, fruits, seeds, bird's eggs, small lizards, insects")
class horse:
    def __init__(self, c = "black"):
        self.__legs = 4
        self.__eyes = 2
        self.__coatcolor = c
    def get_legs(self):
        return self.__legs
    def get_coatcolor(self):
        return self.__coatcolor
    def eat(self):
        print("It eats mainly grass and also eat fruits and vegetables")
    def vision(self):
        print("It has range of vision more than 350 degrees")
    def set_legs(self, n):
        self.__legs = n
    def speak(self):
        print("Neigh or snort")
class chimpanzee:
    def __init__(self, c = "black"):
        self.__legs = 2
        self.__hands = 2
        self.__eyes = 2
        self.__haircolor = c
    def get_legs(self):
        return self.__legs
    def get_haircolor(self):
        return self.__furcolor
    def set_eyecolor(self, c):
        self.__eyecolor = c
    def get_eyecolor(self):
        return self.__eyecolor
    def get_eyes(self):
        return self.__eyes
    def set_eyes(self, n):
        self.__eyes = n
    def genes(self):
        print("It has most similarity that is 99% between it's genes and human's genes")
    def get_hands(self):
        return self.__hands
    def eat(self):
        print("It eats insects, bark, eggs, nuts, and wide variety of fruits")
    def speak(self):
        print('It uses great ape that is sign language to communicate with other chimpanzees and humans')
class donkey:
    def __init__(self, c = "gray"):
        self.__eyes = 2
        self.__legs = 4
        self.__coatcolor = c
    def set_legs(self, n):
        self.__legs = n
    def get_legs(self):
        return self.__legs
    def get_coatcolor(self):
        return self.__coatcolor
    def eat(self):
        print("It eats barley straw, hay, grass, molasses, sugar beet and some fruits like apples")
    def work(self):
        print("It is used for transportation work like pulling a carriage ,also to sire mules, and to guard sheep")
  

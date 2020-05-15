class circle() :
    def __init__(self, n = 10):
        self.__r = n
    def getArea(self):
        return 3.14 * self.__r * self.__r
    def getCircumference(self):
        return 2 * 3.14 * self.__r
    def draw(self):
        print("Draw a circle with radius", self.__r)
        import turtle
        turtle.circle(self.__r)
class square():
    def __init__(self, n = 15):
        self.__s = n
    def perimeter(self):
        return 4 * self.__s
    def area(self):
        return self.__s * self.__s
    def draw(self):
        print("Draw square  with side", self.__s)
        import turtle
        a = [(self.__s, 0), (self.__s, self.__s), (0, self.__s), (0, 0)]
        for i in a:
            turtle.goto(i)
class rectangle():
    def __init__(self, i = 15, j = 10):
        self.__l = i
        self.__b = j
    def perimeter(self):
        return 2 * (self.__l + self.__b)
    def area(self):
        return self.__l * self.__b
    def draw(self):
        a = [(self.__l, 0), (self.__l, self.__b), (0, self.__b), (0, 0)]
        import turtle
        for i in a:
            turtle.goto(i)
class pentagon:
    def __init__(self, n = 20):
        self.__side = n
    def get_perimeter(self):
        return 5 * self.__side
    def get_area(self):
        import math
        return (5 * (self.__side ** 2)) / (4 * math.tan(math.pi / 5))
    def draw(self):
        import turtle
        print("Draw regular pentagon with side", self.__side)
        for i in range(5):
            turtle.forward(self.__side)
            turtle.right(-72)
class hexagon:
    def __init__(self, n = 20):
        self.__side = n
    def get_perimeter(self):
        return 6 * self.__side
    def get_area(self):
        import math
        return (6 * (self.__side ** 2)) / (4 * math.tan(math.pi / 6))
    def draw(self):
        import turtle
        i = 0
        while i < 6:
            turtle.forward(self.__side)
            turtle.right(-60)
            i += 1
class equilateral_triangle:
    def __init__(self, n = 20):
        self.__side = n
    def get_perimeter(self):
        return 3 * self.__side
    def get_area(self):
        import math
        return ((math.sqrt(3) * math.pow(self.__side, 2)) / 4 )
    def draw(self):
        import turtle
        for i in range(0, 3):
            turtle.forward(self.__side)
            turtle.left(120)
class octagon:
	def __init__(self, n = 20):
		self.__side = 20
	def get_perimeter(self):
		return 8 * self.__side
	def get_area(self):
		import math
		return (8 * (self.__side ** 2)) / (4 * math.tan(math.pi / 8))
	def draw(self):
		import turtle
		for i in range(0, 8):
			turtle.forward(self.__side)
			turtle.right(-45)
class decagon:
	def __init__(self, n = 20):
                self.__side = n
	def get_perimeter(self):
		return 10 * self.__side
	def get_area(self):
                import math
                return (10 * (self.__side ** 2)) / (4 * math.tan(math.pi / 10))
	def draw(self):
		import turtle
		for i in range(0, 10):
			turtle.forward(self.__side)
			turtle.right(-36)
class right_angled_triangle:
        def __init__(self, i = 7, j = 24):
            self.__side1 = i
            self.__side2 = j
            self.__hypotenuse = ((i ** 2) + (j ** 2)) ** 0.5
        def get_perimeter(self):
            return (self.__side1 + self.__side2 + self.__hypotenuse)
        def get_area(self):
            return (0.5 * self.__side1 * self.__side2)
        def draw(self):
            import turtle
            a = [(self.__side1, 0), (0, self.__side2), (0,0)]
            for i in a:
                turtle.goto(i)
class isosceles_right_angled_triangle:
        def __init__(self, n = 20):
            self.__side = n
            self.__hypotenuse = (2 ** 0.5) * n
        def get_perimeter(self):
            return (2 + 2 ** 0.5) * self.__side
        def get_area(self):
            return (0.5 * self.__side ** 2)
        def draw(self):
            import turtle
            a = [(self.__side, 0), (0, self.__side), (0,0)]
            for i in a:
                turtle.goto(i)


#A class for soft drinks
class softdrinks:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def name(self):
        print("This is:", self.brand)
        print("An example of a size is:", self.size)

fanta = softdrinks("fanta", "350ml")
fanta.name()

cocacola = softdrinks("Coca Cola","500ml")
cocacola.name()


#class 2
class cars:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def car(self):
        print("This is a:", self.brand)
        print("An exaple of a price:", self.price)

Mazda = cars("Mazda", "110,130,000")
Mazda.car()

Audi = cars("Audi", "158,025,000")
Audi.car()


#class 3
class phones:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def phone(self):
        print("This is a:", self.brand)
        print("An exaple of a model:", self.model)

Tecno = phones("Tecno", "Camon 30 Pro")
Tecno.phone()


#class 4
class universities:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def university(self):
        print("This is:", self.name)
        print("An exaple of a course:", self.course)

AfricanLeadershipUniversity = universities("African Leadership University", "Bachelor of Software Engineering")
AfricanLeadershipUniversity.university()


#class 5
class clothes:
    def __init__(self, types, name):
        self.types = types
        self.name = name

    def cloth(self):
        print("This type is called:", self.types)
        print("An exaple is:", self.name)

Swimwear = clothes("Swimwear", "Bikinis")
Swimwear.cloth()



class Factory:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Bear_Toy(Factory):
    def __init__(self, name, color, type):
        Factory.__init__(self, name, color)
        self.type = type

    def toy(self):
        return " Bear Toy\n Name: {}\n Color: {}\n Type: {}\n".format(self.name, self.color, self.type)

    def purchase_of_silk(self):
        return "\n We go to the store and buy silk\n"

    def tailoring(self):
        return " Then we take the needle and when we have sewn the base, we push it into the silk\n"

    def dyeing(self):
        return " Now we paint in blue-yellow\n"

    def end(self):
        return " That's all our toy is ready\n"


class Toy_Planet(Factory):
    def __init__(self, name, color, type):
        Factory.__init__(self, name, color)
        self.type = type

    def toy(self):
        return " Toy Planet\n Name: {}\n Color: {}\n Type: {}\n".format(self.name, self.color, self.type)

    def purchase_of_cloth(self):
        return " \nWe go to the store and buy cloth\n"

    def tailoring(self):
        return " Then we take a needle and sew\n"

    def dyeing(self):
        return " Now we will color the planet Earth\n"

    def end(self):
        return " That's all our toy is ready\n"


class Toy_Rabbit(Factory):
    def __init__(self, name, color, type):
        Factory.__init__(self, name, color)
        self.type = type

    def toy(self):
        return " Toy Rabbit\n Name: {}\n Color: {}\n Type: {}\n".format(self.name, self.color, self.type)

    def purchase_of_silk(self):
        return " \nWe go to the store and buy silk\n"

    def tailoring(self):
        return " Then we take the needle and when we have sewn the base, we push it into the silk\n"

    def dyeing(self):
        return " Now we paint in White-Black\n"

    def end(self):
        return " That's all our toy is ready\n"


class Air_Layer_Toy(Factory):
    def __init__(self, name, color, type):
        Factory.__init__(self, name, color)
        self.type = type

    def toy(self):
        return " Air Layer Toy\n Name: {}\n Color: {}\n Type: {}\n".format(self.name, self.color, self.type)

    def purchase_of_plasma_and_cloth(self):
        return " \nWe go to the store and buy cloth and plastic\n"

    def tailoring_and_melting(self):
        return " Then we take a needle and sew, and then melt\n"

    def dyeing(self):
        return " Now we paint in White-Blue-Green\n"

    def end(self):
        return " That's all our toy is ready\n"


class Man_Toy(Factory):
    def __init__(self, name, color, type):
        Factory.__init__(self, name, color)
        self.type = type

    def toy(self):
        return " Man Toy\n Name: {}\n Color: {}\n Type: {}\n".format(self.name, self.color, self.type)

    def purchase_of_plasma(self):
        return " \nWe go to the store and buy plastic\n"

    def melting(self):
        return " Then we melt it\n"

    def dyeing(self):
        return " Now we paint in White\n"

    def end(self):
        return " That's all our toy is ready\n"


Bear = Bear_Toy("Bear", "Blue-Yellow", "Silk")
Planet = Toy_Planet("Planet", "The color of planet earth", "The cloth")
Rabbit = Toy_Rabbit("Rabbit", "White-Black", "Silk")
AirLayer = Air_Layer_Toy(
    "Air Layer", "White-Blue-Green", "Silk-Plasma-The cloth")
Man = Man_Toy("Man", "White", "Plasma")
print(Bear.toy(), Bear.purchase_of_silk(),
      Bear.tailoring(), Bear.dyeing(), Bear.end())
print(Planet.toy(), Planet.purchase_of_cloth(),
      Planet.tailoring(), Planet.dyeing(), Planet.end())
print(Rabbit.toy(), Rabbit.purchase_of_silk(),
      Rabbit.tailoring(), Rabbit.dyeing(), Rabbit.end())
print(AirLayer.toy(), AirLayer.purchase_of_plasma_and_cloth(),
      AirLayer.tailoring_and_melting(), AirLayer.dyeing(), AirLayer.end())
print(Man.toy(), Man.purchase_of_plasma(),
      Man.melting(), Man.dyeing(), Man.end())

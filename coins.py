import random
class Coin:
    def __init__(self,rare=False,clean=True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        if self.is_rare:
            self.value = 1.25*self.original_value
        else:
            self.value = self.original_value
        
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    # def __del__(self):
    #     print("Coin Spent")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice
        print('Coin is flipped successfully')

    def __str__(self):
        if self.original_value >= 1:
            return "$()coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))

class One_Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_colour":"Silver",
            "rusty_colour":"Brownish",
            "num_edges" : 1,
            "diameter" : 22.5,
            "thickness" : 2.85,
            "mass" : 9.5
        }
        super().__init__(**data)

class Two_Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":2.00,
            "clean_colour":"Silver",
            "rusty_colour":"Brownish",
            "num_edges" : 1,
            "diameter" : 26.5,
            "thickness" : 2.15,
            "mass" : 12.5
        }
        super().__init__(**data)

class Five_Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":5.00,
            "clean_colour":"Gold",
            "rusty_colour":"None",
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 3.15,
            "mass" : 15.5
        }
        super().__init__(**data)

class Ten_Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":10.00,
            "clean_colour":"Gold",
            "rusty_colour":"None",
            "num_edges" : 1,
            "diameter" : 30.5,
            "thickness" : 3.15,
            "mass" : 18.5
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

class Twenty_Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":20.00,
            "clean_colour":"Gold",
            "rusty_colour":"Reddish",
            "num_edges" : 1,
            "diameter" : 32.5,
            "thickness" : 3.15,
            "mass" : 20.5
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

class Fifty_Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":50.00,
            "clean_colour":"Ocean-Blue",
            "rusty_colour":"Greenish",
            "num_edges" : 1,
            "diameter" : 32.5,
            "thickness" : 3.55,
            "mass" : 22.5
        }
        super().__init__(**data)

class Hundred_Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":100.00,
            "clean_colour":"Green",
            "rusty_colour":"Brownish",
            "num_edges" : 1,
            "diameter" : 32.5,
            "thickness" : 3.85,
            "mass" : 25.5
        }
        super().__init__(**data)

coins = [One_Rupee(),Two_Rupee(),Five_Rupee(),Ten_Rupee(),Twenty_Rupee(),Fifty_Rupee(),Hundred_Rupee()]

for coin in coins:
    arguments = [coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.num_edges,coin.mass]

    string = "{}-Colour:{},value:{},diameter(mm):{},thickness(mm):{},number of edges:{},mass(g):{}".format(*arguments)
    print(string)


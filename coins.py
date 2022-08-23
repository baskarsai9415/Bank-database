import random
class Coin:
    def __init__(self,rare=False,clean=True):
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

    def __del__(self):
        print("Coin Spent")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice
        print('Coin is flipped successfully')

class Ruppee(Coin):
    def __init__(self):
        data = {
            "original_value":1,
            "clean_colour":"Gold",
            "rusty_colour":"Brownish",
            "num_edges" : 1,
            "diameter" : 22.5,
            "thickness" : 3.15,
            "mass" : 9.5
        }
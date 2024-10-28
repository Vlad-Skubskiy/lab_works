class Shoes():
    def __init__(self, price = 154, size = 9, color = 'Black', brand_model = 'AirJordan'):
        self.__price = int(price)
        self.__size = size
        self.__color = color
        self.__brand_model = brand_model
        
        self.texture = 'textile'
        self.sole_height = 3
               
    def get_price(self):
        return self.__price

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color
    
    def set_price(self):
        print(self.__price)     
    
    
    
    def __str__(self):
        return f"the texture of this shoes is {self.texture}, and this sole height is {self.sole_height}"

    def __repr__(self):
        return (
            f"brand_model: {self.__brand_model}\n"
            f"price: {self.__price}\n"
            f"size: {self.__size}\n"
            f"color: {self.__color}\n"
            f"textrue: {self.texture}\n"
            f"sole_height: {self.sole_height}\n"            
        )
        """
    def __del__(self):
    
        print('class park deleted')
        """
def main():
    Nike = Shoes(150, 8, 'Black', 'AirJordan')
    Adidas = Shoes(100, 8, 'White', 'Campus')
    NewBalance = Shoes(80, 11, 'Red', 'Z-102')
    print(repr(Nike))
    print(repr(Adidas))
    print(repr(NewBalance))

main()
Nike = Shoes(150, 8, 'Black', 'AirJordan')
Adidas = Shoes(100, 8, 'White', 'Campus')
NewBalance = Shoes(80, 11, 'Red', 'Z-102')
list = [
    Shoes(150, 8, 'Black', 'AirJordan'),
    Shoes(100, 8, 'White', 'Campus'),
    Shoes(80, 7, 'Red', 'Z-102')
]

def find_best_shoes():

    best_shoe = list[0]
    
    for shoe in list:   
        if (shoe.get_size() > best_shoe.get_size()) or ((shoe.get_size() == best_shoe.get_size()) and shoe.get_price() < best_shoe.get_price()):
            best_shoe = shoe
    return print(repr(best_shoe))
find_best_shoes()

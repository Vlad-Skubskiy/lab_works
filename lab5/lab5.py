from enum import Enum

class Clothing():
    def __init__(self, name=None, description=None, location=None, colour=None, size=None):
        self.name = name
        self.description = description
        self.location = location
        self.colour = colour
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size})"

class ClothingType(Enum):
    SHIRT = "Shirt"
    JEANS = "Jeans"
    JACKET = "Jacket"
    SKIRT = "Skirt"

class Wardrobe():
    def __init__(self, shirt, jeans, jacket, skirt):
        self.clothes = [shirt, jeans, jacket, skirt]
            
    def go_out(self):
        count_of_clothingtype = len(ClothingType)
        if count_of_clothingtype > 3:
            print("Готова вийти")
        else:
            print("Не готова вийти")
                
    def clothes_size_sort(self):  
        size_chart = ["XS", "S", "M", "L", "XL", "XXL"]
        sorted_clothes = []
        
        for size in size_chart:
            for item in self.clothes:
                if item.size == size:
                    sorted_clothes.append(item)

        self.clothes = sorted_clothes
                              
    def __str__(self):
        clothes_info = ""
        for item in self.clothes:
            clothes_info += str(item) + "\n"
        return f"In the wardrobe you can find:\n{clothes_info}"


shirt = Clothing("Casual Shirt", "A plain casual shirt", "Wardrobe", "Blue", "M")
jeans = Clothing("Skinny Jeans", "A pair of skinny jeans", "Wardrobe", "Black", "L")
jacket = Clothing("Leather Jacket", "A stylish leather jacket", "Wardrobe", "Brown", "M")
skirt = Clothing("Pleated Skirt", "A pleated skirt", "Wardrobe", "Red", "S")


wardrobe = Wardrobe(shirt, jeans, jacket, skirt)

wardrobe.clothes_size_sort() 
print(wardrobe)  
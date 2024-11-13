from enum import Enum

class Clothing():
    def __init__(self, name=None, description=None, location=None, colour=None, size=None, price=None, type=None):
        self.name = name
        self.description = description
        self.location = location
        self.colour = colour
        self.size = size
        self.price = price
        self.type = type
        
    def __str__(self):
        return f"{self.name} ({self.size}, {self.price}$)"

class ClothingType(Enum):
    SHIRT = "Up Clothes"
    JEANS = "Down Clothes"
    JACKET = "Up Clothes"
    SKIRT = "Down Clothes"
    DOWN_JACKET = "Up Clothes"
    OVERCOAT = "Up Clothes"
    TSHIRT = "Up Clothes"
    SWEATER = "Up Clothes"
    BLAZER = "Up Clothes"
    JOGGERS = "Down Clothes"
    LONGSLEEVE = "Up Clothes"
    
class Wardrobe():
    def __init__(self, shirt, jeans, jacket, skirt, down_jacket, overcoat, tshirt, sweater, blazer, joggers, longsleeve):
        self.clothes = [shirt, jeans, jacket, skirt, down_jacket, overcoat, tshirt, sweater, blazer, joggers, longsleeve]
            
    def go_out(self):
        count_of_clothingtype = len(ClothingType)
        if count_of_clothingtype > 3:
            print("Готова вийти \n")
        else:
            print("Не готова вийти \n")
                
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

    def pick_outfit(self):   
        self.clothes_size_sort()
        look_options = {}
        for item in self.clothes:
            if item.size not in look_options:
                look_options[item.size] = []
            look_options[item.size].append(item)

        for size, items in look_options.items():
            if len(items) < 2:
                continue

            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    first_clothes = items[i]
                    second_clothes = items[j]
                    if first_clothes.type != second_clothes.type:
                        print("Selected Look:")
                        print(f"First clothes: {first_clothes}")
                        print(f"Second clothes: {second_clothes} \n")

    def find_cheapest_look(self):
        cheapest_look = None
        min_price = 10000000000000000000000 
        
        for i in range(len(self.clothes)):
            for j in range(i + 1, len(self.clothes)):
                first_clothes = self.clothes[i]
                second_clothes = self.clothes[j]
                
                if first_clothes.type != second_clothes.type:
                    total_price = first_clothes.price + second_clothes.price
                    
                    if total_price < min_price:
                        min_price = total_price
                        cheapest_look = (first_clothes, second_clothes)
        
        if cheapest_look:
            print("Cheapest Look:")
            print(f"First Item: {cheapest_look[0]}")
            print(f"Second Item: {cheapest_look[1]}\n")
    
    def find_most_expensive_look(self):
        most_expensive_look = None
        max_price = 0 
        
        for i in range(len(self.clothes)):
            for j in range(i + 1, len(self.clothes)):
                first_clothes = self.clothes[i]
                second_clothes = self.clothes[j]
                
                if first_clothes.type != second_clothes.type:
                    total_price = first_clothes.price + second_clothes.price
                    
                    if total_price > max_price:
                        max_price = total_price
                        most_expensive_look = (first_clothes, second_clothes)
        
        if most_expensive_look:
            print("Most Expensive Look:")
            print(f"First Item: {most_expensive_look[0]}")
            print(f"Second Item: {most_expensive_look[1]}\n")
            

Shirt = Clothing("Casual Shirt", "A plain casual shirt", "Wardrobe", "Blue", "M", 100, ClothingType.SHIRT)
Jeans = Clothing("Skinny Jeans", "A pair of skinny jeans", "Wardrobe", "Black", "L", 50, ClothingType.JEANS)
Jacket = Clothing("Leather Jacket", "A stylish leather jacket", "Wardrobe", "Brown", "M", 43, ClothingType.JACKET)
Skirt = Clothing("Pleated Skirt", "A pleated skirt", "Wardrobe", "Red", "S", 53, ClothingType.SKIRT)
Down_jacket = Clothing("Winter Down Jacket", "Warm down jacket for winter", "Wardrobe", "Dark Blue", "L", 76, ClothingType.DOWN_JACKET)
Overcoat = Clothing("Classic Overcoat", "A refined wool overcoat", "Wardrobe", "Gray", "XL", 51, ClothingType.OVERCOAT)
Tshirt = Clothing("Cotton T-shirt", "A cool cotton T-shirt", "Wardrobe", "Black", "L", 10, ClothingType.TSHIRT)
Sweater = Clothing("Wool Sweater", "Soft wool sweater for winter", "Wardrobe", "Green", "M", 24, ClothingType.SWEATER)
Blazer = Clothing("Formal Blazer", "A formal blazer for events", "Wardrobe", "Navy Blue", "L", 78, ClothingType.BLAZER)
Joggers = Clothing("Comfort Joggers", "Casual joggers for lounging", "Wardrobe", "Gray", "M", 98, ClothingType.JOGGERS)
Longsleeve = Clothing("Thin Longsleeve", "Pretty good Longsleeve", "Wardrobe", "White with floral", "S", 120, ClothingType.LONGSLEEVE)

wardrobe = Wardrobe(Shirt, Jeans, Jacket, Skirt, Down_jacket, Overcoat, Tshirt, Sweater, Blazer, Joggers, Longsleeve)

wardrobe.go_out()
wardrobe.clothes_size_sort() 
print(wardrobe)
wardrobe.pick_outfit()
wardrobe.find_cheapest_look()
wardrobe.find_most_expensive_look()

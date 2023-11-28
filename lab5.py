class Sneakers:
    
    def __init__(self, brand, size, color, price, quantity, material, numberOfSales):

        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.numberOfSales = numberOfSales

    def __str__(self):

        return f"{self.brand} - Size: {self.size}, Color: {self.color}, Price: {self.price}, Quantity: {self.quantity}, Material: {self.material}, Sales: {self.numberOfSales}"


class SportShoesStore:
        
        def __init__(self):
            self.inventory = []

        def add_sneakers(self, sneakers):
            self.inventory.append(sneakers)

        def sort_by_price(self):
            self.inventory = sorted(self.inventory, key = lambda x: x.price)

        def sort_by_quantity(self):
            self.inventory = sorted(self.inventory, key = lambda x: x.quantity, reverse = True)

        def top_sellers(self, top_n = 5):
            self.inventory  = sorted(self.inventory, key = lambda x: x.numberOfSales, reverse = True)[:top_n]

def main():

    store = SportShoesStore()
    number_of_spaces = 100


    sneaker1 = Sneakers("Nike", 10, "Black", 150, 50, "Leather", 100)
    sneaker2 = Sneakers("Adidas", 9, "White", 120, 30, "Mesh", 80)
    sneaker3 = Sneakers("Asics", 11, "Black", 100, 20, "Synthetic", 120)
    sneaker4 = Sneakers("New Balance", 11, "Green", 100, 20, "Synthetic", 120)
    sneaker5 = Sneakers("Fila", 11, "Red", 100, 20, "Synthetic", 190)
    sneaker6 = Sneakers("Converse", 11, "White", 100, 20, "Synthetic", 120)
    sneaker7 = Sneakers("Puma", 11, "White", 100, 20, "Synthetic", 150)
    sneaker8 = Sneakers("Vans", 11, "White", 100, 20, "Synthetic", 150)
    sneaker9 = Sneakers("Fred Perry", 11, "White", 100, 20, "Synthetic", 160)
    sneaker10 = Sneakers("vans", 11, "White", 100, 20, "Synthetic", 120)


    store.add_sneakers(sneaker1)
    store.add_sneakers(sneaker2)
    store.add_sneakers(sneaker3)
    store.add_sneakers(sneaker4)
    store.add_sneakers(sneaker5)
    store.add_sneakers(sneaker6)
    store.add_sneakers(sneaker7)
    store.add_sneakers(sneaker8)
    store.add_sneakers(sneaker9)
    store.add_sneakers(sneaker10)


    print("*" * number_of_spaces)
    print("INVENTORY BEFORE SORTING: ")
    print("*" * number_of_spaces)

    for sneaker in store.inventory:
        print(sneaker)


    store.sort_by_price()
    print("*" * number_of_spaces)
    print("INVENTORY AFTER SORTING BY PRICE: ")
    print("*" * number_of_spaces)

    for sneaker in store.inventory:
        print(sneaker)


    store.sort_by_quantity()
    print("*" * number_of_spaces)
    print("INVENTORY AFTER SORTING BY QUANTITY: ")
    print("*" * number_of_spaces)

    for sneaker in store.inventory:
        print(sneaker)


    store.top_sallers()
    print("*" * number_of_spaces)
    print("TOP SELLERS: ")
    print("*" * number_of_spaces)

    for sneaker in store.inventory:
        print(sneaker)
        
    print(store)


if __name__ == "__main__":
    main()




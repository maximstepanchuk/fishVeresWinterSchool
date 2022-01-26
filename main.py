class Fish:

    def __init__(self, name: str, price_in_uah_per_kilo: float, origin: str, weight: float):
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.weight = weight

     def __str__(self):
        return self.name + " " + str(self.weight) + " " + str(self.price_in_uah_per_kilo) + " " + self.origin


class FishShop:
    def __init__(self, shop_name: str):
        self.shop_name = shop_name
        self.fish_set = set()

    def add_fish(self, fish_name: str):
        self.fish_set.add(fish_name)

    def get_fish_names_sorted_by_price(self):
        sorted_fishes = sorted(list(self.fish_set), key=lambda fish: fish.price_in_uah_per_kilo)
        return [fish.name for fish in sorted_fishes]

    def sell_fish(self, fish_name: str):
        self.fish_set.remove(fish_name)


fresh = FishShop("fresh")

fresh.add_fish("LOSOS")
fresh.add_fish("FOREL")
fresh.add_fish("HEK")

first_fish = Fish("LOSOS", 17, "England", 56)
second_fish = Fish("FOREL", 7, "Frankivsk",55)
third_fish = Fish("HEK", 12, "England", 28)

















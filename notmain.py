import datetime


class FishInfo:
    def __init__(self, name:str, price_in_uah_per_kilo: float, due_date:datetime, origin: str, catch_date: datetime):
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.due_date = due_date
        self.origin = origin
        self.catch_date = catch_date


class Fish(FishInfo):
    def __init__(self, age_in_month: int, weight: float, name: str, origin: str, catch_date: datetime):
        super().__init__(name, origin, catch_date)
        self.age_in_month = age_in_month
        self.weight = weight


class FishBox():
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime, height: float, width: float,
                 length: float, is_alive: bool):
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length
        self.is_alive = is_alive


class FishShop():
    def __init__(self):
        self.fish_boxes = {}
        self.fresh_fish = {}



    def get_fish_name_sorted_by_price(self):
        pass

    def get_frozen_fish_names_sorted_by_price(self):
        frozen_fish_sorted = []
        for i in self.fish_boxes.values():
            for j in i

    def get_fresh_fish_names_sorted_by_price(self):
        pass


    def add_fish(self, fish:Fish = None, fish_box:FishBox = None):
        if fish:
            if self.fresh_fish.get(fish.name):
                self.fresh_fish[fish.name].append(fish)

            else:
                self.fresh_fish[fish.name] = [fish]

        elif fish_box:
            if self.fish_boxes.get(fish.name):
                self.fish_boxes[fish.name].append(fish)

            else:
                self.fish_boxes[fish.name] = [fish]



    def sell_fish(self, name: str, weight: float, is_fresh:bool, ):
        pass





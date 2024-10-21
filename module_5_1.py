class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to()

    def go_to(new_floor):
        nonlocal number_of_floors
        new_floor = number_of_floors
        for i in range(1, new_floor + 1):
            print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


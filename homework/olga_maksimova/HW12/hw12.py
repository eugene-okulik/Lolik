# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты) цветов
# разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть хранятся
# в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод)

class Flowers():
    def __init__(self, name, cost, avg_life):
        self.name = name
        self.cost = cost
        self.avg_life = avg_life

    def get_name(self):
        pass

    def get_cost(self):
        pass

    def get_avg_life(self):
        pass


class Rose(Flowers):
    def __init__(self, name, cost, avg_life, color, size):
        super().__init__(name, cost, avg_life)
        self.color = color
        self.size = size

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_avg_life(self):
        return self.avg_life


class Pion(Flowers):
    def __init__(self, name, cost, avg_life, color):
        super().__init__(name, cost, avg_life)
        self.color = color

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_avg_life(self):
        return self.avg_life


class Wild(Flowers):
    def __init__(self, name, cost, avg_life, color, size):
        super().__init__(name, cost, avg_life)
        self.color = color
        self.size = size

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_avg_life(self):
        return self.avg_life


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_flowers(self):
        return self.flowers

    def calculate_average_lifetime(self):
        total_time = sum([flower.get_avg_life() for flower in self.flowers])
        return total_time / len(self.flowers)

    def sort_by_life(self):
        self.flowers.sort(key=lambda x: x.get_avg_life())

    def sort_by_cost(self):
        self.flowers.sort(key=lambda x: x.get_cost())

    def search_by_life(self, life):
        result = []
        for flower in self.flowers:
            if flower.get_avg_life() == life:
                result.append(flower)
        return result

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.get_color())


rose = Rose('Red Rose', 10, 7, "Red", "big")
pion = Pion('White pion', 8, 6, "White")
fofget_me_not = Wild('Forget me not', 4, 9, "Blue", "Small")

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(pion)
bouquet.add_flower(fofget_me_not)

print("Average lifetime of the bouquet:", bouquet.calculate_average_lifetime())
print("Flowers sorted by freshness:")
for flower in bouquet.flowers:
    print(flower.get_name())

searched_lifetime = 7
results = bouquet.search_by_life(searched_lifetime)
if results:
    print("Found flowers with lifespan {}".format(searched_lifetime))
else:
    print("No flowers found with lifespan {}".format(searched_lifetime))

bouquet.sort_by_color()
print("\nFlowers sorted by color:")
for flower in bouquet.flowers:
    print(flower.get_name())

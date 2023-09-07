import statistics
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты)
# цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).


class CatalogFlowers:
    def __init__(self, freshness, color, flower_len, cost, day_to_die):
        self.freshness = freshness
        self.color = color
        self.flower_len = flower_len
        self.cost = cost
        self.day_to_die = day_to_die


class FirstFlower(CatalogFlowers):
    name = "Iris"


class SecondFlower(CatalogFlowers):
    name = "Lilia"


class ThirdFlower(CatalogFlowers):
    name = "Piones"


first_flower = FirstFlower(color="white", freshness=True, flower_len=20, cost='5$', day_to_die=5)
second_flower = SecondFlower(color="yellow", freshness=False, flower_len=30, cost='3$', day_to_die=4)
third_flower = ThirdFlower(color="pink", freshness=True, flower_len=15, cost='1$', day_to_die=5)


class Bouquet:
    def __init__(self, flowers: list = None):
        self.flowers = flowers

    def check_when_bouquet_die(self):
        ckeckers_day = statistics.mean([flowers.day_to_die for flowers in self.flowers])
        return ckeckers_day

    def flower_color_in_stock(self, color):
        for flower in self.flowers:
            if color == flower.color:
                return flower.name

    def flower_len_sort(self):
        return sorted(self.flowers, key=lambda flower: flower.flower_len)

    def flower_cost_sort(self):
        return sorted(self.flowers, key=lambda flower: flower.cost)

    def flower_freshness_sort(self):
        return sorted(self.flowers, key=lambda flower: flower.freshness)


bouquet_for_client = Bouquet(flowers=[first_flower, second_flower, third_flower])
print(bouquet_for_client.check_when_bouquet_die())
print(bouquet_for_client.flower_cost_sort())
print(bouquet_for_client.flower_len_sort())
print(bouquet_for_client.flower_freshness_sort())
print(bouquet_for_client.flower_color_in_stock('pink'))

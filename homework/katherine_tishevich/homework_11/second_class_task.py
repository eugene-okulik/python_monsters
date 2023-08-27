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


peonies = CatalogFlowers(freshness=True, color='pink', flower_len=20, cost='5$', day_to_die=5)
tulips = CatalogFlowers(freshness=True, color='pink', flower_len=15, cost='1$', day_to_die=5)
irises = CatalogFlowers(freshness=True, color='white', flower_len=30, cost='3$', day_to_die=3)


class OrchidsFlower(CatalogFlowers):
    big_orchids = CatalogFlowers(freshness=True, color='white', flower_len=25, cost='45$', day_to_die=10)
    medium_orchids = CatalogFlowers(freshness=True, color='black', flower_len=25, cost='35$', day_to_die=4)
    little_orchids = CatalogFlowers(freshness=True, color='white', flower_len=25, cost='15$', day_to_die=15)


class RoseFlower(CatalogFlowers):
    rose_rb = CatalogFlowers(freshness=True, color='white', flower_len=25, cost='7$', day_to_die=7)
    rose_pl = CatalogFlowers(freshness=True, color='black', flower_len=25, cost='10$', day_to_die=2)
    rose_neth = CatalogFlowers(freshness=True, color='white', flower_len=25, cost='30$', day_to_die=3)


class GiozintFlower(CatalogFlowers):
    blue_giozint = CatalogFlowers(freshness=True, color='blue', flower_len=10, cost='16$', day_to_die=3)
    red_giozint = CatalogFlowers(freshness=True, color='red', flower_len=5, cost='11$', day_to_die=5)
    pink_giozint = CatalogFlowers(freshness=True, color='pink', flower_len=7, cost='22$', day_to_die=7)


class BouquetFlowers(CatalogFlowers):
    flowers_list = [peonies, tulips, irises, OrchidsFlower.big_orchids, OrchidsFlower.medium_orchids,
                    OrchidsFlower.little_orchids, RoseFlower.rose_rb, RoseFlower.rose_pl, RoseFlower.rose_neth,
                    GiozintFlower.blue_giozint, GiozintFlower.red_giozint, GiozintFlower.pink_giozint]

    def bouquet_die(self, flowers_list):
        average_cost_flower = flowers_list.get(self.day_to_die)
        print(average_cost_flower / len(flowers_list))

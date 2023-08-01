import statistics


class Flowers:
    def __init__(self, name, age, freshness, length, price):
        self.name = name
        self.age = age
        self.freshness = freshness
        self.length = length
        self.price = price

    def __str__(self):
        return f'{self.name}: freshness {self.freshness}, length {self.length}, price {self.price}'

    # def __repr__(self):
    #     return f'{self.name}: freshness {self.freshness}, length {self.length}, price {self.price}'


class Rose(Flowers):
    color = 'red'


class Camomile(Flowers):
    color = 'white'


class Tulip(Flowers):
    color = 'yellow'


class Orchid(Flowers):
    color = 'purple'


flower_1 = Rose('rose', 5, 'low', 30, 25)
flower_2 = Camomile('camomile', 7, 'high', 20, 15)
flower_3 = Tulip('tulip', 3, 'medium', 25, 20)
flower_4 = Orchid('orchid', 14, 'high', 35, 50)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def define_bouquet_age(self):
        list_of_ages = [flowers.age for flowers in self.flowers]
        bouquet_age = statistics.mean(list_of_ages)
        return bouquet_age

    def sort_flowers_by_freshness(self):
        return sorted(self.flowers, key=lambda flower: flower.freshness)

    def sort_flowers_by_length(self):
        return sorted(self.flowers, key=lambda flower: flower.length)

    def sort_flowers_by_price(self):
        return sorted(self.flowers, key=lambda flower: flower.price)

    def find_flower(self, age):
        for flower in bouquet_1.flowers:
            if age == flower.age:
                return flower.name


bouquet_1 = Bouquet(flowers=[flower_1, flower_2, flower_3, flower_4])

print(bouquet_1.define_bouquet_age())
print(bouquet_1.sort_flowers_by_freshness())
print(bouquet_1.sort_flowers_by_price())
print(bouquet_1.sort_flowers_by_length())
print(bouquet_1.find_flower(7))

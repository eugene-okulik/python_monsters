import random

list_of_results = []
for result in range(15):
    list_of_results.append(random.random())

print(min(list_of_results))
print(max(list_of_results))
print(sum(list_of_results))
print(sum(list_of_results) / len(list_of_results))

## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [item*2 for item in apple_prices]
apple_prices_lowered = [item - 100 for item in apple_prices]

## 5. Counting Female Names ##

name_counts = {}

for item in legislators:
    if item[3] == 'F' and item[-1] > 1940:
        name = item[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = [ value is not None and value > 30 for value in values ]

## 8. Highest Female Name Count ##

max_value = None
for name in name_counts:
    count = name_counts[name]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for key, plant in plant_types.items():
    print(key)
    print(plant)

## 10. Finding the Most Common Female Names ##

top_female_names = [ name for name, count in name_counts.items() if count == 2 ]

## 11. Finding the Most Common Male Names ##

top_male_names = []

male_name_counts = {}

for item in legislators:
    if item[3] == 'M' and item[-1] > 1940:
        name = item[1]
        if name in male_name_counts:
            male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1
 
highest_male_count = None
for k, v in male_name_counts.items():
    if highest_male_count is None or v > highest_male_count:
        highest_male_count = v
        
top_male_names = [ k for k, v in male_name_counts.items() if v == highest_male_count ]
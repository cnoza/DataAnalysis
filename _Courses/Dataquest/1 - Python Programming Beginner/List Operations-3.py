## 2. Parsing the File ##

weather_data = []
f = open('la_weather.csv','r')
data = f.read()
rows = data.split('\n')
weather_data = [row.split(',') for row in rows]

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
weather = [item[1] for item in weather_data]

## 4. Counting the Items in a List ##

count = 0
for item in weather:
    count += 1

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals
    

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
weather_type_found = [ item in new_weather for item in weather_types ]
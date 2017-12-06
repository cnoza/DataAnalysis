## 3. Read the File Into a String ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()

names_list = names.split('\n')
first_five = names_list[:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')

nested_list = [[item.split(',')[0],item.split(',')[1]] for item in names_list]

## 6. Convert Numerical Values ##

print(nested_list[0:5])

numerical_list = [[item[0], float(item[1])]  for item in nested_list]

print(numerical_list[:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = [item[0] for item in numerical_list if item[1] >= 1000]

print(thousand_or_greater[:10])
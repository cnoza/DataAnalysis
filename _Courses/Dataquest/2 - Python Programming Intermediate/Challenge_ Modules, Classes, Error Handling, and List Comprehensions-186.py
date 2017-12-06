## 2. Introduction to the Data ##

# Importing the data
import csv
file = open('nfl_suspensions_data.csv','r')
nfl_suspensions = list(csv.reader(file))
nfl_suspensions = nfl_suspensions[1:]

# Counting the nbr of occuring years
years = {}
for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] +=1
    else:
        years[row_year] = 1

print(years)

## 3. Unique Values ##

unique_teams = set( [ team[1] for team in nfl_suspensions ] )
unique_games = set( [ game[2] for game in nfl_suspensions ] )

print(unique_teams)
print(unique_games)
## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)

## 2. Importing Using An Alias ##

import math as m
root = m.sqrt(33)

## 3. Importing A Specific Object ##

from math import *
root = sqrt(1001)

## 5. The CSV Module ##

import csv

f = open('nfl.csv')
nfl = list(csv.reader(f))

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))

patriots_wins = 0
for item in nfl:
    if item[2]=='New England Patriots':
        patriots_wins += 1
        

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(name):
    nbr = 0
    for item in nfl:
        if item[2]==name:
            nbr +=1
    return nbr

cowboys_wins = nfl_wins('Dallas Cowboys')
falcons_wins = nfl_wins('Atlanta Falcons')
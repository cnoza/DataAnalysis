## 1. Introduction ##

SELECT COUNT(Major) FROM recent_grads
WHERE ShareWomen < 0.5

## 2. Finding a Columns Minimum and Maximum Values in SQL ##

select Major, Major_category, MIN(Median) from recent_grads
where Major_category = 'Engineering'

## 3. Calculating Sums and Averages in SQL ##

select SUM(Total) from recent_grads

## 4. Combining Multiple Aggregation Functions ##

select AVG(Total), MIN(Men), MAX(Women) from recent_grads

## 5. Customizing The Results ##

select COUNT(*) as 'Number of Students', MAX(Unemployment_rate) as 'Highest Unemployment Rate'
from recent_grads

## 6. Counting Unique Values ##

select COUNT(DISTINCT(Major)) unique_majors,
       COUNT(DISTINCT(Major_category)) unique_major_categories,
       COUNT(DISTINCT(Major_code)) unique_major_codes
from recent_grads

## 7. Performing Arithmetic in SQL ##

select Major, Major_category, P75th - P25th quartile_spread
from recent_grads
order by quartile_spread 
limit 20
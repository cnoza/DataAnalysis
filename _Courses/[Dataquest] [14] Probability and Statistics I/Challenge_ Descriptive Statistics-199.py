## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5)
ax2.set_xlim(0,5)
ax3.set_xlim(0,5)
ax4.set_xlim(0,5)

movie_reviews['RT_user_norm'].hist(ax=ax1)
movie_reviews['Metacritic_user_nom'].hist(ax=ax2)
movie_reviews['Fandango_Ratingvalue'].hist(ax=ax3)
movie_reviews['IMDB_norm'].hist(ax=ax4)

plt.show()

## 2. Mean ##

def calc_mean(series):
    return sum(series.values)/len(series.values)

cols = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']
user_reviews = movie_reviews[cols]

user_reviews_mean = user_reviews.apply(calc_mean)
rt_mean = user_reviews_mean['RT_user_norm']
mc_mean = user_reviews_mean['Metacritic_user_nom']
fg_mean = user_reviews_mean['Fandango_Ratingvalue']
id_mean = user_reviews_mean['IMDB_norm']

# Another way:
rt_mean1 = user_reviews[['RT_user_norm']].apply(calc_mean)
mc_mean1 = user_reviews[['Metacritic_user_nom']].apply(calc_mean)
fg_mean1 = user_reviews[['Fandango_Ratingvalue']].apply(calc_mean)
id_mean1 = user_reviews[['IMDB_norm']].apply(calc_mean)

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    return sum((series.values - mean) ** 2)/len(series.values)

user_reviews_var = user_reviews.apply(calc_variance)

rt_var = user_reviews_var['RT_user_norm']
rt_stdev = (rt_var) ** .5

mc_var = user_reviews_var['Metacritic_user_nom']
mc_stdev = (mc_var) ** .5

fg_var = user_reviews_var['Fandango_Ratingvalue']
fg_stdev = (fg_var) ** .5

id_var = user_reviews_var['IMDB_norm']
id_stdev = (id_var) ** .5


## 4. Scatter plots ##

fig = plt.figure(figsize=(4,8))

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5)
ax2.set_xlim(0,5)
ax3.set_xlim(0,5)

ax1.scatter(x=user_reviews['RT_user_norm'], y=user_reviews['Fandango_Ratingvalue'])
ax2.scatter(x=user_reviews['Metacritic_user_nom'], y=user_reviews['Fandango_Ratingvalue'])
ax3.scatter(x=user_reviews['IMDB_norm'], y=user_reviews['Fandango_Ratingvalue'])

# Another way:
#user_reviews.plot(kind='scatter', x='RT_user_norm', y='Fandango_Ratingvalue', ax=ax1)
#user_reviews.plot(kind='scatter', x='Metacritic_user_nom', y='Fandango_Ratingvalue', ax=ax2)
#user_reviews.plot(kind='scatter', x='IMDB_norm', y='Fandango_Ratingvalue', ax=ax3)

plt.show()

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_covariance(x,y):
    return sum((x.values-calc_mean(x)) * (y.values-calc_mean(y)))/len(x.values)

rt_fg_covar = calc_covariance(user_reviews['RT_user_norm'],user_reviews['Fandango_Ratingvalue'])
mc_fg_covar = calc_covariance(user_reviews['Metacritic_user_nom'],user_reviews['Fandango_Ratingvalue'])
id_fg_covar = calc_covariance(user_reviews['IMDB_norm'],user_reviews['Fandango_Ratingvalue'])

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(x,y):
    return calc_covariance(x,y)/((calc_variance(x) ** .5) * (calc_variance(y) ** .5))


rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

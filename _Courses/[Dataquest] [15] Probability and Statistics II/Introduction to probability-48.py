## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])

most_bars_country = flags['name'].iloc[flags['bars'].idxmax()]

highest_population_country = flags['name'].iloc[flags['population'].idxmax()]



## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = sum(flags['orange'] == 1)/total_countries

stripe_probability = sum(flags['stripes'] > 1)/total_countries


## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = .5 ** 10
hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
flags_red = flags['red'] == 1

three_red = (sum(flags_red)/total_countries) * ((sum(flags_red)-1)/(total_countries-1)) * ((sum(flags_red)-2)/(total_countries-2))

## 5. Disjunctive probability ##

start = 1
end = 18000

hundred_prob = len([i for i in range(start, end+1) if i % 100 == 0])/18000
seventy_prob = len([i for i in range(start, end+1) if i % 70 == 0])/18000

## 6. Disjunctive dependent probabilities ##

red_or_orange = sum(flags['orange'] == 1)/total_countries + sum(flags['red'] == 1)/total_countries - sum((flags['orange'] == 1) & (flags['red'] == 1))/total_countries

stripes_or_bars = sum(flags['stripes'] >= 1)/total_countries + sum(flags['bars'] >= 1)/total_countries - sum((flags['stripes'] >= 1)&(flags['bars'] >= 1))/total_countries

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = 1 - .5 ** 3
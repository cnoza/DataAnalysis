import read
from collections import Counter

df = read.load_data()

all_headlines = ''
for each in df['headline']:
    all_headlines += ' ' + str(each)
 
all_words = all_headlines.lower().split(' ')
ctn = Counter(all_words)

print(ctn.most_common(100))
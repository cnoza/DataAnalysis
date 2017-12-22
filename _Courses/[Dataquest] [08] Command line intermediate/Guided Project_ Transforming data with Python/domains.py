import read

def subdom(url_):
    url_s = str(url_).split('.')
    if len(url_s) >= 2:
        return url_s[-2] + '.' + url_s[-1]
    else:
        return url_

if __name__ == '__main__':

    df = read.load_data()

    df['url'] = df['url'].apply(subdom)

    domains = df['url'].value_counts()

    print(domains.head(100))

   
 
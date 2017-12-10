## 2. Authenticating with the API ##

headers = {'Authorization': 'bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk', 'User-Agent': 'Dataquest/1.0'}
params = {'t': 'day'}
response = requests.get('https://oauth.reddit.com/r/python/top', headers=headers, params=params)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = [item['data'] for item in python_top['data']['children']]

upvotes_max = 0
for post in python_top_articles:
    if post['ups'] > upvotes_max:
        most_upvoted = post['id']
        upvotes_max = post['ups']
    

## 4. Getting Post Comments ##

full_url = 'https://oauth.reddit.com/r/python/comments/' + most_upvoted
response = requests.get(full_url, headers=headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = [item['data'] for item in comments[1]['data']['children']]

ups_max = 0
for item in comments_list:
    if item['ups'] > ups_max:
        most_upvoted_comment = item['id']
        ups_max = item['ups']

## 6. Upvoting a Comment ##

status = requests.post('https://oauth.reddit.com/api/vote', json={'dir': 1, 'id': most_upvoted_comment}, headers=headers).status_code
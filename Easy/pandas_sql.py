import pandas as pd

data = {
    'tweet_id': [1, 2],
    'content': ['Vote for Biden', 'Let us make America great again!']
}

tweets = pd.DataFrame(data)

invalid_tweets = tweets[tweets['content'].apply(len) > 15]

result = invalid_tweets[['tweet_id']]

print(result)

import tweepy
from textblob import TextBlob

# Dane do uwierzytelnienia w API Twittera
consumer_key = 'Uw1YwoRIgVX68L15FvPDEbGg2'
consumer_secret = 'zTYRH2Lpjatt2p2qstm6qkMjvJtsYD9LVwidampYuaokHnJKKS'
access_token = '1641315489803542528-MDVt9pyM3uEmPcQi4tBwj0N0qlc6EH'
access_token_secret = 'raHSj5jHDU76YACNhFKVEtLT0nFsjen0NvMipAWaDn1LE'


# Uwierzytelnienie i połączenie z API Twittera
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Pobranie tweetów z hashtagiem WIG20
tweets = api.search_tweets(q='WIG20', count=3)

# Analiza sentymentu tweetów za pomocą biblioteki TextBlob
positive_tweets = 0
neutral_tweets = 0
negative_tweets = 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        positive_tweets += 1
    elif analysis.sentiment.polarity == 0:
        neutral_tweets += 1
    else:
        negative_tweets += 1

# Obliczenie współczynnika nastroju
total_tweets = len(tweets)
sentiment_ratio = (positive_tweets / total_tweets) * 100

print(f'Analiza sentymentu dla hashtagu WIG20:')
print(f'Liczba tweetów: {total_tweets}')
print(f'Liczba tweetów pozytywnych: {positive_tweets}')
print(f'Liczba tweetów neutralnych: {neutral_tweets}')
print(f'Liczba tweetów negatywnych: {negative_tweets}')
print(f'Współczynnik nastroju: {sentiment_ratio}%')
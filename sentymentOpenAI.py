import openai
import tweepy

# Dane do uwierzytelnienia w API Twittera
consumer_key = 'Uw1YwoRIgVX68L15FvPDEbGg2'
consumer_secret = 'zTYRH2Lpjatt2p2qstm6qkMjvJtsYD9LVwidampYuaokHnJKKS'
access_token = '1641315489803542528-MDVt9pyM3uEmPcQi4tBwj0N0qlc6EH'
access_token_secret = 'raHSj5jHDU76YACNhFKVEtLT0nFsjen0NvMipAWaDn1LE'

# Uwierzytelnienie i połączenie z API Twittera
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Dane do uwierzytelnienia w API OpenAI
openai.api_key = "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"

# Lista spółek WIG20
wig20_companies = ['CDPROJEKT', 'CYFRPLSAT', 'LOTOS', 'PGE', 'PGE', 'PKNORLEN', 'PKOBP', 'PEKAO', 'PGNIG', 'PZU', 'SANPL', 'TAURONPE', 'TPSA', 'KGHM', 'JSW', 'ALEO', 'MBANK', 'CCC', 'AMICA', 'TVN']

# Funkcja do analizy sentymentu zapytania za pomocą ChatGPT
def analyze_sentiment(query):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Sentiment analysis for: {query}\n"
                "Positive, negative or neutral?"),
        temperature=0.5,
        max_tokens=60,
        n = 1,
        stop=None,
        timeout=5
    )

    sentiment = response.choices[0].text.strip().lower()

    return sentiment

# Funkcja do pobierania tweetów dotyczących danej spółki z Twittera
def get_tweets(company):
    tweets = api.search_tweets(q=company, count=3)
    return tweets

# Analiza sentymentu dla każdej spółki WIG20
for company in wig20_companies:
    tweets = get_tweets(company)
    positive_tweets = 0
    neutral_tweets = 0
    negative_tweets = 0

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet.text)
        if sentiment == 'positive':
            positive_tweets += 1
        elif sentiment == 'neutral':
            neutral_tweets += 1
        else:
            negative_tweets += 1

    total_tweets = len(tweets)
    sentiment_ratio = (positive_tweets / total_tweets) * 100

    print(f'Analiza sentymentu dla {company}:')
    print(f'Liczba tweetów: {total_tweets}')
    print(f'Liczba tweetów pozytywnych: {positive_tweets}')
    print(f'Liczba tweetów neutralnych: {neutral_tweets}')
    print(f'Liczba tweetów negatywnych: {negative_tweets}')
    print(f'Współczynnik nastroju: {sentiment_ratio}%')
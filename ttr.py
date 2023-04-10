import pandas as pd
from textblob import TextBlob
import snscrape.modules.twitter as sntwitter


scraper = sntwitter.TwitterSearchScraper("#wig20 CCC lang:pl ")
tweets=[]
#scrapowanie tweetów dla wskazanego zapytania
for i, tweet in enumerate(scraper.get_items()):
    data = tweet.rawContent
    tweets.append(data)
    print(data)
    if i>=20:
        break
tweet_df=pd.DataFrame(tweets, columns=["tekst"])
tweet_df.to_csv("tweety.csv", index=False)



# Wczytanie danych z pliku CSV
df = pd.read_csv('tweety.csv')

# Tworzenie listy ocen sentymentu dla każdej wiadomości
sentiments = []
for text in df['tekst']:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    sentiments.append(sentiment)

# Obliczenie średniej oceny sentymentu
average_sentiment = sum(sentiments) / len(sentiments)

# Interpretacja słowna wyniku
if average_sentiment > 0:
    print("Większość wiadomości ma pozytywny wydźwięk.")
elif average_sentiment < 0:
    print("Większość wiadomości ma negatywny wydźwięk.")
else:
    print("Większość wiadomości jest neutralna.")

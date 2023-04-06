import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
#tweety wyciagnax sentyment dziala
# Lista firm z WIG20
wig20 = ['ASSECO-POLAND', 'ALE', 'CCC', 'CD-PROJEKT', 'CYFROWY-POLSAT', 'DNP', 'JSW-JASTRZEBSKA-SPOLKA-WEGLOWA','KGHM', 'KRUK', 'KETY', 'LPP','MBANK', 'ORANGE', 'PCO', 'PEKAO', 'PGE', 'PKN-ORLEN', 'PKO', 'PZU', 'SPL']

# Utworzenie pustej listy na tweet'y
tweets = {}

# Pętla po każdej firmie z WIG20
for company in wig20:
    tweets[company] = []
    # Pobranie strony wyszukiwania na Twitterze dla danej firmy
    url = f"https://twitter.com/search?q={company}%20lang%3Apl%20-filter%3Aretweets&src=typed_query"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    # Pobranie tweetów z listy
    text=soup.find("span")
    print(soup)
    for tweet in soup.find_all('span'):
         #Pobranie tekstu tweet'u
        text = tweet.find('span').get_text()
         #Dodanie tweet'u do listy
        tweets[company].append(text)
        print(text)
        print(tweet)
# Analiza sentymentu za pomocą TextBlob
for company in wig20:
    sentiment = 0
    count = 0
    for tweet in tweets[company]:
        analysis = TextBlob(tweet)
        sentiment += analysis.sentiment.polarity
        count += 1
    if count > 0:
        sentiment /= count
    print(f"{company}: {sentiment}")

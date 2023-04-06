import tweepy

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = 'Uw1YwoRIgVX68L15FvPDEbGg2'
consumer_secret = 'zTYRH2Lpjatt2p2qstm6qkMjvJtsYD9LVwidampYuaokHnJKKS'

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = '1641315489803542528-MDVt9pyM3uEmPcQi4tBwj0N0qlc6EH'
access_token_secret = 'raHSj5jHDU76YACNhFKVEtLT0nFsjen0NvMipAWaDn1LE'

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# If the authentication was successful, this should print the
# screen name / username of the account
print(api.verify_credentials().screen_name)
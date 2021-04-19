import pymongo
import tweepy


claves = open('keys_twitter.txt')
keys = []
for clave in claves:
    clave = clave.replace('\n', '')
    clave = clave.split(',')
    keys.append(clave[1])
consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets = []

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
bd = cliente['bigdata']
coleccion = bd['tweets']
try:
    ultimo_tweet = coleccion.find_one(sort=[("id", -1)])['id']
except:
    ultimo_tweet = None

for tweet in tweepy.Cursor(api.user_timeline, since_id=ultimo_tweet, screen_name = 'alferdez', tweet_mode = 'extended').items(100):
    #pprint.pprint(tweet._json)#Para ver toda la info de los tutis
    tweet_dic = tweet._json
    tweets.append(tweet_dic)
    print("tweet capturado")

coleccion.insert_many(tweets)


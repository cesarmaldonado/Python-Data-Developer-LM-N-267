import tweepy
from flask import Flask, json

claves = open('C:/Users/Pc/Desktop/Python/Cursos EANT/Data Developer/Clase_11/keys_twitter.txt')
keys = []
for clave in claves:
    clave = clave.replace('\n', '')
    clave = clave.split(',')
    keys.append(clave[1])
consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[3]
access_token_secret = keys[4]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app = Flask(__name__)

@app.route('/users/<path>')
def searchTwitter(path):
    if path == 'personas':
        response = api.followers(screen_name = 'aguerosergiokun')
    elif path == 'empresas':
        response = api.get_user("BillboardArg")
    else: 
        response = 'No Puedo mostrar lo que estas pidiendo'
    return response

if __name__ == '__main__':
    app.run( port = 3030)


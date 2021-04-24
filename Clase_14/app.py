from flask import Flask, json, request
import settings
from os import environ
from pymongo import MongoClient 
from urllib.parse import urlencode


app = Flask(__name__)

USER = environ['USER']
PASS = environ['PASS']
HOST = environ['HOST']
BASE = environ['BASE']

params = {
'retryWrites':'true',
'w':'majority',
'ssl':'true',
'ssl_cert_reqs':'CERT_NONE'  
}

client = MongoClient("mongodb+srv://"+ USER +":"+ PASS +"@"+ HOST+"/"+ BASE +"?"+urlencode(params))


@app.route('/')
def hello_flask():
    return 'Hola desde Flask :D'
#########

@app.route('/users')
def usersTwitter():
    users = [
        {'name' :'smessina_'},
        {'name' :'eanttech'},
        {'name' :'TinchoLutter'},
        {'name' :'bitcoinArg'}
        ]
    response = app.response_class(response = json.dumps(users), status = 200, mimetype = 'application/json')
    return response
#########

@app.route('/users/<path>')
def searchTwitter(path):
    if path == 'personas':
        response = "Aca deberia mostrar un Json de personas"
    elif path == 'empresas':
        response = "Aca deberia mostrar un Json de empresas"
    else: 
        response = 'No Puedo mostrar lo que estas pidiendo'
    return response
#########

@app.route('/api/tweets/<user>/<limit>', methods = ['GET'])
def getTweets(user, limit):
    
    bigdata = client['bigdata']
    tweets = bigdata['tweets']
    
    #sin ternario
    # if limit != None and limit.isnumeric():
    #     limit = int(limit)
    # else:
    #     limit = 0
    
    #con ternario
    limit = int(limit) if limit != None and limit.isnumeric() else 0

    los_tweets = tweets.find({'in_reply_to_screem_name': user}).limit(limit)

    response = [] if los_tweets.count() > 0 else [{'ok': False, 'mgs' : 'User not found'}]   

    for tweet in los_tweets:
        el_tweet = {
            'id' : tweet['id_str'],
            'user' : tweet['in_reply_to_screem_name'],
            'message' : tweet['full_text']
             }
        
        response.append(el_tweet)
        
        # print( tweet['id_str'] )
  
    return app.response_class(response = json.dumps(response), status = 200, mimetype = 'application/json')
########

@app.route('/api/tweets', methods = ['POST'])
def postTweets():
    
    bigdata = client['bigdata']
    tweets = bigdata['tweets']
    
    el_tweet = {
        'id_str' : request.form['id'],
        'in_reply_to_screem_name' : request.form['user'],
        'full_text' : request.form['message']
    }
          
    result = tweets.insert_one( el_tweet)
    print(result.acknowledged)
    response = [{'ok': True, 'mgs': 'Tweet saved!'}] if result.acknowledged == True else [{'ok': False, 'mgs': 'Error..'}]
    return app.response_class(response = json.dumps(response), status = 200, mimetype = 'application/json')

if __name__ == '__main__':
    app.run( port = 3030, host= '0.0.0.0')

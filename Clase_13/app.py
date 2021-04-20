from flask import Flask, json


app = Flask(__name__)

# client = pymongo.MongoClient("mongodb+srv://cesarmaldonado:<password>@saopablomydatabase.txlon.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

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

if __name__ == '__main__':
    app.run( port = 3030, host= '0.0.0.0')

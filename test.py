from flask import Flask
from flask import request;

app = Flask(__name__)

@app.route('/test')
def index():
    
    str = "Hello, "
    username = request.args.get('username')
    if(username is not None ):
        str = str + username
    return str

app.run(host='0.0.0.0', port=9999)

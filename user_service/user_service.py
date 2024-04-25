from flask import Flask
import json
app = Flask(__name__)

@app.route('/user_service')
def user_service():
    message={"message":'Hello, this is user service'}
    return json.dumps(message)

if __name__=='__main__':
    app.run(port=5000)
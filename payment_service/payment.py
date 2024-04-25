from flask import Flask
app = Flask(__name__)
import json

@app.route('/payment')
def payment():
    message={"message":'Hello, this is payment service'}
    return json.dumps(message)

if __name__=='__main__':
    app.run(port=5001)
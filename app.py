import time
from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
   print('here')
   print(request.form)
   print(request.get_json())
   return 'Hello mo! I have been 2 times'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

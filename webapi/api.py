#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello, World!"

@app.route('/pliers/1.0/<int:status>', methods=['GET', 'POST'])
def pliers(status):
  return str(status)

if __name__ == '__main__':

  app.run(debug=True)

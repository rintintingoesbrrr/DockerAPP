from flask import Flask, jsonify, request
app = Flask(__name__)

endpoints = [
   { '/hello': 'returns "hello world"', '/health': 'returns the status of the APP' }
]

@app.route('/')
def get_incomes():
   return jsonify(endpoints)

@app.route('/hello')
def helloPSL():
   return "Hello P\S\L"

@app.route('/health')
def health():
   return "App is up and running"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
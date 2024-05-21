from flask import Flask, jsonify
from requestTomtom import verritas

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    data = verritas()
    # {
    #     "name": "John",
    #     "age": 30,
    #     "city": "New York"
    # }
    return jsonify(data)

app.run(port=5000,host='localhost', debug=True)

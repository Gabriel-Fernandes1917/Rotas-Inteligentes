from flask import Flask, jsonify
from requestTomtom import verrotas

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    data = verrotas()

    return jsonify(data)

app.run(port=5000,host='0.0.0.0', debug=True)

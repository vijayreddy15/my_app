from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods=['POST'])
def square():
    data = request.get_json()
    number = data.get('number', 0)
    result = number ** 2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


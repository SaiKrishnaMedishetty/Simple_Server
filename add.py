from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Please provide both num1 and num2'}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'num1 and num2 must be numbers'}), 400

    result = num1-num2
    return jsonify({'sum': result})

if __name__ == '__main__':
    app.run(debug=False)

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    greeting_message = f"Hello Everyone"
    return jsonify(message=greeting_message)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

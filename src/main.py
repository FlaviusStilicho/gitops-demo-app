from flask import Flask

app = Flask(__name__)


@app.route('/health')
def hello():
    return 'Hello!', 200, {}

@app.route('/hello')
def hello2():
    return 'Hello world!', 200, {}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    app.secret_key=''
    app.run(debug=True)
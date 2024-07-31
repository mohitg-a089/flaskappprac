from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return 'Hello, this app is for githubactions demo'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
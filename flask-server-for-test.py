from flask import Flask

app = Flask(__name__)

@app.route('/')
def First_run():
    return 'Hello Flask'

@app.route('/add')
def add():
    return 'add something'

@app.route('/delete')
def delete():
    return 'delete something'


if __name__ == '__main__':
    app.run(debug=True,port=8080)
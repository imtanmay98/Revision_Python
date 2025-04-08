from flask import Flask
app = Flask(__name__)
@app.route('/add/<a>/<b>')
def add(a, b):
    answer = int(a) + int(b)
    result = {
        'ans': answer
    }
    return result


if __name__ == '__main__':
    app.run(debug=True)

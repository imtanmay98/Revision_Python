from flask import Flask
app = Flask(__name__)
@app.route('/api/<name>')
def api(name):
    result= 'Hello ' + name + ' !'
    return result
if __name__ == '__main__':
    app.run(debug=True)
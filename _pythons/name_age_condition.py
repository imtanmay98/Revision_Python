from flask import Flask, request
app= Flask(__name__)

@app.route('/api')
def home():
    name = request.values.get('name')
    age = request.values.get('age')
    age = int(age)
    if age>18:
        return 'welcome to the site,' +name+ '!'
    else:
        return 'Sorry! you are not authorized to access this site!!'

if __name__ =='__main__':
    app.run(debug=True)

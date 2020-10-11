from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username':'Serhii'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
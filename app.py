#-*-coding:utf8

from flask import Flask


from flask import request

from flask import render_template
app = Flask(__name__)


@app.route('/' , methods=['GET' , 'POST'])
def home():
    return render_template('index.html')

@app.route('/signin' , methods = ['GET'])
def signin_form():
    return render_template('sign-form.html')

@app.route('/signin' , methods = ['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123':
        return render_template('signin-ok.html' , username = username)
    return render_template('sign-form.html' , message = 'Error Password Or Username!')

if __name__ == '__main__':
    app.run(debug=True)
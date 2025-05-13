from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doxy')
def doxy():
    return render_template('doxy.html')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=3000)
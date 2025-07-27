from flask import Flask, redirect, abort
import json

app = Flask(__name__)

DEFAULT_URL = "https://www.google.com"

def load_redirects():
    with open('redirects.json', 'r') as f:
        return json.load(f)

@app.route('/<client_id>')
def redirect_qr(client_id):
    redirects = load_redirects()
    if client_id in redirects:
        url = redirects[client_id]
        if url:
            return redirect(url, code=302)
        else:
            return redirect(DEFAULT_URL, code=302)
    return abort(404, description="QR code non reconnu")

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=10000, debug=True)



""" from flask import Flask, redirect, abort
import json

app = Flask(__name__)

def load_redirects():
    with open('redirects.json', 'r') as f:
        return json.load(f)

@app.route('/<client_id>')
def redirect_qr(client_id):
    redirects = load_redirects()
    url = redirects.get(client_id)
    if url:
        return redirect(url, code=302)
    return abort(404, description="QR code non reconnu")

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=10000, debug=True) """




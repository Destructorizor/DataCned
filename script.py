from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_data():
    username = request.form['username']
    password = request.form['password']
    
    login_url = "https://www.cned360.fr/uPortal/p/Login"
    login_data = {
        "username": username,
        "password": password
    }
    
    session = requests.Session()
    response = session.post(login_url, data=login_data)
    
    if response.status_code == 200:
        data_url = "https://www.cned360.fr/uPortal/main-es2015.8f57def7b996d0b3600e.js"
        data_response = session.get(data_url)
        
        if data_response.status_code == 200:
            return "Data downloaded successfully."
        else:
            return "Failed to download data."
    else:
        return "Login failed."

if __name__ == '__main__':
    app.run(debug=True)

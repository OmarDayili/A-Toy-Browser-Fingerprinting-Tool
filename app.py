from flask import Flask, render_template, request
import platform
import hashlib

app = Flask(__name__)

def generate_fingerprint(user_agent, accept, languages, platform_info):
    data_string = f"{user_agent}{accept}{languages}{platform_info}"
    fingerprint = hashlib.sha256(data_string.encode()).hexdigest()
    return fingerprint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fingerprint', methods=['POST'])
def fingerprint():
    user_agent = request.headers.get('User-Agent')
    accept = request.headers.get('Accept')
    languages = request.headers.get('Accept-Language')     
    platform_info = platform.platform()
    
    fingerprint = generate_fingerprint(user_agent, accept, languages, platform_info)
    return render_template('result.html', fingerprint=fingerprint, user_agent=user_agent, accept=accept, languages=languages, platform_info=platform_info)

if __name__ == '__main__':
    app.run(debug=True)

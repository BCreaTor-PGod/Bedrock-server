from flask import Flask, render_template, request, redirect
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_server():
    subprocess.Popen(['start_server.bat'], shell=True)
    return redirect('/')

@app.route('/stop', methods=['POST'])
def stop_server():
    subprocess.call(['stop_server.bat'], shell=True)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask
import getpass
import time
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Gontla Prabhas"
    username = getpass.getuser()
    
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')
    top_output = subprocess.getoutput("top -b -n 1 | head -20")

    html = f"""
    Name: {name}<br>
    user: {username}<br>
    Server Time (IST): {ist_time}<br>
    <br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

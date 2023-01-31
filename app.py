from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['get'])

def time():
    time_now = datetime.now().strftime("%H:%M:%S")
    return ('The current date and time is: ' + time_now )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

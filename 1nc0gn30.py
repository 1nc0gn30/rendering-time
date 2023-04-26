from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    is_weekend = now.weekday() in (5, 6)  # Saturday is 5, Sunday is 6
    return render_template('1nc0gn30.html', datetime=now, is_weekend=is_weekend)

if __name__ == '__main__':
    app.run(debug=True)



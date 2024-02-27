from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Use 0.0.0.0 as the host to make the app externally accessible
    app.run(host='0.0.0.0', port=8000)

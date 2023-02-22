from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def peace_world():
    return "peace world"
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True )

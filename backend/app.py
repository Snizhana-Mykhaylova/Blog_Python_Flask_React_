from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[SQLALCHEMY_DATABASE_URI] = "mysql://root:""@localchost/blog"
app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = False

@app.route('/', methods = ['GET'])

def get_articles():
    return jsonify({"Hello":"World"})

if __name__ == "__main__":
    app.run(debug=True)


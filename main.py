from flask import Flask, render_template, Request, request, redirect, Response, jsonify
from flask_pymongo import PyMongo

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


mongo = PyMongo(app=app)
db = mongo.db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/telegrams')
def telegrams():
    return render_template('telegrams.html')


@app.route('/longread')
def longread():
    return render_template('longread.html')


@app.route('/thank-you')
def thankyou():
    return render_template('thankyou.html')


@app.route('/add', methods = ['POST', 'GET'])
def add():
    if request.method == "POST":
        with open("user_data.txt", "a") as file:
            file.write(str(request.form.to_dict()) + "\n")
        return redirect("/thank-you")
    else:
        return render_template('add.html')


@app.route('/user-data', methods=['POST'])
def add_user_data():
    data = request.get_json(force=True)
    print(data)
    db.user_data.insert_one(data)
    return jsonify(message='user data saved'), 201


@app.route('/user-data', methods=['GET'])
def get_user_data():
    data = [
        {
            "username": user.get("username"),
            "picture_link": user.get("picture_link"),
            "volunteer": user.get("volunteer"),
            "contact_info": user.get("contact_info"),
        }
        for user in db.user_data.find()
    ]
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=True)

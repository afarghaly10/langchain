from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from app import app

load_dotenv()

server = Flask(__name__)


@server.route("/")
def index():
    return render_template("index.html")


@server.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = app(name=name)
    result = {"summary_and_facts": summary.to_dict(), "photoUrl": profile_pic_url}
    return jsonify(result)


if __name__ == "__main__":

    server.run(port=4000, host="0.0.0.0", debug=True)

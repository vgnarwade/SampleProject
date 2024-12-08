from flask import Flask, render_template, Response


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return Response("This is home page.")



if __name__ == "__main__":
    app.run(debug=True)
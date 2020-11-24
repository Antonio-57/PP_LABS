from flask import Flask
app = Flask(__name__)


@app.route("/api/v1/hello-world-{1_V}")
def index():
    return "Hello world! 1 Variant"


if __name__ == "__main__":
    app.run(debug=True)

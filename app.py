from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello, Bekbolat!</h1>
    <p>DevOps Laboratory Work 4</p>
    <p>Variant 16</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

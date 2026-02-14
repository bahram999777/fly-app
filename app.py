from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello testehosh.ir 🚀"

if __name__ == "__main__":
    app.run()

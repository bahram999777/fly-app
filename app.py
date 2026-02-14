from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "سلام! سایت شما با موفقیت روی Fly.io اجرا شد 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

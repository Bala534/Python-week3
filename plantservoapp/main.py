from flask import Flask,render_template, request

app = Flask(__name__)
from .data.info import bot

@app.route("/")
def index():
	return render_template("index.html", data=bot, question={'key':"name","text":"Hello😊😊! I am a PlantServo Bot☘☘. Please enter your name:"})

@app.route("/message", methods=['POST'])
def user_message():
    if request.method == 'POST':
        from .intents import handle
        return handle(request.form)
    else:
        return "invalid"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
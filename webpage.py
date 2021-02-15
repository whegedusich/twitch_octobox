from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('Main.html')


@app.route("/Streams", methods=["POST", "GET"])
def streams():
    if request.method == "POST":
        streamers = request.form

        return render_template('Streams.html', chans=streamers)


if __name__ == '__main__':
    app.run('0.0.0.0', port='80')

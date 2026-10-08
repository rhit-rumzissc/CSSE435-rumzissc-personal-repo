import flask
import blinker
import threading

app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
blink = blinker.Blinker() #TODO: set port if needed

@app.get("/api/<flashes>/<periodMS>")
def handle_commands(flashes, periodMS):
    with serial_lock:
        response = blink.send_command(flashes, periodMS)
    return response

@app.route("/")
def naked_domain_route():
    return flask.redirect("/index.html")


if __name__ == "__main__":
    print("Running flask!")
    blink.connect()
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)

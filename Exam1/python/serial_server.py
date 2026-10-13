import flask
import my_blinker
import threading

app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
blink = my_blinker.Blinker()

@app.get("/api/flash/<flashes>/<periodMS>")
def handle_commands(flashes, periodMS):
    with serial_lock:
        response = blink.send_flash(flashes, periodMS)
    return response

@app.get("/api/led/<LEDState>")
def handle_LED_commands(LEDState):
    with serial_lock:
        if (LEDState == "on"):
            response = blink.send_LED_State("LED ON")
            #LEDState == "LED ON"
        elif (LEDState == "off"):
            response = blink.send_LED_State("LED OFF")
            #LEDState == "LED OFF"
        #print(LEDState)
        else:
            response = "ERROR"
        
    return response

@app.route("/")
def naked_domain_route():
    return flask.redirect("/index.html")


if __name__ == "__main__":
    print("Running flask!")
    blink.connect()
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)

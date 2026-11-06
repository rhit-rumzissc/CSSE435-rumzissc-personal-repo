import mqtt_helper as mh
from rosebot import Rosebot
import signal
import time

class App:
    def __init__(self):
        self.robot = Rosebot()
        self.ultra = self.robot.ultrasonic()

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/rumzissc/#",
                                 publish_topic_name="me435/rumzissc/")
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, message_payload):
        
        if message_type == "left":
            print("Side: " + message_type + 
                        "  Direction: " + message_payload[0] +
                        "  Time: " + message_payload[1] +
                        "  Speed: " + message_payload[2])
            if message_payload[0]: #forwards
                self.robot.drive_system.set_speeds(message_payload[2],message_payload[2], 0, 0)
            else: 
                self.robot.drive_system.set_speeds(-message_payload[2],-message_payload[2], 0, 0)
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()

        if message_type == "right":
            print("Side: " + message_type + 
                        "  Direction: " + message_payload[0] +
                        "  Time: " + message_payload[1] +
                        "  Speed: " + message_payload[2])
            if message_payload[0]: #forwards
                self.robot.drive_system.set_speeds(0, 0, message_payload[2],message_payload[2])
            else: 
                self.robot.drive_system.set_speeds(0, 0, -message_payload[2],-message_payload[2])
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()

        if message_type == "both":
            print("Side: " + message_type + 
                        "  Direction: " + message_payload[0] +
                        "  Time: " + message_payload[1] +
                        "  Speed Left: " + message_payload[2] +
                        "  Speed Right: " + message_payload[3])
            if message_payload[0]: #forwards
                self.robot.drive_system.set_speeds(message_payload[2],message_payload[2],message_payload[3],message_payload[3])
            else: 
                self.robot.drive_system.set_speeds(-message_payload[2],-message_payload[2],-message_payload[3],-message_payload[3])
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()

def main():
    print("GPIO MQTT")
    app = App()
    
    try:
        while True:
            ultra_reading = app.robot.ultra.get_cm()
            print("Ultra: " + ultra_reading)
            app.mqtt_client.send_message("ultra", round(ultra_reading))
            time.sleep(2)

        #signal.pause() # keeps program running

    except KeyboardInterrupt:
        print("Goodbye")
        app.robot.drive_system.stop
        app.mqtt_client.close()

main()
import serial
import time

class Blinker:
    def __init__(self, port="/dev/ttyACM0"):
        self.port = port
        self.ser = None
        

    def connect(self):
        if self.ser and self.ser.is_open:
            return
        self.ser = serial.Serial(port=self.port, baudrate=19200, timeout=15)
        time.sleep(2.0)
        self.ser.reset_input_buffer()     

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

    def send_flash(self, flashes, periodMS):
        self.ser.reset_input_buffer()
        message_bytes = (str(flashes) + " " + str(periodMS) + "\n").encode()
        print(message_bytes)
        self.ser.write(message_bytes)

        response_bytes = self.ser.readline()
        print(response_bytes)
        response = response_bytes.decode().strip()
        return response

    def send_LED_State(self, LEDState):
            self.ser.reset_input_buffer()
            message_bytes = (str(LEDState) + "\n").encode()
            print(message_bytes)
            self.ser.write(message_bytes)
    
            response_bytes = self.ser.readline()
            print(response_bytes)
            response = response_bytes.decode().strip()
            return response

if __name__ == "__main__":
    print("Quick Blinker testing")
    blink = Blinker()
    blink.connect()
    response = blink.send_flash(6, 500)
    print("Response: ", response)
    blink.disconnect()
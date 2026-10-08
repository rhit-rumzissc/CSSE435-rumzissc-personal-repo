String inputString = "";      // a String to hold incoming data
bool isFlashSet = false;  // whether the string is complete
int flashes = 1;
int periodMS = 1000;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  // initialize serial:
  Serial.begin(19200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  if (isFlashSet){
    for (int i = 1; i <= flashes; i++) {
      digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
      delay(periodMS/2);
      digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
      delay(periodMS/2);
    }
    isFlashSet = false;
  }
  
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();

    if (inChar == ' ') {
      flashes = inputString.toInt();
      inputString = "";
      Serial.print("Flashes: ");
      Serial.println(flashes);
    } else if (inChar == '\n') {
      periodMS = inputString.toInt();;
      inputString = "";
      isFlashSet = true;
      Serial.print("Period: ");
      Serial.println(periodMS);
    } else {
      inputString += inChar;
    }
  }
}

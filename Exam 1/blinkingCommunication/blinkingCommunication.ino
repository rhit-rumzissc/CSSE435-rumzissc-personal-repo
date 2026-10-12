String inputString = "";      // a String to hold incoming data
bool isFlashSet = false;  // whether the string is complete
int flashes = 1;
int periodMS = 1000;
bool isLEDOn = false;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  // initialize serial:
  Serial.begin(19200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  if ((isFlashSet) &! (isLEDOn)){
    for (int i = 1; i <= flashes; i++) {
      digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
      delay(periodMS/2);
      digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
      delay(periodMS/2);
    }
    isFlashSet = false;
  }
  if (isLEDOn){
      digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  } else {
      digitalWrite(LED_BUILTIN, LOW);
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
      if (inputString == "LED"){
      } else {
        flashes = inputString.toInt();
        inputString = "";
      }

    } else if (inChar == '\n') {
      if (inputString == "LEDON"){
        isLEDOn=true;
        Serial.println("LED ON");
      } else if (inputString == "LEDOFF"){
        isLEDOn=false;
        Serial.println("LED OFF");
        isFlashSet = false;
      } else {
      periodMS = inputString.toInt();
      
      isFlashSet = true;

      Serial.print("Flashes = " + String(flashes) + "  ");
      Serial.println( "PeriodMS = " + String(periodMS));
      }
      inputString = "";
    } else {
      inputString += inChar;
    }
  }

}

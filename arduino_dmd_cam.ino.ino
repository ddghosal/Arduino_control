const int dmdSignalPin = 2;           // Replace with the right DMD signal pin
const int machineTriggerPin = 3;      // Replace with the right machine trigger pulse pin
const int cameraTriggerPin = 4;       // Replace with the right camera trigger pin

void setup() {
  pinMode(dmdSignalPin, INPUT);
  pinMode(machineTriggerPin, INPUT);
  pinMode(cameraTriggerPin, OUTPUT);
  
  // Initialize the camera trigger pin to LOW
  digitalWrite(cameraTriggerPin, LOW);

  //Serial.begin(9600); // Start serial communication
  //If the camera is directly connected to one of the digital pins on the Arduino board and can be triggered by setting 
  //that pin HIGH, then serial communication is not required.
}

void loop() {
  // Read the status of the DMD signal and machine trigger pulse
  int dmdSignalStatus = digitalRead(dmdSignalPin);
  int machineTriggerStatus = digitalRead(machineTriggerPin);

  // Check if both DMD signal and machine trigger pulse are HIGH (active)
  if (dmdSignalStatus == HIGH && machineTriggerStatus == HIGH) {
    // Trigger the camera by sending a high signal
    digitalWrite(cameraTriggerPin, HIGH);
    delay(100);  // Keep the signal high for a short duration (adjust as needed)
    digitalWrite(cameraTriggerPin, LOW);
    //Serial.println("Camera triggered!");
    // Add any additional camera-specific logic here
  }

  // Add a delay or other processing as needed
  delay(100);  // Adjust the delay
}


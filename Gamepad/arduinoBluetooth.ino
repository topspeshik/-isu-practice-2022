#include <ArduinoJson.h>
#include <SoftwareSerial.h>
#include <TroykaIMU.h>


#define pinX A0
#define pinY A3
#define pinZ A7


Gyroscope gyroscope;
SoftwareSerial bluetooth(8, 9);

void setup() {
   Serial.begin(9600);
   bluetooth.begin(9600);
   gyroscope.begin();
}

void loop() {
  DynamicJsonDocument doc(1024);

  int x = analogRead(pinX);
  int y = analogRead(pinY);
  int z = analogRead(pinZ);
  int gyrX = gyroscope.readRotationDegX();
  int gyrY = gyroscope.readRotationDegY();

  doc["pinX"] = x;
  doc["pinY"] = y;
  doc["pinZ"] = z;
  doc["gyrX"] = gyrX;
  doc["gyrY"] = gyrY;

  serializeJson(doc, bluetooth);
  delay(100);
  serializeJson(doc, Serial);
  Serial.println();
}

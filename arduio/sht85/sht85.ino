#include <Wire.h>
#include "SHTSensor.h"
#include <ArduinoJson.h>

SHTSensor sht;
// To use a specific sensor instead of probing the bus use this command:
// SHTSensor sht(SHTSensor::SHT3X);
void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
  delay(1000); // let serial console settle
  if (sht.init()) {
    Serial.print("init(): success\n");
  } else {
    Serial.print("init(): failed\n");
  }
  sht.setAccuracy(SHTSensor::SHT_ACCURACY_MEDIUM); // only supported by SHT3x
}
void loop() {
  // put your main code here, to run repeatedly:
  if (sht.readSample()) {
    Serial.print(sht.getHumidity(), 2);
    Serial.print(" ");
    Serial.println(sht.getTemperature(), 2);
  } else {
    Serial.print("Error in readSample()\n");
  }
  delay(500);
}

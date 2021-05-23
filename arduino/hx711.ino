#include <Arduino.h>
// https://github.com/bogde/HX711
#include "HX711.h"
const int DT_PIN = 2;
const int SCK_PIN = 3;
HX711 scale;
//TO DO
//set reference and offseet
void setup() {
  Serial.begin(9600);
  //Serial.println("start");
  scale.begin(DT_PIN, SCK_PIN);

  scale.set_scale(unit/reference_i); //set reference units
  scale.tare();

  scale.set_offset(deviation); //definition of offset?

  Serial.println(scale.get_units(10));
}


void loop() {
  Serial.println(scale.get_units(1), 1);
}

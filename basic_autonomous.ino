
#include <stdio.h>

//This code is UNTESTED and is likely full of bugs. This is the earliest version.

int motor_one = //Digital Pin 1 (Motor on the left) (Forward)
int motor_two = //Digital Pin 2 (Motor on the right) (Forward)
int ultrasonic = //Analog Pin 5 (On the front of the robot)
int init_length = //Length of the Grid Area
int d = //Number of times the robot goes through the loop
int range = //Ultrasonic Sensor Range
int counter = 0
int motor_one_back = //Digital Pin 1 (Motor on the left) (Backward)
int motor_two_back = //Digital Pin 2 (Motor on the right) (Backward)
int constant = //Rotation delay time
int constant2 = //Backup delay time

void setup() {
  // put your setup code here, to run once:
  
  pinMode(motor_one, OUTPUT)
  pinMode(motor_two, OUTPUT)
  pinMode(ultrasonic, INPUT) 
  Serial.begin(9600);
  Serial.println("Starting...");
  
}

void loop() {
  if (counter == 0) {
  for (int i = 0; i < d; i++) {
    if (analogRead(ultrasonic) < range) {
    digitalWrite(motor_one, HIGH)
    digitalWrite(motor_two, HIGH)
  }
  else {
    digitalWrite(motor_two, LOW)
    delay(constant)
    digitalWrite(motor_one, LOW)
    if (analogRead(ultrasonic) < range) {
      digitalWrite(motor_one_back, HIGH)
      delay(constant)
      digitalWrite(motor_one_back, LOW)
      digitalWrite(motor_two, HIGH)
      delay(constant)
      digitalWrite(motor_two, LOW)
      if (analogRead(ultrasonic) < range) {
        digitalWrite(motor_two_back, HIGH)
        delay(constant)
        digitalWrite(motor_two_back, LOW)
        digitalWrite(motor_one_back, HIGH)
        digitalWrite(motor_two_back, HIGH)
        delay(constant2)
        digitalWrite(motor_one_back, LOW)
        digitalWrite(motor_two_back, LOW)
      }
    }
    
    }
  }
  }
}

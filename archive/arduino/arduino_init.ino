#include <stdio.h>

int motor_one = //Digital Pin 1 (Motor on the left)
int motor_two = //Digital Pin 2 (Motor on the right)
int ultrasonic = //Analog Pin 5 (On the front of the robot)
int init_length = //Length of the Grid Area

void setup() {
  // put your setup code here, to run once:
  
  pinMode(motor_one, OUTPUT)
  pinMode(motor_two, OUTPUT)
  pinMode(ultrasonic, INPUT) 
  Serial.begin(9600);
  Serial.println("Starting...");

  digitalWrite(motor_one, HIGH)
  delay(//Dependant on the type of motor)
  digitalWrite(motor_one, LOW)
  delay(100)
  digitalWrite(motor_one, HIGH)
  digitalWrite(motor_two, HIGH)
  delay(//Dependant on the type of motor)
  digitalWrite(motor_one, LOW)
  digitalWrite(motor_two, LOW)
  digitalWrite(motor_two, HIGH)
  delay(//Dependant on the type of motor)
  digitalWrite(motor_two, LOW)
  
}

void loop() {
  int net = 0
  // put your main code here, to run repeatedly:
  while (net < init_length) {
    //Incomplete: Code that governs the robot's autonomous features.
  }
}

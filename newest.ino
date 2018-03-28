//We credit certain snipets of this code to Adafruit industries, and other developers who created the libraries and built-in functions for the specific sensors that we are usinf.

#include <Servo.h>
#include <SPI.h>
#include <string.h>
#include "DHT.h"
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_L3GD20_U.h>

#define DHTPIN 2
#define DHTTYPE DHT11

#include <Wire.h>
#include <Adafruit_AMG88xx.h>

Adafruit_AMG88xx amg;

int pin = A1;

float pixels[AMG88xx_PIXEL_ARRAY_SIZE];

Adafruit_L3GD20_Unified gyro = Adafruit_L3GD20_Unified(20);

void displaySensorDetails(void)
{
  sensor_t sensor;
  gyro.getSensor(&sensor);
  delay(500);
}


DHT dht(DHTPIN, DHTTYPE);

Servo myservo;
Servo myservo2;

void setup() {
  pinMode(pin, INPUT);
  // put your setup code here, to run once:
  gyro.enableAutoRange(true);
  myservo.attach(9);
  myservo2.attach(6);
dht.begin();
Serial.begin(115200);
randomSeed(analogRead(A0));

bool status;

status = amg.begin();
    if (!status) {
        Serial.println("Could not find a valid AMG88xx sensor, check wiring!");
        while (1);
    }
    


    delay(100);


if(!gyro.begin())
  {
    /* There was a problem detecting the L3GD20 ... check your connections */
    Serial.println("Ooops, no L3GD20 detected ... Check your wiring!");
    while(1);
  }

  displaySensorDetails();

}

int counter = 0;
int tree = 0;

void loop() {
  // put your main code here, to run repeatedly
  sensors_event_t event; 
  gyro.getEvent(&event);

  float one = dht.readHumidity();
  float two = dht.readTemperature();

  String temp = String((int) two);
  String hum = String((int) one);
  int distsensor, i;
  long t;


distsensor = 0;
for (i=0;i<8;i++) {
  distsensor += analogRead(A0);
  delay(50);
}
distsensor /= 8;

if (distsensor < 50) {
 myservo.write(0);
myservo2.detach();
delay(2000);
myservo2.attach(6);
myservo.write(0);
myservo2.write(180);
delay(2000);
myservo.detach();
delay(2500);
myservo.attach(9);
myservo2.attach(6);
myservo.write(0);
myservo2.write(180);
delay(3000);
myservo.detach();
myservo2.write(180);
delay(2000);
myservo.attach(9);
myservo.write(0);
myservo2.write(180);
delay(1000);
myservo2.detach();
myservo.write(0);
delay(2000);
myservo2.attach(6);
tree = tree + 1;
counter = counter + 4;
}
else {
  myservo.write(0);
myservo2.write(180);
counter = counter + 1;
delay(100);
}

int counter2 = 0;
    //read all the pixels
    amg.readPixels(pixels);
    for(int i=1; i<=AMG88xx_PIXEL_ARRAY_SIZE; i++){
      counter2 = counter2 + pixels[i-1];
    }

if (counter2/64 > 25) {
  myservo.detach();
  myservo2.detach();
}

    //delay a second

String a = String(distsensor);
String b = String(temp);
String c = String(hum);
String e = String(counter/8);
String f = String(counter2/64);
String g = String(analogRead(pin));
String h = String(tree);

if (counter%4 == 0) {

Serial.println("Distance: "+a+",Temperature: "+b+",Humidity: "+c+",Coordinates: "+e+",Thermal Camera: "+f+",Light: "+g+",Trees: "+h);

}

}

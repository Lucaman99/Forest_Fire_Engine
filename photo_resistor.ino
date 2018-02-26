//Basic code for photoresistor analog data

int outputpin = 3;
int inputpin = 2;
int analog = A1;
int analog2 = A2;

void setup() {
  // put your setup code here, to run once:
  pinMode(outputpin, OUTPUT);
  pinMode(inputpin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int data2 = analogRead(analog);
  int data = digitalRead(inputpin);
  int data3 = analogRead(analog2);
  if (data == LOW) {
    digitalWrite(outputpin, HIGH);
    Serial.println("The bottom = "+String(data2));
    Serial.println("The top = "+String(data3));
  }
  else {
    digitalWrite(outputpin, LOW);
  }
}

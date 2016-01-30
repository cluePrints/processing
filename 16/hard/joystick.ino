#include <Servo.h>

Servo servo1;
Servo servo2;

int ledPin = 13;
int joyPin1 = 0;                 // slider variable connecetd to analog pin 0
int joyPin2 = 1;                 // slider variable connecetd to analog pin 1
int value1 = 0;                  // variable to read the value from the analog pin 0
int value2 = 0;                  // variable to read the value from the analog pin 1
int oldValue1 = -1;
int oldValue2 = -2;

void setup() {
  pinMode(ledPin, OUTPUT);              // initializes digital pins 0 to 7 as outputs
  Serial.begin(9600);
  servo1.attach(9);
  servo2.attach(10);
}

int treatValue(int data) {
  return (data * 10 / 1024);
}

void loop() {
  // reads the value of the variable resistor
  value1 = analogRead(joyPin1);
  // this small pause is needed between reading
  // analog pins, otherwise we get the same value twice
  //delay(100);

  // reads the value of the variable resistor
  value2 = analogRead(joyPin2);

  //blynk();

  value1 = map(value1, 0, 1023, 170, 0);
  value2 = map(value2, 0, 1023, 170, 10);

  debugWrite(value1, value2);
  servo1.write(value1);
  servo2.write(value2);
  delay(100);
}

void debugWrite(int value1, int value2) {
  Serial.print("J ");
  Serial.print(value1);
  Serial.print(',');
  Serial.println(value2);
}

void blynk() {
  digitalWrite(ledPin, HIGH);
  delay(value1);
  digitalWrite(ledPin, LOW);
  delay(value2);
}

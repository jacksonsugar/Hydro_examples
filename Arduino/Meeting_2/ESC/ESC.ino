// Controlling a servo position using a potentiometer (variable resistor)  

#include <Servo.h> 
 
Servo esc1;  // create servo object to control a servo 
 
int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin 
 
void setup() 
{ 
  esc1.attach(3);  // attaches the servo on pin 3 to the servo object 
  esc1.write(1500);  // motor stop on startup
  delay(5000);
} 
 
void loop() 
{ 
  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023) 
  val = map(val, 0, 1023, 1100, 1900);     // scale it to use it with the servo (value between 0 and 180) 
  esc1.write(val);                  // sets the servo position according to the scaled value 
  delay(15);                           // waits for the servo to get there 
} 

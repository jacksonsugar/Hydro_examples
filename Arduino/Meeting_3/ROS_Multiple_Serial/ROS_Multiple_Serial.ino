
//#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
//else
//  #include <WProgram.h>
//#endif
#include <HardwareSerial.h>
#define SERIAL_CLASS HardwareSerial
#include <Servo.h> 
#include <ros.h>
#include <sensor_msgs/Joy.h>
#include <ArduinoHardware.h>

ros::NodeHandle nh;
//ros::NodeHandle_<ArdunioHardware, 2, 2, 150, 150> nh;

Servo esc1;
Servo esc2;
Servo esc3;
Servo esc4;

void esc_cb( const sensor_msgs::Joy& cmd_msg){
  int PWM1 = cmd_msg.axes[1] * 100;
  //PWM1 = PWM1 *10;
  PWM1 = map(PWM1, -100, 100, 1000, 2000);
  esc1.writeMicroseconds(PWM1); //set servo angle, should be from 0-180   

  int PWM2 = cmd_msg.axes[1] * 100;
  //PWM2 = PWM2 *1000;
  PWM2 = map(PWM2, -100, 100, 1000, 2000);
  esc2.writeMicroseconds(PWM2); //set servo angle, should be from 0-180   

  int PWM3 = cmd_msg.axes[1] * 100;
  //PWM3 = PWM3 *1000;
  PWM3 = map(PWM3, -100, 100, 1000, 2000);
  esc3.writeMicroseconds(PWM3);//set servo angle, should be from 0-180   


  int PWM4 = cmd_msg.axes[1] * 100;
  //PWM4 = PWM4 *1000;
  PWM4 = map(PWM4, -100, 100, 1000, 2000);
  esc4.writeMicroseconds(PWM4); //set servo angle, should be from 0-180   

}

ros::Subscriber<sensor_msgs::Joy> sub("joy", esc_cb);

void setup(){

  nh.initNode();
  nh.subscribe(sub);

  esc1.attach(3); //attach it to pin 3
  esc2.attach(5); //attach it to pin 5
  esc3.attach(6); //attach it to pin 6
  esc4.attach(9); //attach it to pin 9

}

void loop(){
  nh.spinOnce();
  delayMicroseconds(5);
}


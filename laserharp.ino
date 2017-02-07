
/*
 Laser Harp code for 7 beams using 30mW laser module, stepper motor 
 and a NPN transistor as switch

 */
//SoftwareSerial(2,3); // (Tx,Rx) for MIDI to serial communicate with Arduino


  
#include <Stepper.h>

int Laser=12;  // Base of the NPN transistor to control laser
int LaserDelay=5;
int counter=1;
int Motor=6;
int step1=2;
int ldr;
int c=10;
int prev_c,ic;
boolean Detect;
int sstep=0;

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor


// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() 
{
pinMode(Laser,OUTPUT);    //Input for laser to turn only at defined position
pinMode(A2,INPUT);       // Output from ldr to detect obstruction of beam 
myStepper.setSpeed(200);  // set the speed at 200 rpm:
Serial.begin(9600);     // Start a serial communication channel for MIDI
digitalWrite(Laser,HIGH);
delay(7000);
digitalWrite(Laser,LOW);  
delay(10000);
}

void detectfunc(int stp)
{ 
  if(ldr==HIGH)
  { if(stp<0)
    c=(-sstep/step1);
    else
    c=sstep/step1;
  }
   Serial.println(c);
   if(prev_c!=c)
   ic=0;
  switch(c)
  { case 0: Serial.print('a');
            break;
    case 1: Serial.print('b');
            break;
    case 2: Serial.print('c');
            break;
    case 3: Serial.print('d');
            break;
    case 4: Serial.print('e');
            break;
    case 5: Serial.print('f');
            break;
    case 6: Serial.print('g');
            break;
    case 7: Serial.print('h');
            break;              
    case 10:{ ic++;
       if(ic>20)
       Serial.print('z');}
            break;                                                  
  }
       
}    

void loop() 
{

 for(counter=0; counter<7; counter++)
  { //if (counter==1)
   //delay(10); 
   myStepper.step(step1);
   delay(Motor); 
   sstep+=step1;
   digitalWrite(Laser,HIGH); // Trigger laser ON if NPN transistor
    
   delay(3);
   ldr=analogRead(A2)>700;
 //  Serial.println(analogRead(A2));
   delay(2);
   
   digitalWrite(Laser,LOW);
   if(step1<0)
   detectfunc(-1);
   else
   detectfunc(1);

   prev_c=c;
 
 /*Detect= LDR();
   if(Detect==HIGH)
    { Serial.println("Beam no:");
      if(step1>0)
     Serial.println(counter);
     else
     Serial.println(8-counter);
    }
   
  */ 
  
  }
  

   
  
 // myStepper.step(179);
 //delay(50);
step1=(-step1);
 
}            





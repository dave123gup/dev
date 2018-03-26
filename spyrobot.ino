#include <SoftwareSerial.h>
char X;
int r1=3,r2=5,r3=10,r4=11;
void setup()
{
Serial.begin(9600);
pinMode(r1,OUTPUT);
pinMode(r2,OUTPUT);
pinMode(r3,OUTPUT);
pinMode(r4,OUTPUT);
}
void loop()
{
while(Serial.available()==0);
X=Serial.read();
Serial.print(X);
if(X=='F')
{
analogWrite(3,150);
analogWrite(5,0);
analogWrite(10,150);
analogWrite(11,0);

}
else
if(X=='B')
{
analogWrite(3,0);
analogWrite(5,150);
analogWrite(10,0);
analogWrite(11,150);
}
else
if(X=='L')
{
analogWrite(3,0);
analogWrite(5,0);
analogWrite(10,150);
analogWrite(11,0);
}
else
if(X=='R')
{
analogWrite(3,150);
analogWrite(5,0);
analogWrite(10,0);
analogWrite(11,0);
}
if(X=='S')
{
analogWrite(3,0);
analogWrite(5,0);
analogWrite(10,0);
analogWrite(11,0);
}
}

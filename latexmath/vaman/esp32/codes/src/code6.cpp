#include<Arduino.h>

//Declaring all variables as integers

int D0,D1,D2,CLK;
int Q0,Q1,Q2;

//Creating a function 

void ref(int D0,int D1,int D2,int CLK){
	digitalWrite(12,D0);
	digitalWrite(13,D1);
	digitalWrite(14,D2);
	digitalWrite(15,CLK);
}

//the setup function runs once when you press reset or power the board

void setup(){
	pinMode(12,OUTPUT);
	pinMode(13,OUTPUT);
	pinMode(14,OUTPUT);
	pinMode(15,OUTPUT);
	pinMode(16,INPUT);
	pinMode(17,INPUT);
	pinMode(18,INPUT);
}

//the loop function runs over and over again

void loop(){
	digitalWrite(15,HIGH);
	delay(1000);

	Q0=digitalRead(16);
	Q1=digitalRead(17);
	Q2=digitalRead(18);
	D2=(Q2&&!Q0) || (Q0&&!Q2);
	D1=(Q2);
	D0=(Q1);
	
	digitalWrite(15,LOW);

	ref(D0,D1,D2,CLK);
}

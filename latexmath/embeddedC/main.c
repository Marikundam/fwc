#include <avr/io.h>
#include <util/delay.h>

 int main (void)
{
	int P,Q,R;
	int F;
//set 2,3,4 pins as input of arduino
DDRD &= ~(1<<PD2)&(1<<PD3)&(1<<PD4);

DDRB |= (1<<PB5); //13 output
	
  while (1) {
	  P =(PIND & (1<<PIND2)) == (1<<PIND2);
	  Q =(PIND & (1<<PIND3)) == (1<<PIND3);
	  R =(PIND & (1<<PIND4)) == (1<<PIND4);
	  F =(R&&(!Q))||(P&&Q);
 PORTB = (F<<5);
    
  }

  return 0;

}

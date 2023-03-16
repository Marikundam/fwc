.include "/sdcard/arduino/fwc/assembly/m328Pdef.inc"
ldi r16,0b01111100
out DDRD,r16
ldi r17,0b11111111
out PORTD,r17
ldi r16,0b00000001
out DDRB,r16

loop:
 in r17,PIND

;Taking T
ldi r24,0b00000100
mov r18,r17
and r18,r24
ldi r25,0b00000010
loopt:
lsr r18
dec r25
brne   loopt
.DEF T =r18

;Taking S
ldi r24,0b00001000
mov r19,r17
and r19,r24
ldi r25,0b00000011
loops:
lsr r19
dec r25
brne   loops
.DEF S =r19

;Taking R
ldi r24,0b00010000
mov r20,r17
and r20,r24
ldi r25,0b00000100
loopr:
lsr r20
dec r25
brne   loopr
.DEF R =r20

;Taking Q 
ldi r24,0b00100000
mov r21,r17
and r21,r24
ldi r25,0b00000101
loopq:
lsr r21
dec r25
brne   loopq
.DEF Q =r21

;Taking P
ldi r24,0b01000000
mov r22,r17
and r22,r24
ldi r25,0b00000110
loopp:
lsr r22
dec r25
brne   loopp
.DEF P =r22

ldi r23,0x00
ldi r24,0x00
ldi r26,0x00
ldi r27,0x00
ldi r28,0x00
.DEF A1 = r23
.DEF A2 = r24
.DEF A3 = r26
.DEF A4 = r27
.DEF A5 = r28

mov A2,S
mov A3,R
and A2,A3
mov A4,Q
mov A5,P
and A4,A5
and A4,A2
mov A1,T
com A1
mov A2,S
mov A3,R
and A3,A2
and A1,A3
or A1,A4
out PORTB,A1

rjmp loop

Start:
rjmp Start

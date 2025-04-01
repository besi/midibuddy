from machine import UART, Pin
import time
import binascii
import struct

midi_baud = 31250
tx = 36
rx = 35
uart=UART(1, baudrate=midi_baud, bits=8, tx=tx, rx=rx, invert=UART.INV_RX)

# Midi IN (weird bytes being received?)
# Middle C pressed as hard as possible and then released
# 28 2 28 254
# Middle C Pressed softly
# 28 250 28 254 
# Middle C pressed quickly
# 28 74 152 

while False:
    if uart.any():
        msg = uart.read(2)
        m = struct.unpack('B', msg)[0]
        if m != 0:
            #print(int.from_bytes(msg), end=' ')
            #print(binascii.hexlify(msg).decode(), end='.')
            print(m,end=' ')


# MIDI OUT
notes = [60,61,62,63,64,63,62,61]
delay = 0.5

while True:
  for x in notes:
    print(f"Sending Midi note #{x}...", end= '')
    uart.write(struct.pack("bbb",0x90,x,77))
    time.sleep(delay)
    uart.write(struct.pack("bbb",0x80,x,0))
    uart.write(struct.pack("bbb",0x80,x,0))
    print(" Note off")
    time.sleep(delay)

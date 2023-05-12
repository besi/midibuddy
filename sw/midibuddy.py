import machine
uart = machine.UART(0,31250)


print("Detaching REPL (use webrepl)")
import os
os.dupterm(None, 1)
import time

# MIDI IN
while True:
    if (uart.any()):
        print(uart.read())




# MIDI OUT
notes = [60,61,62,63,64,63,62,61]
import ustruct
import time

while True:
  for x in notes:
    print("note")
    uart.write(ustruct.pack("bbb",0x90,x,127))
    time.sleep(0.5)
    time.sleep(0.5)
    uart.write(ustruct.pack("bbb",0x80,x,0))
    

import serial
import keyboard

ser = serial.Serial('/dev/cu.usbserial-210', 115200)

while True:
  line = ser.readline().decode('utf-8')
  line = int(line)

  if line == 1:
    keyboard.press_and_release('space')                                                   

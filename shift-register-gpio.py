import RPi.GPIO as GPIO
import time

SDI   = 10  # BCM10 - physical pin 19
RCLK  = 8   # BCM8 - physical pin 24
SRCLK = 11  # BCM11- physical pin 23

CLK_TIME = 0.05

def setup():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)   # BCM pin numbering
  GPIO.setup(SDI, GPIO.OUT)
  GPIO.setup(RCLK, GPIO.OUT)
  GPIO.setup(SRCLK, GPIO.OUT)
  GPIO.output(SDI, GPIO.LOW)
  GPIO.output(RCLK, GPIO.LOW)
  GPIO.output(SRCLK, GPIO.LOW)

def pulse_clk(clk):
  GPIO.output(clk, GPIO.LOW)
  time.sleep(CLK_TIME)
  GPIO.output(clk, GPIO.HIGH)
  time.sleep(CLK_TIME)

def send_byte(byte):
  GPIO.output(SDI,GPIO.LOW)
  GPIO.output(RCLK,GPIO.LOW)
  bitarray = [int(b) for b in format(byte, '08b')]
  for bit in bitarray:
    GPIO.output(SDI, bit)
    # when you pulse SRCLK, bits in SR move one stage over
    pulse_clk(SRCLK) 
    # when you pulse RCLK, shift register contents are copied 
    # to storage register, which is connected to outputs QA–QH
    #pulse_clk(RCLK)  
  GPIO.output(RCLK,GPIO.HIGH)
  GPIO.output(SDI,GPIO.LOW)

if __name__ == '__main__': 
  setup() 
  send_byte(0b111111111111111111111111)
  print("all white")
  # sleep, just so that you have a chance to see final output
  time.sleep(5)
  send_byte(0b111111110000000000000000)#red
  print("all red")
  time.sleep(5)
  send_byte(0b000000001111111100000000)#blue
  print("all blue")
  time.sleep(5)
  send_byte(0b000000000000000011111111)#green
  print("all green")
  time.sleep(5)
  send_byte(0b101010101010101010101010)#every other LED whie
  time.sleep(5)
  send_byte(0b010101010101010101010101)
  time.sleep(5)
  send_byte(0b000000000000000000000000)
  GPIO.cleanup()

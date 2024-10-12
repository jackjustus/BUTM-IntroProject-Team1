from time import time_ns, sleep, time
import RPi._GPIO as g
trigger_pulse = 10000
pulse_width = 100000000
g.setmode(g.BCM)
g.setwarnings(False)

trigger_pin = 2     # Corresponds to pin 3
reader_pin = 3      # Corresponds to pin 5

g.setup(trigger_pin, g.OUT)
g.setup(reader_pin, g.IN)

def get_distance(t,r):
    g.output(t,g.HIGH)
    start_time = time_ns()
    #sleep(trigger_pulse)
    #g.output(t,g.LOW)
    flag = False
    pulse_length= 0
    high_start = 0
    
    while not flag:
        if time_ns()-start_time >= trigger_pulse:
            g.output(t, g.LOW)
            while time_ns()-start_time <= pulse_width:
                out = g.input(r)
                if out ==1 and not flag:
                    high_start = time_ns()
                    flag = True
                if out == 0 and flag:
                    pulse_length = time_ns()-high_start
                    break
    return round(pulse_length/58000,3)

stime = time()

while time()-stime <30:
    print(get_distance(trigger_pin, reader_pin))
    sleep(0.2)
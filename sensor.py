
from time import time_ns, sleep, time
import RPi._GPIO as g
import constants
trigger_pulse = 10000
pulse_width = 100000000
g.setmode(g.BCM)
g.setwarnings(False)



class sensor_data_collector:
    def __init__(self, trigger_pin: int, ultrasonic_read_pin:int, ir_read_pin:int):
        self.trigger_pin = trigger_pin
        self.us_read_pin = ultrasonic_read_pin
        self.ir_read_pin = ir_read_pin
        g.setup(self.trigger_pin, g.OUT)
        g.setup(self.us_read_pin, g.IN)
        g.setup(self.ir_read_pin, g.IN)

    def get_distance(self):
        g.output(self.trigger_pin,g.HIGH)
        start_time = time_ns()
        flag = False
        pulse_length= 0
        high_start = 0
        
        while not flag:
            if time_ns()-start_time >= trigger_pulse:
                g.output(self.trigger_pin, g.LOW)
                while time_ns()-start_time <= pulse_width:
                    out = g.input(self.us_read_pin)
                    if out ==1 and not flag:
                        high_start = time_ns()
                        flag = True
                    if out == 0 and flag:
                        pulse_length = time_ns()-high_start
                        break
        return round(pulse_length/58000,3)

    def is_close(self):
        #reads value and choses output as approprate
        match g.input(self.ir_read_pin):
            case 0:
                return True
            case 1:
                return False
            case _:
                print("ERROR HAS OCCURED WITH IR SENSOR IN [is_close()]")
                return None
stime = time()
sensor = sensor_data_collector(constants.trigger_pin, constants.ultrasonic_read_pin, constants.ir_read_pin)
while time()-stime <10:
    print(sensor.get_distance())
    print(sensor.is_close())
    sleep(0.2)
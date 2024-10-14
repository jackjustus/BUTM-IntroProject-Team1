
from time import time_ns, sleep, time, asctime, localtime
import RPi._GPIO as g
import csv
import constants
trigger_pulse = 10000
pulse_width = 100000000
g.setmode(g.BCM)
g.setwarnings(False)



class sensor_data_collector:
    def __init__(self, trigger_pin: int, ultrasonic_read_pin:int, ir_read_pin:int, current_time):
        self.trigger_pin = trigger_pin
        self.us_read_pin = ultrasonic_read_pin
        self.ir_read_pin = ir_read_pin
        self.start_time = time()
        self.current_time = current_time
        g.setup(self.trigger_pin, g.OUT)
        g.setup(self.us_read_pin, g.IN)
        g.setup(self.ir_read_pin, g.IN)

    def reset_start_time(self):
        self.start_time = time()
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
    def get_distance_timestamped(self):
        return (self.get_distance(),time()-self.start_time)
    
    def is_close_timestamped(self):
        return (self.is_close(),time()-self.start_time)
    
    def get_data_timestamped(self):
        return (self.get_distance(),self.is_close(), time()-self.start_time)
    
    def collect_data(self):
        za_data = self.get_data_timestamped()
        name = asctime(localtime(self.current_time)).replace(' ', '_')
        name = name.replace(':', '-')
        with open(f'data_{name}.csv', 'w', newline= '') as c:
           # writer = csv.writer(c)
           # writer.writerows(za_data)
           c.write(str(za_data))
           c.write('\n')
        print(za_data)
        return za_data

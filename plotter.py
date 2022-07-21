import matplotlib.pyplot as plt
import serial
import random
import time

xdata, ydata = [], []
while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(1)
        line = ser.readline()
        s = line.decode()
        o = ""
        for i in s:
            if(i.isdigit()):
                o += i
        xdata.append(time.time())
        ydata.append(int(o))
        plt.plot(xdata, ydata, 'r-')
        plt.xlabel('time')
        plt.ylabel('distance')
        plt.title('Proximity output')
        plt.pause(2)
        plt.draw()
        
    except KeyboardInterrupt:
        exit()

import odrive
import csv
from timeloop import Timeloop
from datetime import timedelta

data = [[0, 0]]

tl = Timeloop()

filename = "test1.csv"

@tl.job(interval=timedelta(seconds=1))
def get_data():
    
    data.append([my_drive.axis0.motor.current_control.Iq_setpoint, my_drive.vbus_voltage])



tl.start()

my_drive = odrive.find_any()
my_drive.axis0.requested_state = 3

input("Calibrating. Press Enter after calibration is done to set the Odrive in position control mode.")

my_drive.axis0.requested_state = 8

input("Press Enter to start logging data. Ctrl+C or Del to stop.")
    
while True:
    try:
        print("...")
    except KeyboardInterrupt:
        tl.stop()
        break

with open(filename, 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(data)

print("Done writing to file " + filename)

import serial
import sys
import glob
import hello as time
import csv
import os
import time as sleep

count = 0

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

port = serial_ports()
if not port:
    print("No port is found!!")
    sleep.sleep(2)
    print("Closing")
    sleep.sleep(1)
    exit()

i = 1
for p in port:
    print(i,")",port)
    i=i+1

port_number = input("Choose your port No: ")
port_number = int(port_number)
if(port_number<i):
    print("Selected ", port[port_number-1])
else:
    print("Wrong port number")
    sleep.sleep(2)
    print("Closing")
    sleep.sleep(1)
    exit()
PORT = port[port_number-1]

try:
    ser = serial.Serial(PORT, '9600')
    print("PORT STARTED")
except SerialException:
    print("Serial port error!!")

ser.flushInput()
if not os.path.exists('data'):
    print("Created a DATA Folder")
    os.mkdir('data')

with open("data/"+time.fileName(), 'w', newline='') as file:
    writer = csv.writer(file)
    ser_bytes = ser.readline()
    print(ser_bytes.decode('utf-8'))
    writer.writerow(["SL No", "timeStamp", "Humidity", "Temperature"])

    while(1):
        try:
            ser_bytes = ser.readline()
            ser_bytes = ser_bytes.decode('utf-8').strip()
            ser_bytes = ser_bytes.split(" ")
            write = csv.writer(file, delimiter = ",")
            count = count + 1
            print(count, time.timeStamp(), ser_bytes[0], ser_bytes[1])
            writer.writerow([count, time.timeStamp(), ser_bytes[0], ser_bytes[1]])
            
        except:
            print("keyboard Interrupt")
            ser.close()
            count = 0
            break
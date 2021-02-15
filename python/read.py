import serial
import hello as time
import csv
count = 0

ser = serial.Serial('/dev/tty.usbmodem14201', '9600')
ser.flushInput()

with open(time.fileName(), 'w') as file:
    
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
    


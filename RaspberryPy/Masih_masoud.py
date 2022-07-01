import serial
import getch
serialport = serial.Serial ("/dev/ttyS0")
serialport.baudrate = 115200
front_cnt =  0
while(True):
    x = getch.getch()
    if(x=='w'):
        command="+200+20015+00"
    elif(x=='s'):
        command="-200-20015+00"
    elif(x=='a'):
        command="-100+10015+00"
    elif(x=='d'):
        command="+100-10015+00"
    elif(x=='b'):
        command="+000+00015+00"
    elif(x=="h"):
        command="+200+18015+00"
    elif(x=="f"):
        command="+180+20015+00"
    elif(x=="t"):
        command="-200-18015+00"
    elif(x=="g"):
        command="-180-20015+00"
    else:
        command="+000+00015+00"
        serialport.write(command.encode())
        break
    # type your code here
    serialport.write(command.encode())
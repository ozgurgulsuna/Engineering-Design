import serial
from serial.tools import list_ports



def main():
    print("Hello World!")
    # Device IDs are mapped as:
    #   ST-right
    #   ST-middle
    #   ST-left
    ser = serial.Serial('/dev/ST-right') # open serial port
    print(ser.name)             # check which port was really used

    while True:
        message = ser.readline().decode('utf-8')
        print(message)
        if message != "":
            print("Message received")
            command = input("Command to be sent:")
            ser.write(command.encode('utf-8'))

    # ser.close()             # close port

if __name__ == "__main__":
    main()

import serial
import numpy as np
import time


def main():
    print("Hello World!")
    ser1 = serial.Serial('COM9') # open serial port
    print(ser1.name)             # check which port was really used
    """
    ser2 = serial.Serial('COM9') # open serial port
    print(ser2.name)             # check which port was really used
    """
    while True:
        received_message = ser1.readline()
        move_inner = (5)
        move_middle = (-1)
        move_outer = (0)
        move_initialize_command = 'i'
        
        sent_message = move_initialize_command.encode('utf-8') + move_inner.to_bytes(2, 'big', signed = True) + move_middle.to_bytes(2, 'big', signed = True) \
            + move_outer.to_bytes(2, 'big', signed = True)
        

        if received_message != "":
            print("Message received")
            print(received_message)
            # command = input("Command to be sent:")
            print(sent_message)
            ser1.write(sent_message)


        """
        received_message = ser1.readline()
        move_x = (0)
        move_y = (-5)
        move_command = 'm'
        
        sent_message = move_command.encode('utf-8') + move_x.to_bytes(2, 'big', signed = True) + move_y.to_bytes(2, 'big', signed = True)
        """

        """
        if received_message != "":
            print("Message received")
            print(received_message)
            # command = input("Command to be sent:")
            print(sent_message)
            ser1.write(sent_message)
        """


        """
        received_message = ser2.readline().decode('utf-8')
        print(received_message)
        if received_message != "":
            print("Message received")
            command = input("Command to be sent:")
            ser2.write(command.encode('utf-8'))
        """

    # ser.close()             # close port

if __name__ == "__main__":
    main()

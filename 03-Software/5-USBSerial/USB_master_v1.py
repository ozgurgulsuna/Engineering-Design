import serial
import numpy as np
import time


def main():
    # Define commands
    move_initialize_command = 'i'
    move_command = 'm'
    shutdown_command = 's'
    error_command = 'e'

    print("Hello World!")

    # Establish connection with the serial ports
    ser1 = serial.Serial('COM9') # open serial port
    print(ser1.name)             # check which port was really used
    """
    ser2 = serial.Serial('COM10') # open serial port
    print(ser2.name)             # check which port was really used
    
    ser3 = ser2 = serial.Serial('COM11') # open serial port
    print(ser2.name)                    # check which port was really used
    """

    # Start initializing the system by moving it manually
    cont_initializing = 1

    while cont_initializing == 'y':
        
        move_inner = int(input("Enter the displacement for the inner motor (in mm): "))
        move_middle = int(input("Enter the displacement for the middle motor (in mm): "))
        move_outer = int(input("Enter the displacement for the outer motor (in mm): "))
        
        sent_message = move_initialize_command.encode('utf-8') + move_inner.to_bytes(2, 'big', signed = True) \
            + move_middle.to_bytes(2, 'big', signed = True) + move_outer.to_bytes(2, 'big', signed = True)
        
        print(sent_message)
        print('')
        ser1.write(sent_message)

        # 'y' if initialization should be continued
        cont_initializing = input("Continue initializing?: ")


    # Initialize cameras, take background pictures, etc.
    # ADD THE NECESSARY CODES HERE

    while True:
        
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

# This function will include the whole python code for running image processing to extract move_x & move_y
def get_xy():
    # return delta_x, delta_y
    pass

if __name__ == "__main__":
    main()

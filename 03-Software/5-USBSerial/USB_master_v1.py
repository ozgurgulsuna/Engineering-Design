import serial
import numpy as np
import time


def main():
    # Define commands
    move_initialize_command = 'i'
    move_command = 'm'
    shutdown_command = 's'
    error_command = 'e'
    begin_command = 'b'

    print("Hello World!")

    # Establish connection with the serial ports
    ser_right = serial.Serial('/dev/ST-right') # open serial port
    print(ser_right.name)             # check which port was really used
    """
    ser_middle = serial.Serial('/dev/ST-middle') # open serial port
    print(ser_middle.name)             # check which port was really used
    
    ser_left = serial.Serial('/dev/ST-left') # open serial port
    print(ser_left.name)                    # check which port was really used
    """

    # Start initializing the system by moving it manually
    right_pole_initialize = input("Start initializing right pole ('y' if 'yes'): ")

    while right_pole_initialize == 'y':
        
        move_inner = int(input("Enter the displacement for the inner motor (in mm): "))
        move_middle = int(input("Enter the displacement for the middle motor (in mm): "))
        move_outer = int(input("Enter the displacement for the outer motor (in mm): "))
        
        sent_message = move_initialize_command.encode('utf-8') + move_inner.to_bytes(2, 'big', signed = True) \
            + move_middle.to_bytes(2, 'big', signed = True) + move_outer.to_bytes(2, 'big', signed = True)
        
        print(sent_message)
        print('')
        ser_right.write(sent_message)

        # 'y' if initialization should be continued
        right_pole_initialize = input("Continue initializing?: ")
    
    # Send command to set the motor position related values to 0
    sent_message = begin_command.encode('utf-8')
    print(sent_message)
    print('')
    ser_right.write(sent_message)
    
    
    """
    # Start initializing the system by moving it manually
    left_pole_initialize = input("Start initializing left pole ('y' if 'yes'): ")

    while left_pole_initialize == 'y':
        
        move_inner = int(input("Enter the displacement for the inner motor (in mm): "))
        move_middle = int(input("Enter the displacement for the middle motor (in mm): "))
        move_outer = int(input("Enter the displacement for the outer motor (in mm): "))
        
        sent_message = move_initialize_command.encode('utf-8') + move_inner.to_bytes(2, 'big', signed = True) \
            + move_middle.to_bytes(2, 'big', signed = True) + move_outer.to_bytes(2, 'big', signed = True)
        
        print(sent_message)
        print('')
        ser_left.write(sent_message)

        # 'y' if initialization should be continued
        left_pole_initialize = input("Continue initializing?: ")
    
    # Send command to set the motor positio related values to 0
    sent_message = begin_command.encode('utf-8')
    print(sent_message)
    print('')
    ser_left.write(sent_message)
    """
    
    # Initialize cameras, take background pictures, etc.
    # ADD THE NECESSARY CODES HERE
    
    while True:
        
        # [move_x, move_y] = get_xy()
        move_x = int(input("Displacement in X axis (in mm): "))
        move_y = int(input("Displacement in Y axis (in mm): "))
        
        # Send move command
        sent_message = move_command.encode('utf-8') + move_x.to_bytes(2, 'big', signed = True) + move_y.to_bytes(2, 'big', signed = True)
        ser_right.write(sent_message)
        # ser_middle.write(sent_message)
        # ser_left.write(sent_message)
        
        # Wait for acknowledge
        received_message = ser_right.readline().decode('utf-8')
        print(received_message)
        
        # If not acknowledged, shutdown
        if received_message != 'a'
            # sent_message = shutdown_command.encode('utf-8')
            # ser_right.write(sent_message)
            # ser_middle.write(sent_message)
            # ser_left.write(sent_message)
        
        """
        # Wait for acknowledge
        received_message = ser_middle.readline().decode('utf-8')
        print(received_message)
        
        # If not acknowledged, shutdown
        if received_message != 'a'
            # sent_message = shutdown_command.encode('utf-8')
            # ser_right.write(sent_message)
            # ser_middle.write(sent_message)
            # ser_left.write(sent_message)
        
        # Wait for acknowledge
        received_message = ser_left.readline().decode('utf-8')
        print(received_message)
        
        # If not acknowledged, shutdown
        if received_message != 'a'
            # sent_message = shutdown_command.encode('utf-8')
            # ser_right.write(sent_message)
            # ser_middle.write(sent_message)
            # ser_left.write(sent_message)
        """

    # ser_right.close()             # close port
    # ser_middle.close()             # close port
    # ser_left.close()             # close port

# This function will include the whole python code for running image processing to extract move_x & move_y
def get_xy():
    # return delta_x, delta_y
    pass

if __name__ == "__main__":
    main()

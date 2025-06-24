""" DEMOOOOO
serial_comm.py - FaceLockR Arduino Communication Module
Handles all serial communication between Python and Arduino
"""

import serial
import serial.tools.list_ports
import time

class FaceLockSerial:
    def __init__(self, baudrate=9600, timeout=1):
        """
        Initialize serial connection
        :param baudrate: Communication speed (must match Arduino)
        :param timeout: Read timeout in seconds
        """
        self.port = None
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def detect_arduino(self):
        """Auto-detect Arduino COM port"""
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if 'Arduino' in port.description or 'CH340' in port.device:
                self.port = port.device
                return True
        return False

    def connect(self):
        """Establish serial connection"""
        try:
            if not self.port and not self.detect_arduino():
                raise Exception("Arduino not found!")

            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)  # Wait for Arduino reset
            return True
            
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            return False

    def send_command(self, command):
        """
        Send single-character command to Arduino
        :param command: 'U' (unlock) or 'L' (lock)
        """
        if self.serial_conn and self.serial_conn.is_open:
            try:
                self.serial_conn.write(command.encode('ascii'))
                return True
            except:
                print("Failed to send command")
        return False

    def close(self):
        """Close serial connection"""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

# Example Usage
if __name__ == "__main__":
    fl_serial = FaceLockSerial()
    
    if fl_serial.connect():
        print("Connected to Arduino!")
        
        # Test unlock/lock cycle
        fl_serial.send_command('U')  # Unlock
        time.sleep(3)
        fl_serial.send_command('L')  # Lock
        
        fl_serial.close()
    else:
        print("Could not connect to Arduino")
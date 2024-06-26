"""
    PCA9629A Micropython CLI
    Copyright (C) 2024  David Verbeek
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from machine import Pin, I2C
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=10000000)

def setAddress():
    address = int(input("What is the hex address of the board: 0x"),16)
    return address

def writeRegister(address):
    register = int(input("What register: 0x"),16)
    print("              76543210")
    value = int(input("What value: 0b"),2)
    output=register.to_bytes(1,"big")+value.to_bytes(1,"big")
    i2c.writeto(address, output)

def busScan():
    print(i2c.scan())

def readRegister(address):
    register = int(input("What register: 0x"),16)
    i2c.writeto(address, register.to_bytes(1,"big"))
    value = i2c.readfrom(address+1,1)
    print(value)

def stepCount(address):
    i2c.writeto(address, b"0x9f")
    value = i2c.readfrom(address+1,4)
    print(value)

def getAction():
    while True:
        action = input("Enter action:\n'scan' to scan the i2c bus\n'addr' to set i2c address\n'write' to write to a register\n"+
                       "'read' to read from a register\n'steps' to get read the"+
                        " number of steps taken\n'quit' to well quit\n:")
        if action in ["addr", "quit", "write", "scan", "read", "steps"]:
            return action
        else:
            print("Invalid entry.")

def main():
    quit = False
    busScan()
    address = setAddress()
    while not quit:
        action = getAction()
        if action == "addr":
            address = setAddress()
        elif action == "write":
            writeRegister(address)
        elif action == "read":
            readRegister(address)
        elif action == "scan":
            busScan()
        elif action == "steps":
            stepCount(address)
        elif action == "quit":
            print("For your sake I hope this worked better this time")
            quit = True
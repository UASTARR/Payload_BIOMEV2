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

def getAddress():
    address = int(input("what is the hex address of the board: 0x"),16)
    return address

def getAction():
    while True:
        action = input("Enter n for new adress, w for write to register, q for quit: ")
        if action in ["n", "q", "w"]:
            return action
        else:
            print("Invalid entry.")

def writeRegister(address):
    register = int(input("what register: 0x"),16)


def main():
    address = getAddress()
    quit = False
    while not quit:
        action = getAction()
        if action == "n":
            address = getAddress()
        elif action == "w":
            writeRegister(address)
        elif action == "q":
            quit = True

    print("for your sake I hope this worked better this time")

main()
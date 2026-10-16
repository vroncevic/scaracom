# -*- coding: UTF-8 -*-

'''
Module
    idriver.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    scaracom is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    scaracom is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Interface protocol for physical serial communication drivers.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ISerialDriver(Protocol):
    '''
        Defines structural contract for low-level serial communication drivers.

        It defines:

            :methods:
                | open - Opens connection to specified serial port endpoint.
                | close - Closes active physical serial communication port.
                | read - Reads raw byte payload of specified size from stream.
                | write - Transmits raw binary payload over serial connection.
                | is_open - Checks whether underlying serial port is open.
    '''

    def open(self, port: str, baudrate: int, timeout: float) -> bool:
        '''
            Opens connection to specified serial port endpoint.

            :param port: Device port path identifier (e.g. '/dev/ttyUSB0').
            :param baudrate: Communication transmission baud rate.
            :param timeout: Read timeout in seconds.
            :return: True if port opened successfully, False otherwise.
            :exceptions: None.
        '''

    def close(self) -> None:
        '''
            Closes active physical serial communication port.

            :exceptions: None.
        '''

    def read(self, size: int) -> bytes:
        '''
            Reads raw byte payload of specified size from stream.

            :param size: Number of bytes to read from buffer.
            :return: Read bytes from serial port.
            :exceptions: None.
        '''

    def write(self, data: bytes) -> int:
        '''
            Transmits raw binary payload over serial connection.

            :param data: Binary byte payload to write.
            :return: Number of bytes successfully transmitted.
            :exceptions: None.
        '''

    def is_open(self) -> bool:
        '''
            Checks whether underlying serial port is open.

            :return: True if serial port is currently open, False otherwise.
            :exceptions: None.
        '''

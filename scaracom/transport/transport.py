# -*- coding: UTF-8 -*-

'''
Module
    transport.py
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
    Hardware serial communication transport implementation.
'''

from __future__ import annotations

from threading import Lock
from typing import Final

from scaracom.transport.driver.idriver import ISerialDriver

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SerialTransport:
    '''
        Serial communication transport executing physical byte I/O over ISerialDriver.

        It defines:

            :attributes:
                | _driver - Injected physical serial driver instance.
                | _read_lock - Thread lock for stream reading synchronization.
                | _write_lock - Thread lock for stream writing synchronization.
                | _state_lock - Thread lock for connection lifecycle synchronization.
            :methods:
                | __init__ - Initializes serial transport with driver.
                | is_connected - Returns connection state.
                | connect - Establishes communication connection.
                | disconnect - Closes active connection.
                | read_bytes - Reads raw byte packet from communication stream.
                | write_bytes - Transmits raw byte packet.
    '''

    _driver: ISerialDriver
    _read_lock: Lock
    _write_lock: Lock
    _state_lock: Lock

    def __init__(self, driver: ISerialDriver) -> None:
        '''
            Initializes serial transport with injected driver.

            :param driver: Injected ISerialDriver instance.
            :exceptions: None.
        '''
        self._driver: Final[ISerialDriver] = driver
        self._read_lock: Final[Lock] = Lock()
        self._write_lock: Final[Lock] = Lock()
        self._state_lock: Final[Lock] = Lock()

    def is_connected(self) -> bool:
        '''
            Returns connection state.

            :return: True if connected, False otherwise.
            :exceptions: None.
        '''
        with self._state_lock:
            return self._driver.is_open()

    def connect(self, port: str, baudrate: int) -> bool:
        '''
            Establishes communication connection.

            :param port: Device address or port identifier.
            :param baudrate: Transmission baud rate.
            :return: True if connected successfully, False otherwise.
            :exceptions: None.
        '''
        with self._state_lock, self._read_lock, self._write_lock:
            return self._driver.open(port=port, baudrate=baudrate, timeout=0.1)

    def disconnect(self) -> None:
        '''
            Closes active connection.

            :exceptions: None.
        '''
        with self._state_lock, self._read_lock, self._write_lock:
            self._driver.close()

    def read_bytes(self, size: int) -> bytes:
        '''
            Reads raw byte packet from communication stream.

            :param size: Number of bytes to read.
            :return: Read byte payload.
            :exceptions: None.
        '''
        with self._read_lock:
            return self._driver.read(size)

    def write_bytes(self, data: bytes) -> bool:
        '''
            Transmits raw byte packet.

            :param data: Binary payload to send.
            :return: True if transmitted, False otherwise.
            :exceptions: None.
        '''
        with self._write_lock:
            return self._driver.write(data) > 0

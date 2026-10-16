# -*- coding: UTF-8 -*-

'''
Module
    pyserial_driver.py
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
    Physical serial communication driver using pyserial.
'''

from __future__ import annotations

from serial import Serial, SerialBase, SerialException, serial_for_url

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class PySerialDriver:
    '''
        Hardware serial driver adapter encapsulating pyserial communication.

        It defines:

            :attributes:
                | _serial - Internal active serial communication handle.
            :methods:
                | __init__ - Initializes driver instance.
                | open - Opens connection to specified serial port endpoint.
                | close - Closes active physical serial communication port.
                | read - Reads raw byte payload of specified size from stream.
                | write - Transmits raw binary payload over serial connection.
                | is_open - Checks whether underlying serial port is open.
    '''

    _serial: SerialBase | None

    def __init__(self) -> None:
        '''
            Initializes driver with empty serial handle.

            :exceptions: None.
        '''
        self._serial = None

    def is_open(self) -> bool:
        '''
            Checks whether underlying serial port is open.

            :return: True if serial port is currently open, False otherwise.
            :exceptions: None.
        '''
        return bool(self._serial is not None and self._serial.is_open)

    def open(self, port: str, baudrate: int, timeout: float) -> bool:
        '''
            Opens connection to specified serial port endpoint.

            :param port: Device port path identifier (e.g. '/dev/ttyUSB0').
            :param baudrate: Communication transmission baud rate.
            :param timeout: Read timeout in seconds.
            :return: True if port opened successfully, False otherwise.
            :exceptions: None.
        '''
        self.close()

        try:
            if '://' in port:
                self._serial = serial_for_url(port, baudrate=baudrate, timeout=timeout)
            elif ':' in port and not port.startswith('/'):
                self._serial = serial_for_url(
                    f'socket://{port}', baudrate=baudrate, timeout=timeout
                )
            else:
                self._serial = Serial(port=port, baudrate=baudrate, timeout=timeout)

            return True

        except (OSError, SerialException):
            self._serial = None

            return False

    def close(self) -> None:
        '''
            Closes active physical serial communication port.

            :exceptions: None.
        '''
        if self._serial is not None:
            try:
                self._serial.close()

            except (OSError, SerialException, TypeError, AttributeError):
                pass

            finally:
                self._serial = None

    def read(self, size: int) -> bytes:
        '''
            Reads raw byte payload of specified size from stream.

            :param size: Number of bytes to read from buffer.
            :return: Read bytes from serial port.
            :exceptions: None.
        '''
        if not self.is_open() or self._serial is None:
            return b''

        try:
            return self._serial.read(size)

        except (OSError, SerialException):
            self.close()

            return b''

    def write(self, data: bytes) -> int:
        '''
            Transmits raw binary payload over serial connection.

            :param data: Binary byte payload to write.
            :return: Number of bytes successfully transmitted.
            :exceptions: None.
        '''
        if not self.is_open() or self._serial is None:
            return 0

        try:
            count = self._serial.write(data)
            self._serial.flush()

            return count

        except (OSError, SerialException):
            self.close()

            return 0

# -*- coding: UTF-8 -*-

'''
Module
    port_scanner.py
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
    Hardware serial port scanner adapter component.
'''

from __future__ import annotations

from sys import platform
from typing import ClassVar

from serial.tools.list_ports import comports

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class PortScanner:
    '''
        Discovers and enumerates available serial communication endpoints on host machine.

        It defines:

            :attributes:
                | LINUX_DEFAULT_PORTS - Standard Linux serial device paths.
                | WINDOWS_DEFAULT_PORTS - Standard Windows COM port identifiers.
                | DARWIN_DEFAULT_PORTS - Standard macOS USB serial device paths.
            :methods:
                | scan_ports - Discovers and returns available serial port identifiers with descriptions.
                | get_default_ports - Returns fallback port identifiers for target OS platform.
                | get_version - Returns component version string.
    '''

    LINUX_DEFAULT_PORTS: ClassVar[tuple[str, ...]] = (
        '/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1'
    )
    WINDOWS_DEFAULT_PORTS: ClassVar[tuple[str, ...]] = (
        'COM1', 'COM2', 'COM3', 'COM4'
    )
    DARWIN_DEFAULT_PORTS: ClassVar[tuple[str, ...]] = (
        '/dev/tty.usbmodem1', '/dev/tty.usbserial1'
    )

    def scan_ports(self) -> list[str]:
        '''
            Discovers and returns available serial port identifiers with descriptions.

            :return: List of detected port description strings.
            :exceptions: None.
        '''
        detected: list[str] = []

        try:
            ports = comports()

            for port in ports:
                device = str(port.device) if port.device else ''
                description = str(port.description) if port.description else ''

                if device and description and description != 'n/a':
                    detected.append(f'{device} - {description}')
                elif device:
                    detected.append(device)

        except (OSError, TypeError, AttributeError):
            pass

        if not detected:
            return list(self.get_default_ports())

        return detected

    def get_default_ports(self) -> tuple[str, ...]:
        '''
            Returns fallback port identifiers for target OS platform.

            :return: Tuple of platform default serial port paths.
            :exceptions: None.
        '''
        if platform.startswith('win'):
            return self.WINDOWS_DEFAULT_PORTS

        if platform == 'darwin':
            return self.DARWIN_DEFAULT_PORTS

        return self.LINUX_DEFAULT_PORTS

    def get_version(self) -> str:
        '''
            Returns component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

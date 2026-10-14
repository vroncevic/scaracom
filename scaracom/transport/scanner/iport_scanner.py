# -*- coding: UTF-8 -*-

'''
Module
    iport_scanner.py
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
    Interface protocol for hardware serial port scanning and discovery.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IPortScanner(Protocol):
    '''
        Defines structural contract for serial port discovery and scanning.

        It defines:

            :methods:
                | scan_ports - Enumerates detected serial ports with descriptions.
                | get_version - Returns port scanner component version string.
    '''

    def scan_ports(self) -> list[str]:
        '''
            Enumerates detected serial ports with descriptions.

            :return: List of detected port description strings.
            :exceptions: None.
        '''

    def get_version(self) -> str:
        '''
            Returns port scanner component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''

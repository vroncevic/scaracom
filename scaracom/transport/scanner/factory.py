# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory component instantiating hardware serial port scanner.
'''

from __future__ import annotations

from scaracom.transport.scanner.iport_scanner import IPortScanner
from scaracom.transport.scanner.port_scanner import PortScanner

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class PortScannerFactory:
    '''
        Factory component constructing serial port scanner instances.

        It defines:

            :methods:
                | create - Constructs and returns IPortScanner instance.
                | get_version - Returns factory version string.
    '''

    @classmethod
    def create(cls) -> IPortScanner:
        '''
            Constructs and returns IPortScanner instance.

            :return: Fully configured IPortScanner implementation.
            :exceptions: None.
        '''
        return PortScanner()

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns factory version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

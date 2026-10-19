# -*- coding: UTF-8 -*-

'''
Module
    iport_scanner_test.py
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
    Unit tests for IPortScanner protocol.
'''

from __future__ import annotations

from unittest import TestCase

from scaracom.transport.scanner.iport_scanner import IPortScanner
from scaracom.transport.scanner.port_scanner import PortScanner

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class PortScannerProtocolTestCase(TestCase):
    '''
        Verifies IPortScanner protocol contract satisfaction.
    '''

    def test_port_scanner_implements_protocol(self) -> None:
        '''
            Verifies PortScanner satisfies IPortScanner structurally.
        '''
        scanner = PortScanner()
        self.assertTrue(isinstance(scanner, IPortScanner))

# -*- coding: UTF-8 -*-

'''
Module
    port_scanner_test.py
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
    Unit tests for PortScanner.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main
from unittest.mock import MagicMock, patch

from scaracom.transport.scanner.port_scanner import PortScanner

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class PortScannerTestCase(TestCase):
    '''
        Verifies PortScanner execution behaviors.

        It defines:

            :methods:
                | setUp - Sets up fresh port scanner instance.
                | test_scan_ports_detected - Verifies ports formatted when detected.
                | test_scan_ports_fallback_when_empty - Verifies fallback on empty or error.
                | test_get_default_ports_windows - Verifies Windows fallback ports.
                | test_get_default_ports_darwin - Verifies macOS fallback ports.
                | test_get_version - Verifies component version string.
    '''

    def setUp(self) -> None:
        '''
            Sets up fresh port scanner instance.
        '''
        self.scanner = PortScanner()

    @patch('scaracom.transport.scanner.port_scanner.comports')
    def test_scan_ports_detected(self, mock_comports: MagicMock) -> None:
        '''
            Verifies ports formatted with description when detected.
        '''
        p1 = MagicMock()
        p1.device = '/dev/ttyUSB0'
        p1.description = 'FTDI USB Serial'

        p2 = MagicMock()
        p2.device = '/dev/ttyACM0'
        p2.description = 'n/a'

        mock_comports.return_value = [p1, p2]
        ports = self.scanner.scan_ports()

        self.assertIn('/dev/ttyUSB0 - FTDI USB Serial', ports)
        self.assertIn('/dev/ttyACM0', ports)

    @patch('scaracom.transport.scanner.port_scanner.comports')
    def test_scan_ports_fallback_when_empty(self, mock_comports: MagicMock) -> None:
        '''
            Verifies fallback to default platform ports when no ports detected or on error.
        '''
        mock_comports.return_value = []
        ports = self.scanner.scan_ports()
        self.assertTrue(len(ports) > 0)

        mock_comports.side_effect = OSError('COM scanning error')
        fallback_ports = self.scanner.scan_ports()
        self.assertTrue(len(fallback_ports) > 0)

    @patch('scaracom.transport.scanner.port_scanner.platform', 'win32')
    def test_get_default_ports_windows(self) -> None:
        '''
            Verifies default fallback ports on Windows platform.
        '''
        ports = self.scanner.get_default_ports()
        self.assertEqual(ports, PortScanner.WINDOWS_DEFAULT_PORTS)

    @patch('scaracom.transport.scanner.port_scanner.platform', 'darwin')
    def test_get_default_ports_darwin(self) -> None:
        '''
            Verifies default fallback ports on macOS platform.
        '''
        ports = self.scanner.get_default_ports()
        self.assertEqual(ports, PortScanner.DARWIN_DEFAULT_PORTS)

    def test_get_version(self) -> None:
        '''
            Verifies component version string.
        '''
        self.assertEqual(self.scanner.get_version(), '1.0.0')


if __name__ == '__main__':
    main()

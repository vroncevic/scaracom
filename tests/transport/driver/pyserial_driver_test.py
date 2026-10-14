# -*- coding: UTF-8 -*-

'''
Module
    pyserial_driver_test.py
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
    Unit tests for PySerialDriver implementation.
'''

from __future__ import annotations

from unittest import TestCase
from unittest.mock import MagicMock, patch

from serial import SerialException

from scaracom.transport.driver.pyserial_driver import PySerialDriver

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class PySerialDriverTestCase(TestCase):
    '''
        Verifies PySerialDriver execution behaviors.
    '''

    def setUp(self) -> None:
        '''
            Sets up fresh driver for each test.
        '''
        self.driver = PySerialDriver()

    def test_initial_state_closed(self) -> None:
        '''
            Verifies driver is initially closed.
        '''
        self.assertFalse(self.driver.is_open())
        self.assertEqual(self.driver.read(10), b'')
        self.assertEqual(self.driver.write(b'hello'), 0)

    @patch('scaracom.transport.driver.pyserial_driver.Serial')
    def test_open_success(self, mock_serial_cls: MagicMock) -> None:
        '''
            Verifies successful port opening.
        '''
        mock_ser = MagicMock()
        mock_ser.is_open = True
        mock_serial_cls.return_value = mock_ser

        opened = self.driver.open('/dev/ttyUSB0', 115200, 0.1)
        self.assertTrue(opened)
        self.assertTrue(self.driver.is_open())
        mock_serial_cls.assert_called_once_with(port='/dev/ttyUSB0', baudrate=115200, timeout=0.1)

    @patch('scaracom.transport.driver.pyserial_driver.Serial')
    def test_open_failure_exception(self, mock_serial_cls: MagicMock) -> None:
        '''
            Verifies port open failure on SerialException.
        '''
        mock_serial_cls.side_effect = SerialException('Port busy')
        opened = self.driver.open('/dev/ttyUSB0', 115200, 0.1)
        self.assertFalse(opened)
        self.assertFalse(self.driver.is_open())

    @patch('scaracom.transport.driver.pyserial_driver.Serial')
    def test_read_and_write_success(self, mock_serial_cls: MagicMock) -> None:
        '''
            Verifies read and write operations on open port.
        '''
        mock_ser = MagicMock()
        mock_ser.is_open = True
        mock_ser.read.return_value = b'response\n'
        mock_ser.write.return_value = 5
        mock_serial_cls.return_value = mock_ser

        self.driver.open('/dev/ttyUSB0', 115200, 0.1)
        read_bytes = self.driver.read(10)
        written_count = self.driver.write(b'hello')

        self.assertEqual(read_bytes, b'response\n')
        self.assertEqual(written_count, 5)
        mock_ser.flush.assert_called_once()

    @patch('scaracom.transport.driver.pyserial_driver.Serial')
    def test_close_handles_cleanly(self, mock_serial_cls: MagicMock) -> None:
        '''
            Verifies close gracefully shuts down serial handle.
        '''
        mock_ser = MagicMock()
        mock_ser.is_open = True
        mock_serial_cls.return_value = mock_ser

        self.driver.open('/dev/ttyUSB0', 115200, 0.1)
        self.driver.close()
        self.assertFalse(self.driver.is_open())
        mock_ser.close.assert_called_once()

# -*- coding: UTF-8 -*-

'''
Module
    transport_test.py
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
    Unit tests for SerialTransport.
'''

from __future__ import annotations

from threading import Event, Thread
from time import sleep, time
from unittest import TestCase
from unittest.mock import MagicMock

from scaracom.transport.transport import SerialTransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SerialTransportTestCase(TestCase):
    '''
        Verifies SerialTransport execution behaviors.
    '''

    def setUp(self) -> None:
        '''
            Sets up transport with mocked driver.
        '''
        self.mock_driver = MagicMock()
        self.transport = SerialTransport(driver=self.mock_driver)

    def test_connect_delegates_to_driver(self) -> None:
        '''
            Verifies connect opens driver with port and baudrate.
        '''
        self.mock_driver.open.return_value = True
        result = self.transport.connect('/dev/ttyUSB0', 115200)

        self.assertTrue(result)
        self.mock_driver.open.assert_called_once_with(port='/dev/ttyUSB0', baudrate=115200, timeout=0.1)

    def test_disconnect_delegates_to_driver(self) -> None:
        '''
            Verifies disconnect closes driver.
        '''
        self.transport.disconnect()
        self.mock_driver.close.assert_called_once()

    def test_is_connected_delegates_to_driver(self) -> None:
        '''
            Verifies is_connected checks driver is_open.
        '''
        self.mock_driver.is_open.return_value = True
        self.assertTrue(self.transport.is_connected())

        self.mock_driver.is_open.return_value = False
        self.assertFalse(self.transport.is_connected())

    def test_read_bytes_delegates_to_driver(self) -> None:
        '''
            Verifies read_bytes reads from driver.
        '''
        self.mock_driver.read.return_value = b'test_payload'
        data = self.transport.read_bytes(12)

        self.assertEqual(data, b'test_payload')
        self.mock_driver.read.assert_called_once_with(12)

    def test_write_bytes_delegates_to_driver(self) -> None:
        '''
            Verifies write_bytes writes to driver.
        '''
        self.mock_driver.write.return_value = 4
        success = self.transport.write_bytes(b'data')

        self.assertTrue(success)
        self.mock_driver.write.assert_called_once_with(b'data')

        self.mock_driver.write.return_value = 0
        failure = self.transport.write_bytes(b'data')
        self.assertFalse(failure)

    def test_concurrent_read_write_non_blocking(self) -> None:
        '''
            Verifies write does not block when read is in progress.
        '''
        read_started = Event()
        self.mock_driver.write.return_value = 4

        def slow_read(_size: int) -> bytes:
            read_started.set()
            sleep(0.06)
            return b'done'

        self.mock_driver.read.side_effect = slow_read
        reader = Thread(target=lambda: self.transport.read_bytes(4))
        reader.start()

        read_started.wait(timeout=1.0)
        start_time = time()
        written = self.transport.write_bytes(b'ping')
        duration = time() - start_time

        self.assertTrue(written)
        self.assertLess(duration, 0.04)
        reader.join(timeout=1.0)

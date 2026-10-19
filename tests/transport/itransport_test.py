# -*- coding: UTF-8 -*-

'''
Module
    itransport_test.py
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
    Unit tests for ITransport protocol.
'''

from __future__ import annotations

from unittest import TestCase
from unittest.mock import MagicMock

from scaracom.transport.itransport import ITransport
from scaracom.transport.transport import SerialTransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportProtocolTestCase(TestCase):
    '''
        Verifies ITransport protocol contract satisfaction.
    '''

    def test_serial_transport_implements_protocol(self) -> None:
        '''
            Verifies SerialTransport satisfies ITransport structurally.
        '''
        mock_driver = MagicMock()
        transport = SerialTransport(driver=mock_driver)
        self.assertTrue(isinstance(transport, ITransport))

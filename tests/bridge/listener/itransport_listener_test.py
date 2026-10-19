# -*- coding: UTF-8 -*-

'''
Module
    itransport_listener_test.py
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
    Unit tests for ITransportListener protocol.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.bridge.listener.itransport_listener import ITransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ConformingTransportListener:
    '''
        Mock listener conforming to ITransportListener protocol.

        It defines:

            :methods:
                | on_bytes_received - Handles received byte data.
                | on_log_emitted - Handles emitted log entry.
                | get_version - Returns version string.
    '''

    def on_bytes_received(self, data: bytes) -> None:
        '''
            Handles received byte buffer.

            :param data: Received byte buffer.
            :exceptions: None.
        '''
        del data

    def on_log_emitted(self, message: str, is_tx: bool) -> None:
        '''
            Handles log event emission.

            :param message: Log text string.
            :param is_tx: Direction flag.
            :exceptions: None.
        '''
        del message, is_tx

    def get_version(self) -> str:
        '''
            Returns semantic version string.

            :return: Version string.
            :exceptions: None.
        '''
        return '1.0.2'


class TransportListenerProtocolTestCase(TestCase):
    '''
        Verifies ITransportListener runtime checkable protocol.

        It defines:

            :methods:
                | test_conforming_listener_implements_protocol - Verifies valid listener satisfies protocol.
                | test_non_listener_fails_protocol - Verifies non-conforming object fails check.
    '''

    def test_conforming_listener_implements_protocol(self) -> None:
        '''
            Verifies conforming object satisfies ITransportListener.

            :exceptions: None.
        '''
        listener = ConformingTransportListener()
        self.assertTrue(isinstance(listener, ITransportListener))

    def test_non_listener_fails_protocol(self) -> None:
        '''
            Verifies non-conforming object fails ITransportListener check.

            :exceptions: None.
        '''
        self.assertFalse(isinstance(object(), ITransportListener))


if __name__ == '__main__':
    main()

# -*- coding: UTF-8 -*-

'''
Module
    holder_test.py
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
    Unit tests for TransportListenerHolder.
'''

from __future__ import annotations

from unittest import TestCase

from scaracom.bridge.listener.holder import TransportListenerHolder

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MockListener:
    '''
        Mock listener recording dispatched events.
    '''

    def __init__(self) -> None:
        '''
            Initializes mock listener records.
        '''
        self.received_lines: list[str] = []
        self.received_bytes: list[bytes] = []
        self.emitted_logs: list[tuple[str, bool]] = []

    def on_line_received(self, line: str) -> None:
        '''
            Records inbound line.
        '''
        self.received_lines.append(line)

    def on_bytes_received(self, data: bytes) -> None:
        '''
            Records inbound bytes chunk.
        '''
        self.received_bytes.append(data)

    def on_log_emitted(self, message: str, is_tx: bool) -> None:
        '''
            Records emitted log.
        '''
        self.emitted_logs.append((message, is_tx))

    def get_version(self) -> str:
        '''
            Returns semantic version string.
        '''
        return '0.1.0'


class TransportListenerHolderTestCase(TestCase):
    '''
        Verifies TransportListenerHolder behaviors.
    '''

    def test_default_listener_discards_events(self) -> None:
        '''
            Verifies default initialization with NullTransportListener safely executes.
        '''
        holder = TransportListenerHolder()
        holder.on_line_received('LINE')
        holder.on_bytes_received(b'BYTES')
        holder.on_log_emitted('LOG', False)

    def test_delegates_to_injected_listener(self) -> None:
        '''
            Verifies holder delegates calls to injected listener.
        '''
        mock = MockListener()
        holder = TransportListenerHolder(mock)

        holder.on_line_received('STATUS:OK')
        holder.on_bytes_received(b'\x01\x02')
        holder.on_log_emitted('Log 1', True)

        self.assertEqual(mock.received_lines, ['STATUS:OK'])
        self.assertEqual(mock.received_bytes, [b'\x01\x02'])
        self.assertEqual(mock.emitted_logs, [('Log 1', True)])

    def test_set_listener_updates_target(self) -> None:
        '''
            Verifies changing listener swaps delegation target.
        '''
        mock1 = MockListener()
        mock2 = MockListener()
        holder = TransportListenerHolder(mock1)

        holder.on_line_received('FIRST')
        self.assertEqual(mock1.received_lines, ['FIRST'])

        holder.set_listener(mock2)
        holder.on_line_received('SECOND')

        self.assertEqual(mock1.received_lines, ['FIRST'])
        self.assertEqual(mock2.received_lines, ['SECOND'])

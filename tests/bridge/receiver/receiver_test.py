# -*- coding: UTF-8 -*-

'''
Module
    receiver_test.py
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
    Unit tests for TransportReceiver.
'''

from __future__ import annotations

from threading import Event
from unittest import TestCase
from unittest import main
from unittest.mock import Mock

from scaracom.bridge.receiver.dependencies import ReceiverDependencies
from scaracom.bridge.receiver.receiver import TransportReceiver

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportReceiverTestCase(TestCase):
    '''
        Verifies TransportReceiver behaviors.

        It defines:

            :methods:
                | test_is_running - Verifies is_running mirrors stop_event state.
                | test_run_terminates_if_not_connected - Verifies run exits when disconnected.
                | test_run_reads_bytes_and_dispatches_lines - Verifies run reads and forwards.
                | test_run_handles_listener_callback_exceptions - Verifies exception handling.
                | test_run_handles_abnormal_disconnect - Verifies disconnect handling.
                | test_get_version - Verifies component version string.
    '''

    def test_is_running(self) -> None:
        '''
            Verifies is_running mirrors stop_event state.

            :exceptions: None.
        '''
        stop_event = Event()
        deps = ReceiverDependencies(
            transport=Mock(),
            listener=Mock(),
            stop_event=stop_event,
        )
        receiver = TransportReceiver(deps)
        self.assertTrue(receiver.is_running())
        stop_event.set()
        self.assertFalse(receiver.is_running())

    def test_run_terminates_if_not_connected(self) -> None:
        '''
            Verifies run immediately exits when transport is not connected.

            :exceptions: None.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = False
        mock_listener = Mock()
        stop_event = Event()

        deps = ReceiverDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        receiver = TransportReceiver(deps)
        receiver.run()

        mock_transport.read_bytes.assert_not_called()

    def test_run_reads_bytes_and_dispatches_lines(self) -> None:
        '''
            Verifies run reads data and forwards bytes and assembled lines to listener.

            :exceptions: None.
        '''
        stop_event = Event()
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True

        calls: int = 0

        def read_side_effect(_size: int) -> bytes:
            nonlocal calls
            calls += 1
            if calls == 1:
                return b''
            stop_event.set()
            return b'CMD:STATUS_OK\n'

        mock_transport.read_bytes.side_effect = read_side_effect
        mock_listener = Mock()

        deps = ReceiverDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        receiver = TransportReceiver(deps)
        receiver.run()

        mock_listener.on_bytes_received.assert_called_with(b'CMD:STATUS_OK\n')
        mock_listener.on_line_received.assert_called_with('CMD:STATUS_OK')

    def test_run_handles_listener_callback_exceptions(self) -> None:
        '''
            Verifies run catches listener callback exceptions and logs errors.

            :exceptions: None.
        '''
        stop_event = Event()
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True

        def read_side_effect(_size: int) -> bytes:
            stop_event.set()
            return b'MALFORMED_LINE\n'

        mock_transport.read_bytes.side_effect = read_side_effect
        mock_listener = Mock()
        mock_listener.on_bytes_received.side_effect = RuntimeError('Byte error')
        mock_listener.on_line_received.side_effect = RuntimeError('Line error')

        deps = ReceiverDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        receiver = TransportReceiver(deps)
        receiver.run()

        self.assertEqual(mock_listener.on_log_emitted.call_count, 2)

    def test_run_handles_abnormal_disconnect(self) -> None:
        '''
            Verifies run disconnects transport on read failure when stop_event not set.

            :exceptions: None.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        mock_transport.read_bytes.side_effect = IOError('Hardware failure')
        mock_listener = Mock()
        stop_event = Event()

        deps = ReceiverDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        receiver = TransportReceiver(deps)
        receiver.run()

        mock_transport.disconnect.assert_called_once()
        mock_listener.on_log_emitted.assert_called_with(
            '[HOST]: Connection lost (device disconnected / unplugged)', False
        )

    def test_get_version(self) -> None:
        '''
            Verifies version returns valid semantic string.

            :exceptions: None.
        '''
        deps = ReceiverDependencies(
            transport=Mock(),
            listener=Mock(),
            stop_event=Event(),
        )
        receiver = TransportReceiver(deps)
        self.assertEqual(receiver.get_version(), '1.0.0')


if __name__ == '__main__':
    main()

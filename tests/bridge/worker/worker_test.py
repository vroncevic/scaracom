# -*- coding: UTF-8 -*-

'''
Module
    worker_test.py
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
    Unit tests for TransportReaderWorker.
'''

from __future__ import annotations

from threading import Event
from unittest import TestCase
from unittest.mock import Mock

from scaracom.bridge.worker.dependencies import WorkerDependencies
from scaracom.bridge.worker.worker import TransportReaderWorker

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportReaderWorkerTestCase(TestCase):
    '''
        Verifies TransportReaderWorker behaviors.
    '''

    def test_is_running(self) -> None:
        '''
            Verifies is_running mirrors stop_event state.
        '''
        stop_event = Event()
        deps = WorkerDependencies(
            transport=Mock(),
            listener=Mock(),
            stop_event=stop_event,
        )
        worker = TransportReaderWorker(deps)
        self.assertTrue(worker.is_running())
        stop_event.set()
        self.assertFalse(worker.is_running())

    def test_run_terminates_if_not_connected(self) -> None:
        '''
            Verifies run immediately exits when transport is not connected.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = False
        mock_listener = Mock()
        stop_event = Event()

        deps = WorkerDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        worker = TransportReaderWorker(deps)
        worker.run()

        mock_transport.read_bytes.assert_not_called()

    def test_run_reads_bytes_and_dispatches_lines(self) -> None:
        '''
            Verifies run reads data and forwards bytes and assembled lines to listener.
        '''
        stop_event = Event()
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True

        def read_side_effect(_size: int) -> bytes:
            stop_event.set()
            return b'CMD:STATUS_OK\n'

        mock_transport.read_bytes.side_effect = read_side_effect
        mock_listener = Mock()

        deps = WorkerDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        worker = TransportReaderWorker(deps)
        worker.run()

        mock_listener.on_bytes_received.assert_called_with(b'CMD:STATUS_OK\n')
        mock_listener.on_line_received.assert_called_with('CMD:STATUS_OK')

    def test_run_handles_listener_callback_exceptions(self) -> None:
        '''
            Verifies run catches listener callback exceptions and logs errors.
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

        deps = WorkerDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        worker = TransportReaderWorker(deps)
        worker.run()

        self.assertEqual(mock_listener.on_log_emitted.call_count, 2)

    def test_run_handles_abnormal_disconnect(self) -> None:
        '''
            Verifies run disconnects transport on read failure when stop_event not set.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        mock_transport.read_bytes.side_effect = IOError('Hardware failure')
        mock_listener = Mock()
        stop_event = Event()

        deps = WorkerDependencies(
            transport=mock_transport,
            listener=mock_listener,
            stop_event=stop_event,
        )
        worker = TransportReaderWorker(deps)
        worker.run()

        mock_transport.disconnect.assert_called_once()
        mock_listener.on_log_emitted.assert_called_with(
            '[HOST]: Connection lost (device disconnected / unplugged)', False
        )

    def test_get_version(self) -> None:
        '''
            Verifies version returns valid semantic string.
        '''
        deps = WorkerDependencies(
            transport=Mock(),
            listener=Mock(),
            stop_event=Event(),
        )
        worker = TransportReaderWorker(deps)
        self.assertEqual(worker.get_version(), '0.1.0')

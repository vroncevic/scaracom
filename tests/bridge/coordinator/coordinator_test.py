# -*- coding: UTF-8 -*-

'''
Module
    coordinator_test.py
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
    Unit tests for ConnectionCoordinator.
'''

from __future__ import annotations

from threading import Event, Thread
from unittest import TestCase
from unittest.mock import Mock

from scaracom.bridge.coordinator.coordinator import ConnectionCoordinator
from scaracom.bridge.coordinator.dependencies import CoordinatorDependencies
from scaracom.bridge.listener.itransport_listener import ITransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ConnectionCoordinatorTestCase(TestCase):
    '''
        Verifies ConnectionCoordinator behaviors.
    '''

    def test_is_connected(self) -> None:
        '''
            Verifies is_connected delegates to transport.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        deps = CoordinatorDependencies(
            transport=mock_transport,
            listener_holder=Mock(),
            receiver=Mock(),
            stop_event=Event(),
        )
        coordinator = ConnectionCoordinator(deps)
        self.assertTrue(coordinator.is_connected())

        mock_transport.is_connected.return_value = False
        self.assertFalse(coordinator.is_connected())

    def test_set_listener(self) -> None:
        '''
            Verifies set_listener forwards to listener_holder.
        '''
        mock_holder = Mock()
        deps = CoordinatorDependencies(
            transport=Mock(),
            listener_holder=mock_holder,
            receiver=Mock(),
            stop_event=Event(),
        )
        coordinator = ConnectionCoordinator(deps)
        listener = Mock(spec=ITransportListener)
        coordinator.set_listener(listener)
        mock_holder.set_listener.assert_called_with(listener)

    def test_connect_failure(self) -> None:
        '''
            Verifies connect logs error and returns False on connection failure.
        '''
        mock_transport = Mock()
        mock_transport.connect.return_value = False
        mock_holder = Mock()

        deps = CoordinatorDependencies(
            transport=mock_transport,
            listener_holder=mock_holder,
            receiver=Mock(),
            stop_event=Event(),
        )
        coordinator = ConnectionCoordinator(deps)
        result = coordinator.connect('/dev/ttyUSB0', 115200)

        self.assertFalse(result)
        mock_holder.on_log_emitted.assert_called_with(
            '[ERR]: Failed to connect to /dev/ttyUSB0', False
        )

    def test_connect_and_disconnect_success(self) -> None:
        '''
            Verifies connect starts thread and disconnect stops it cleanly.
        '''
        mock_transport = Mock()
        mock_transport.connect.return_value = True
        mock_transport.is_connected.return_value = False
        mock_holder = Mock()
        stop_event = Event()
        mock_receiver = Mock()
        mock_receiver.run.side_effect = lambda: stop_event.wait(0.5)

        deps = CoordinatorDependencies(
            transport=mock_transport,
            listener_holder=mock_holder,
            receiver=mock_receiver,
            stop_event=stop_event,
        )
        coordinator = ConnectionCoordinator(deps)
        result = coordinator.connect('/dev/ttyUSB0', 115200)

        self.assertTrue(result)
        coordinator.disconnect()
        mock_transport.disconnect.assert_called()

    def test_disconnect_handles_exception(self) -> None:
        '''
            Verifies disconnect catches and logs transport disconnect error.
        '''
        mock_transport = Mock()
        mock_transport.disconnect.side_effect = IOError('Close error')
        mock_holder = Mock()

        deps = CoordinatorDependencies(
            transport=mock_transport,
            listener_holder=mock_holder,
            receiver=Mock(),
            stop_event=Event(),
        )
        coordinator = ConnectionCoordinator(deps)
        coordinator.disconnect()

        mock_holder.on_log_emitted.assert_any_call(
            '[ERR]: Error disconnecting transport: Close error', False
        )

    def test_concurrent_connect_disconnect_thread_safe(self) -> None:
        '''
            Verifies concurrent connect and disconnect calls do not raise race errors.
        '''
        mock_transport = Mock()
        mock_transport.connect.return_value = True
        mock_transport.is_connected.return_value = False
        deps = CoordinatorDependencies(
            transport=mock_transport,
            listener_holder=Mock(),
            receiver=Mock(),
            stop_event=Event(),
        )
        coordinator = ConnectionCoordinator(deps)
        threads: list[Thread] = []

        for idx in range(4):
            if idx % 2 == 0:
                t = Thread(target=coordinator.connect, args=('/dev/ttyUSB0', 115200))
            else:
                t = Thread(target=coordinator.disconnect)
            threads.append(t)
            t.start()

        for t in threads:
            t.join(timeout=1.0)

        coordinator.disconnect()
        self.assertFalse(coordinator.is_connected())

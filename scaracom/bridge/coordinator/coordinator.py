# -*- coding: UTF-8 -*-

'''
Module
    coordinator.py
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
    Dedicated connection coordinator managing transport lifecycle and reader thread.
'''

from __future__ import annotations

from threading import Event, RLock, Thread
from typing import Final

from scaracom.bridge.coordinator.dependencies import CoordinatorDependencies
from scaracom.bridge.listener.iholder import ITransportListenerHolder
from scaracom.bridge.listener.itransport_listener import ITransportListener
from scaracom.bridge.receiver.ireceiver import ITransportReceiver
from scaracom.transport.itransport import ITransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ConnectionCoordinator:
    '''
        Connection lifecycle coordinator managing channel driver state and background reader thread.

        It defines:

            :attributes:
                | _transport - Injected ITransport communication transport layer.
                | _listener_holder - Injected ITransportListenerHolder event sink container.
                | _receiver - Injected ITransportReceiver background packet runner.
                | _stop_event - Injected Event signaling reader loop termination.
                | _reader_thread - Thread handle running background packet reading loop.
                | _lock - Reentrant thread lock for lifecycle state transitions.
            :methods:
                | __init__ - Initializes connection coordinator with dependencies.
                | is_connected - Checks if communication link is active.
                | set_listener - Updates the transport event listener.
                | connect - Opens channel and starts reader thread.
                | disconnect - Terminates reader thread and closes channel.
    '''

    _transport: ITransport
    _listener_holder: ITransportListenerHolder
    _receiver: ITransportReceiver
    _stop_event: Event
    _reader_thread: Thread
    _lock: RLock

    def __init__(self, dependencies: CoordinatorDependencies) -> None:
        '''
            Initializes connection coordinator with dependency bundle.

            :param dependencies: Injected CoordinatorDependencies parameter bundle.
            :exceptions: None.
        '''
        self._transport: Final[ITransport] = dependencies.transport
        self._listener_holder: Final[ITransportListenerHolder] = dependencies.listener_holder
        self._receiver: Final[ITransportReceiver] = dependencies.receiver
        self._stop_event: Final[Event] = dependencies.stop_event
        self._reader_thread: Thread = Thread(target=bool)
        self._lock: Final[RLock] = RLock()

    def is_connected(self) -> bool:
        '''
            Checks if communication link is active.

            :return: True if connected, False otherwise.
        '''
        with self._lock:
            return self._transport.is_connected()

    def set_listener(self, listener: ITransportListener) -> None:
        '''
            Updates the transport event listener.

            :param listener: ITransportListener instance.
        '''
        self._listener_holder.set_listener(listener)

    def connect(self, port: str, baudrate: int) -> bool:
        '''
            Opens transport connection and starts reader thread.

            :param port: Serial port identifier path.
            :param baudrate: Transmission baud rate.
            :return: True if connected successfully, False otherwise.
        '''
        with self._lock:
            self.disconnect()

            if self._transport.connect(port, baudrate):
                self._stop_event.clear()
                self._reader_thread = Thread(target=self._receiver.run, daemon=True)
                self._reader_thread.start()
                self._listener_holder.on_log_emitted(
                    f'[HOST]: Connected to {port}', False
                )

                return True

            self._listener_holder.on_log_emitted(
                f'[ERR]: Failed to connect to {port}', False
            )

            return False

    def disconnect(self) -> None:
        '''
            Terminates reader thread and closes transport connection.
        '''
        with self._lock:
            self._stop_event.set()

            try:
                self._transport.disconnect()

            except Exception as exc:
                self._listener_holder.on_log_emitted(
                    f'[ERR]: Error disconnecting transport: {exc}', False
                )

            if self._reader_thread.is_alive():
                self._reader_thread.join(timeout=0.2)

            self._listener_holder.on_log_emitted(
                '[HOST]: Disconnected from transport', False
            )

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

from threading import Event, Thread
from typing import Final, Type

from scaracom.bridge.coordinator.dependencies import CoordinatorDependencies
from scaracom.bridge.listener.iholder import ITransportListenerHolder
from scaracom.bridge.listener.itransport_listener import ITransportListener
from scaracom.bridge.worker.dependencies import WorkerDependencies
from scaracom.bridge.worker.factory import ReaderWorkerFactory
from scaracom.transport.itransport import ITransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
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
                | _worker_factory - Injected ReaderWorkerFactory worker creator class.
                | _stop_event - Event signaling reader thread termination.
                | _reader_thread - Thread handle running background packet reading loop.
            :methods:
                | __init__ - Initializes connection coordinator with dependencies.
                | is_connected - Checks if communication link is active.
                | set_listener - Updates the transport event listener.
                | connect - Opens channel and starts reader thread.
                | disconnect - Terminates reader thread and closes channel.
    '''

    _transport: ITransport
    _listener_holder: ITransportListenerHolder
    _worker_factory: Type[ReaderWorkerFactory]
    _stop_event: Event
    _reader_thread: Thread

    def __init__(self, dependencies: CoordinatorDependencies) -> None:
        '''
            Initializes connection coordinator with dependency bundle.

            :param dependencies: Injected CoordinatorDependencies parameter bundle.
            :exceptions: None.
        '''
        self._transport: Final[ITransport] = dependencies.transport
        self._listener_holder: Final[ITransportListenerHolder] = dependencies.listener_holder
        self._worker_factory: Final[Type[ReaderWorkerFactory]] = dependencies.worker_factory
        self._stop_event: Final[Event] = Event()
        self._reader_thread: Thread = Thread(target=bool)

    def is_connected(self) -> bool:
        '''
            Checks if communication link is active.

            :return: True if connected, False otherwise.
        '''
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
        self.disconnect()

        if self._transport.connect(port, baudrate):
            self._stop_event.clear()
            worker = self._worker_factory.create(
                WorkerDependencies(
                    transport=self._transport,
                    listener=self._listener_holder,
                    stop_event=self._stop_event,
                )
            )
            self._reader_thread = Thread(target=worker.run, daemon=True)
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

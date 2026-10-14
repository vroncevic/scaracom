# -*- coding: UTF-8 -*-

'''
Module
    worker.py
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
    Dedicated background reader loop worker for hardware communication transports.
'''

from __future__ import annotations

from threading import Event
from time import sleep
from typing import Final

from scaracom.bridge.listener.itransport_listener import ITransportListener
from scaracom.bridge.worker.dependencies import WorkerDependencies
from scaracom.transport.itransport import ITransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportReaderWorker:
    '''
        Dedicated background worker handling byte streaming and newline packet assembly.

        It defines:

            :attributes:
                | _transport - Low-level communication transport layer.
                | _listener - Inbound transport event listener.
                | _stop_event - Event signaling reader loop termination.
            :methods:
                | __init__ - Initializes reader worker with dependency bundle.
                | is_running - Checks if reader loop termination event is not set.
                | run - Executes background read loop until stopped or disconnect detected.
                | get_version - Returns worker component version string.
    '''

    _transport: ITransport
    _listener: ITransportListener
    _stop_event: Event

    def __init__(self, dependencies: WorkerDependencies) -> None:
        '''
            Initializes reader worker with dependencies bundle.

            :param dependencies: Injected WorkerDependencies parameter bundle.
            :exceptions: None.
        '''
        self._transport: Final[ITransport] = dependencies.transport
        self._listener: Final[ITransportListener] = dependencies.listener
        self._stop_event: Final[Event] = dependencies.stop_event

    def is_running(self) -> bool:
        '''
            Checks if reader loop termination event is not set.

            :return: True if running, False otherwise.
        '''
        return not self._stop_event.is_set()

    def run(self) -> None:
        '''
            Executes background polling loop assembling incoming lines and forwarding byte chunks.

            :exceptions: None.
        '''
        buffer: str = ''
        abnormal_disconnect: bool = False

        while not self._stop_event.is_set():
            if not self._transport.is_connected():
                break

            try:
                data: bytes = self._transport.read_bytes(64)
                if not data:
                    sleep(0.01)
                    continue

                try:
                    self._listener.on_bytes_received(data)
                except Exception as b_exc:
                    self._listener.on_log_emitted(
                        f'[ERR]: Byte callback error: {b_exc}', False
                    )

                buffer += data.decode('utf-8', errors='ignore')

                while '\n' in buffer:
                    line: str
                    line, buffer = buffer.split('\n', 1)
                    line = line.strip()

                    if line:
                        try:
                            self._listener.on_line_received(line)
                        except Exception as cb_exc:
                            self._listener.on_log_emitted(
                                f'[ERR]: Line callback error: {cb_exc}', False
                            )
            except Exception:
                if not self._stop_event.is_set():
                    abnormal_disconnect = True
                break

        if abnormal_disconnect:
            self._transport.disconnect()
            self._listener.on_log_emitted(
                '[HOST]: Connection lost (device disconnected / unplugged)', False
            )

    def get_version(self) -> str:
        '''
            Returns worker component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

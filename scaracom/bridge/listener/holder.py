# -*- coding: UTF-8 -*-

'''
Module
    holder.py
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
    Thread-safe listener wrapper allowing dynamic updating of transport event sinks.
'''

from __future__ import annotations

from threading import Lock
from typing import Final

from scaracom.bridge.listener.itransport_listener import ITransportListener
from scaracom.bridge.listener.null_listener import NullTransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportListenerHolder:
    '''
        Mutable holder delegating transport callbacks to the active listener.

        It defines:

            :attributes:
                | _listener - Active ITransportListener instance.
                | _lock - Re-entrant thread safety lock for listener swapping.
            :methods:
                | __init__ - Initializes holder with default null listener.
                | set_listener - Updates active listener target.
                | on_line_received - Dispatches text line event to active listener.
                | on_bytes_received - Dispatches raw bytes event to active listener.
                | on_log_emitted - Dispatches log event to active listener.
    '''

    _listener: ITransportListener
    _lock: Lock

    def __init__(self, listener: ITransportListener | None = None) -> None:
        '''
            Initializes holder with initial listener or null listener fallback.

            :param listener: Optional initial ITransportListener instance.
            :exceptions: None.
        '''
        self._listener = listener if listener is not None else NullTransportListener()
        self._lock: Final[Lock] = Lock()

    def set_listener(self, listener: ITransportListener) -> None:
        '''
            Updates active listener target.

            :param listener: New ITransportListener instance.
            :exceptions: None.
        '''
        with self._lock:
            self._listener = listener

    def on_line_received(self, line: str) -> None:
        '''
            Dispatches text line event to active listener.

            :param line: Received text line.
            :exceptions: None.
        '''
        with self._lock:
            active_listener: ITransportListener = self._listener
        active_listener.on_line_received(line)

    def on_bytes_received(self, data: bytes) -> None:
        '''
            Dispatches raw bytes event to active listener.

            :param data: Received byte buffer.
            :exceptions: None.
        '''
        with self._lock:
            active_listener: ITransportListener = self._listener
        active_listener.on_bytes_received(data)

    def on_log_emitted(self, message: str, is_tx: bool) -> None:
        '''
            Dispatches log event to active listener.

            :param message: Formatted log message text.
            :param is_tx: True if emitted after transmission, False otherwise.
            :exceptions: None.
        '''
        with self._lock:
            active_listener: ITransportListener = self._listener
        active_listener.on_log_emitted(message, is_tx)

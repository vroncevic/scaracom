# -*- coding: UTF-8 -*-

'''
Module
    router.py
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
    Routes parsed binary wire frames to registered handler protocol instances.
'''

from __future__ import annotations

from threading import Lock

from scaracom.flow.router.iframe import IRoutedFrame
from scaracom.flow.router.ihandler import IFrameHandler

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FrameRouter:
    '''
        Routes parsed binary wire frames to registered handler protocol instances.

        It defines:

            :attributes:
                | _handlers - Internal mapping of message IDs to list of handler instances.
                | _lock - Synchronization lock protecting handler registry mutations.
            :methods:
                | __init__ - Initializes empty handler registry and synchronization lock.
                | register_handler - Registers protocol handler for specific message ID.
                | unregister_handler - Unregisters protocol handler for specific message ID.
                | route - Routes binary frame payload to registered handlers.
                | get_version - Returns router component version string.
    '''

    _handlers: dict[int, list[IFrameHandler]]
    _lock: Lock

    def __init__(self) -> None:
        '''
            Initializes empty handler registry and synchronization lock.

            :exceptions: None.
        '''
        self._handlers = {}
        self._lock = Lock()

    def register_handler(self, message_id: int, handler: IFrameHandler) -> None:
        '''
            Registers protocol handler for specific message ID.

            :param message_id: Numerical message opcode identifier.
            :param handler: Injected IFrameHandler handler instance.
            :exceptions: None.
        '''
        with self._lock:
            key: int = int(message_id)

            if key not in self._handlers:
                self._handlers[key] = []

            if handler not in self._handlers[key]:
                self._handlers[key].append(handler)

    def unregister_handler(self, message_id: int, handler: IFrameHandler) -> None:
        '''
            Unregisters protocol handler for specific message ID.

            :param message_id: Numerical message opcode identifier.
            :param handler: Injected IFrameHandler handler instance to remove.
            :exceptions: None.
        '''
        with self._lock:
            key: int = int(message_id)

            if key in self._handlers and handler in self._handlers[key]:
                self._handlers[key].remove(handler)

    def route(self, frame: IRoutedFrame) -> bool:
        '''
            Routes binary frame payload to registered handlers.

            :param frame: Parsed IRoutedFrame object.
            :return: True if frame was routed to one or more handlers, False otherwise.
            :exceptions: None.
        '''
        if not hasattr(frame, 'msg_id'):
            return False

        key: int = int(frame.msg_id)

        with self._lock:
            if key not in self._handlers:
                return False

            targets: list[IFrameHandler] = list(self._handlers[key])

        for handler in targets:
            try:
                handler.handle_frame(frame)

            except Exception:
                pass

        return len(targets) > 0

    def get_version(self) -> str:
        '''
            Returns router component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

# -*- coding: UTF-8 -*-

'''
Module
    queue.py
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
    Thread-safe outbound frame queue implementation for communication buffering.
'''

from __future__ import annotations

from queue import Empty, Queue

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FrameQueue:
    '''
        Thread-safe FIFO queue buffering outbound wire protocol frames.

        It defines:

            :attributes:
                | _queue - Internal thread-safe FIFO queue container.
            :methods:
                | __init__ - Initializes empty frame buffer.
                | put_frame - Enqueues outbound frame data into buffer.
                | get_frame - Dequeues frame data with timeout.
                | clear - Empties all queued frames from buffer.
                | size - Returns number of pending queued frames.
                | get_version - Returns queue component version string.
    '''

    _queue: Queue[bytes]

    def __init__(self, *, maxsize: int = 0) -> None:
        '''
            Initializes empty frame buffer.

            :param maxsize: Maximum buffer capacity, defaults to 0 (unbounded).
            :exceptions: None.
        '''
        self._queue = Queue(maxsize=maxsize)

    def put_frame(self, data: bytes) -> bool:
        '''
            Enqueues outbound frame bytes into buffer.

            :param data: Raw frame bytes to buffer.
            :return: True if enqueued successfully, False otherwise.
            :exceptions: None.
        '''
        try:
            self._queue.put_nowait(data)
            return True

        except Exception:
            return False

    def get_frame(self, timeout_sec: float) -> tuple[bool, bytes]:
        '''
            Dequeues next available frame bytes, blocking until timeout expires.

            :param timeout_sec: Maximum wait duration in seconds.
            :return: Tuple of (True, data) if dequeued, or (False, b'') if timed out.
            :exceptions: None.
        '''
        try:
            item: bytes = self._queue.get(timeout=timeout_sec)
            return True, item

        except Empty:
            return False, b''

    def clear(self) -> None:
        '''
            Clears all queued frames from buffer.

            :exceptions: None.
        '''
        while not self._queue.empty():
            try:
                self._queue.get_nowait()

            except Empty:
                break

    def size(self) -> int:
        '''
            Returns current number of pending items in queue.

            :return: Integer count of pending items.
            :exceptions: None.
        '''
        return self._queue.qsize()

    def get_version(self) -> str:
        '''
            Returns queue component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

# -*- coding: UTF-8 -*-

'''
Module
    iqueue.py
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
    Structural protocol defining outbound communication frame queue operations.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IFrameQueue(Protocol):
    '''
        Structural protocol defining outbound frame queue buffering operations.

        It defines:

            :methods:
                | put_frame - Enqueues outbound frame data into buffer.
                | get_frame - Dequeues frame data with timeout.
                | clear - Empties all queued frames from buffer.
                | size - Returns number of pending queued frames.
                | get_version - Returns queue protocol version string.
    '''

    def put_frame(self, data: bytes) -> bool:
        '''
            Enqueues outbound frame bytes into buffer.

            :param data: Raw frame bytes to buffer.
            :return: True if enqueued successfully, False otherwise.
            :exceptions: None.
        '''

    def get_frame(self, timeout_sec: float) -> tuple[bool, bytes]:
        '''
            Dequeues next available frame bytes, blocking until timeout expires.

            :param timeout_sec: Maximum wait duration in seconds.
            :return: Tuple of (True, data) if dequeued, or (False, b'') if timed out.
            :exceptions: None.
        '''

    def clear(self) -> None:
        '''
            Clears all queued frames from buffer.

            :exceptions: None.
        '''

    def size(self) -> int:
        '''
            Returns current number of pending items in queue.

            :return: Integer count of pending items.
            :exceptions: None.
        '''

    def get_version(self) -> str:
        '''
            Returns queue protocol version string.

            :return: Semantic version string.
            :exceptions: None.
        '''

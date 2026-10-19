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
    Thread-safe cyclic frame sequence counter coordinator.
'''

from __future__ import annotations

from threading import Lock

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SequenceCoordinator:
    '''
        Coordinates thread-safe cyclic 8-bit frame sequence numbering.

        It defines:

            :attributes:
                | _seq - Internal sequence counter integer.
                | _lock - Synchronization lock protecting counter mutations.
            :methods:
                | __init__ - Initializes sequence counter to zero.
                | next_sequence_id - Advances and returns next cyclic sequence counter.
                | current_sequence_id - Returns current sequence counter value.
                | reset - Resets sequence counter back to zero baseline.
                | get_version - Returns sequence coordinator component version string.
    '''

    _seq: int
    _lock: Lock

    def __init__(self, *, initial_seq: int = 0) -> None:
        '''
            Initializes sequence coordinator with initial counter value.

            :param initial_seq: Initial sequence integer, defaults to 0.
            :exceptions: None.
        '''
        self._seq = initial_seq & 0xFF
        self._lock = Lock()

    def next_sequence_id(self) -> int:
        '''
            Advances cyclic sequence counter modulo 256 and returns value.

            :return: Incremented 8-bit integer sequence ID (0 - 255).
            :exceptions: None.
        '''
        with self._lock:
            val: int = self._seq
            self._seq = (self._seq + 1) & 0xFF

            return val

    def current_sequence_id(self) -> int:
        '''
            Returns current sequence counter without advancing.

            :return: Current 8-bit integer sequence ID (0 - 255).
            :exceptions: None.
        '''
        with self._lock:
            return self._seq

    def reset(self) -> None:
        '''
            Resets sequence counter to zero.

            :exceptions: None.
        '''
        with self._lock:
            self._seq = 0

    def get_version(self) -> str:
        '''
            Returns sequence coordinator component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

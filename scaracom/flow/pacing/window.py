# -*- coding: UTF-8 -*-

'''
Module
    window.py
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
    Flow control window state tracking unacknowledged and buffered packets.
'''

from __future__ import annotations

from threading import Lock
from typing import Final

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FlowWindow:
    '''
        Flow control window tracking unacknowledged and buffered packets.

        It defines:

            :attributes:
                | DEFAULT_MAX_IN_FLIGHT - Default max concurrent packets in flight.
                | _max_in_flight - Maximum concurrent packets allowed in flight.
                | _firmware_queue_depth - Number of commands buffered in firmware.
                | _unacked_sent_count - Count of unacknowledged packets in flight.
                | _lock - Thread synchronization lock for atomic slot state updates.
            :methods:
                | __init__ - Initializes flow control window with capacity limit.
                | acquire_slot - Attempts to acquire packet transmission slot.
                | update_from_slots - Updates window state from available queue slots.
                | reset - Resets window metrics to empty baseline.
                | get_version - Returns flow window component version string.
    '''

    DEFAULT_MAX_IN_FLIGHT: Final[int] = 16

    _max_in_flight: int
    _firmware_queue_depth: int
    _unacked_sent_count: int
    _lock: Lock

    def __init__(self, max_in_flight: int = DEFAULT_MAX_IN_FLIGHT) -> None:
        '''
            Initializes flow control window with capacity limit.

            :param max_in_flight: Maximum in-flight packets allowed.
            :exceptions: None.
        '''
        self._max_in_flight: Final[int] = max_in_flight
        self._firmware_queue_depth = 0
        self._unacked_sent_count = 0
        self._lock = Lock()

    def acquire_slot(self) -> bool:
        '''
            Attempts to acquire packet transmission slot.

            :return: True if slot acquired, False if window full.
            :exceptions: None.
        '''
        with self._lock:
            if (self._firmware_queue_depth + self._unacked_sent_count) < self._max_in_flight:
                self._unacked_sent_count += 1
                return True

            return False

    def update_from_slots(self, free_slots: int) -> None:
        '''
            Updates window state from available queue slots in firmware acknowledgment.

            :param free_slots: Count of free buffer slots reported by firmware.
            :exceptions: None.
        '''
        with self._lock:
            if self._unacked_sent_count > 0:
                self._unacked_sent_count -= 1

            self._firmware_queue_depth = max(0, self._max_in_flight - max(0, free_slots))

    def reset(self) -> None:
        '''
            Resets window metrics to empty baseline.

            :exceptions: None.
        '''
        with self._lock:
            self._firmware_queue_depth = 0
            self._unacked_sent_count = 0

    def get_version(self) -> str:
        '''
            Returns flow window component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

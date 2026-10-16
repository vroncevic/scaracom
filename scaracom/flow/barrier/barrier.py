# -*- coding: UTF-8 -*-

'''
Module
    barrier.py
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
    Thread synchronization barrier managing command execution gating.
'''

from __future__ import annotations

from threading import Event

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FlowBarrier:
    '''
        Manages thread synchronization barrier events for synchronous command gating.

        It defines:

            :attributes:
                | _barrier_event - Thread synchronization barrier event.
            :methods:
                | __init__ - Initializes synchronization barrier in cleared state.
                | set_barrier - Locks barrier event until confirmation is received.
                | clear_barrier - Unlocks barrier event.
                | is_barrier_clear - Checks whether synchronization barrier is unlocked.
                | wait_clear - Blocks until barrier is unlocked or timeout expires.
                | get_version - Returns barrier component version string.
    '''

    _barrier_event: Event

    def __init__(self) -> None:
        '''
            Initializes synchronization barrier in cleared state.

            :exceptions: None.
        '''
        self._barrier_event = Event()
        self._barrier_event.set()

    def set_barrier(self) -> None:
        '''
            Locks barrier event until confirmation is received.

            :exceptions: None.
        '''
        self._barrier_event.clear()

    def clear_barrier(self) -> None:
        '''
            Unlocks barrier event.

            :exceptions: None.
        '''
        self._barrier_event.set()

    def is_barrier_clear(self) -> bool:
        '''
            Checks whether synchronization barrier is unlocked.

            :return: True if barrier is unlocked, False otherwise.
            :exceptions: None.
        '''
        return self._barrier_event.is_set()

    def wait_clear(self, timeout_sec: float) -> bool:
        '''
            Blocks until barrier is clear or timeout period elapses.

            :param timeout_sec: Timeout period in seconds to wait.
            :return: True if barrier became clear before timeout, False if timed out.
            :exceptions: None.
        '''
        return self._barrier_event.wait(timeout_sec)

    def get_version(self) -> str:
        '''
            Returns barrier component version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

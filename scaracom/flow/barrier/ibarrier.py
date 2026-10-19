# -*- coding: UTF-8 -*-

'''
Module
    ibarrier.py
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
    Structural protocol IFlowBarrier for stream execution synchronization barriers.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IFlowBarrier(Protocol):
    '''
        Structural protocol defining stream execution synchronization barrier operations.

        It defines:

            :methods:
                | set_barrier - Locks synchronization barrier for synchronous execution.
                | clear_barrier - Unlocks synchronization barrier.
                | is_barrier_clear - Checks whether synchronization barrier is unlocked.
                | wait_clear - Blocks until barrier is unlocked or timeout expires.
                | get_version - Returns barrier protocol version string.
    '''

    def set_barrier(self) -> None:
        '''
            Locks synchronization barrier.

            :exceptions: None.
        '''

    def clear_barrier(self) -> None:
        '''
            Unlocks synchronization barrier.

            :exceptions: None.
        '''

    def is_barrier_clear(self) -> bool:
        '''
            Checks if synchronization barrier is cleared.

            :return: True if barrier is clear, False otherwise.
            :exceptions: None.
        '''

    def wait_clear(self, timeout_sec: float) -> bool:
        '''
            Blocks until barrier is clear or timeout period elapses.

            :param timeout_sec: Timeout period in seconds to wait.
            :return: True if barrier became clear before timeout, False if timed out.
            :exceptions: None.
        '''

    def get_version(self) -> str:
        '''
            Returns barrier protocol version string.

            :return: Semantic version string.
            :exceptions: None.
        '''

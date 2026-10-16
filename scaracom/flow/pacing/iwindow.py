# -*- coding: UTF-8 -*-

'''
Module
    iwindow.py
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
    Structural protocol for hardware flow control window state tracking.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IFlowWindow(Protocol):
    '''
        Structural protocol defining flow control window state tracking.

        It defines:

            :methods:
                | acquire_slot - Attempts to acquire packet transmission slot.
                | update_from_slots - Updates window state from available queue slots.
                | reset - Resets window metrics to empty baseline.
                | get_version - Returns flow window protocol version.
    '''

    def acquire_slot(self) -> bool:
        '''
            Attempts to acquire packet transmission slot.

            :return: True if slot acquired, False if window full.
        '''

    def update_from_slots(self, free_slots: int) -> None:
        '''
            Updates window state from available queue slots in firmware acknowledgment.

            :param free_slots: Count of free buffer slots reported by firmware.
        '''

    def reset(self) -> None:
        '''
            Resets window metrics to empty baseline.
        '''

    def get_version(self) -> str:
        '''
            Returns flow window protocol version.

            :return: Semantic version string.
        '''

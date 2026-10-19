# -*- coding: UTF-8 -*-

'''
Module
    icoordinator.py
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
    Structural protocol defining frame sequence counter operations.
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
class ISequenceCoordinator(Protocol):
    '''
        Structural protocol defining frame sequence number generation and tracking.

        It defines:

            :methods:
                | next_sequence_id - Advances and returns next cyclic sequence counter.
                | current_sequence_id - Returns current sequence counter value.
                | reset - Resets sequence counter back to zero baseline.
                | get_version - Returns sequence coordinator protocol version string.
    '''

    def next_sequence_id(self) -> int:
        '''
            Advances cyclic sequence counter modulo 256 and returns value.

            :return: Incremented 8-bit integer sequence ID (0 - 255).
            :exceptions: None.
        '''

    def current_sequence_id(self) -> int:
        '''
            Returns current sequence counter without advancing.

            :return: Current 8-bit integer sequence ID (0 - 255).
            :exceptions: None.
        '''

    def reset(self) -> None:
        '''
            Resets sequence counter to zero.

            :exceptions: None.
        '''

    def get_version(self) -> str:
        '''
            Returns sequence coordinator protocol version string.

            :return: Semantic version string.
            :exceptions: None.
        '''

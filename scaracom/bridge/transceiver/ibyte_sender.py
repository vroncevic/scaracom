# -*- coding: UTF-8 -*-

'''
Module
    ibyte_sender.py
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
    Structural protocol defining raw byte stream transmission operations.
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
class IByteSender(Protocol):
    '''
        Structural protocol defining raw byte stream transmission operations.

        It defines:

            :methods:
                | send_raw_bytes - Transmits raw byte sequence over active transport.
                | get_version - Returns protocol version string.
    '''

    def send_raw_bytes(self, payload: bytes) -> bool:
        '''
            Transmits raw byte sequence over active communication transport.

            :param payload: Raw byte sequence to transmit.
            :return: True if transmission succeeded, False otherwise.
        '''

    def get_version(self) -> str:
        '''
            Returns protocol version string.

            :return: Semantic version string.
        '''

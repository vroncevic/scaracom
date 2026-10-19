# -*- coding: UTF-8 -*-

'''
Module
    ichannel.py
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
    Interface protocol for bi-directional raw byte communication channels.
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
class IRawChannel(Protocol):
    '''
        Structural protocol defining raw byte stream communication operations.

        It defines:

            :methods:
                | is_connected - Checks whether transport connection is currently open.
                | send_raw_bytes - Transmits raw byte payload over active communication transport.
                | get_version - Returns protocol version string.
    '''

    def is_connected(self) -> bool:
        '''
            Checks whether transport connection is currently open.

            :return: True if transport is connected, False otherwise.
        '''

    def send_raw_bytes(self, payload: bytes) -> bool:
        '''
            Transmits raw byte payload over active communication transport.

            :param payload: Raw byte payload to transmit.
            :return: True if transmission succeeded, False otherwise.
        '''

    def get_version(self) -> str:
        '''
            Returns protocol version string.

            :return: Semantic version string.
        '''

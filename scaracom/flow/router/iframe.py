# -*- coding: UTF-8 -*-

'''
Module
    iframe.py
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
    Interface protocol defining routable wire frame contract.
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
class IRoutedFrame(Protocol):
    '''
        Protocol defining structural contract for routable binary wire frames.

        It defines:

            :attributes:
                | msg_id - Message type opcode or identifier.
                | seq_num - Cyclic sequence counter.
                | payload - Binary payload bytes.
                | crc16 - Frame CRC checksum.
    '''

    @property
    def msg_id(self) -> int:
        '''
            Message type opcode or identifier.

            :return: Message identifier opcode.
        '''

    @property
    def seq_num(self) -> int:
        '''
            Cyclic sequence counter.

            :return: Sequence counter value.
        '''

    @property
    def payload(self) -> bytes:
        '''
            Binary payload bytes.

            :return: Frame payload byte sequence.
        '''

    @property
    def crc16(self) -> int:
        '''
            Frame CRC checksum.

            :return: 16-bit CRC checksum value.
        '''

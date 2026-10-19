# -*- coding: UTF-8 -*-

'''
Module
    itransport.py
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
    Defines abstract communication transport interface.
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
class ITransport(Protocol):
    '''
        Interface for communication transport layers.

        It defines:

            :methods:
                | is_connected - Returns connection state.
                | connect - Establishes communication connection.
                | disconnect - Closes active connection.
                | read_bytes - Reads raw byte packet from communication stream.
                | write_bytes - Transmits raw byte packet.
    '''

    def is_connected(self) -> bool:
        '''
            Returns connection state.

            :return: True if connected, False otherwise.
            :exceptions: None.
        '''

    def connect(self, port: str, baudrate: int) -> bool:
        '''
            Establishes communication connection.

            :param port: Device address or port identifier.
            :param baudrate: Transmission baud rate.
            :return: True if connected successfully, False otherwise.
            :exceptions: None.
        '''

    def disconnect(self) -> None:
        '''
            Closes active connection.

            :exceptions: None.
        '''

    def read_bytes(self, size: int) -> bytes:
        '''
            Reads raw byte packet from communication stream.

            :param size: Number of bytes to read.
            :return: Read byte payload.
            :exceptions: None.
        '''

    def write_bytes(self, data: bytes) -> bool:
        '''
            Transmits raw byte packet.

            :param data: Binary payload to send.
            :return: True if transmitted, False otherwise.
            :exceptions: None.
        '''

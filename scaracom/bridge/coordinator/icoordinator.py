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
    Interface protocol defining connection coordinator lifecycle and listener binding.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from scaracom.bridge.listener.itransport_listener import ITransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IConnectionCoordinator(Protocol):
    '''
        Structural interface protocol for connection lifecycle and background reader orchestration.

        It defines:

            :methods:
                | is_connected - Checks if communication link is active.
                | set_listener - Updates the transport event listener.
                | connect - Opens channel and starts reader thread.
                | disconnect - Terminates reader thread and closes channel.
    '''

    def is_connected(self) -> bool:
        '''
            Checks if communication link is active.

            :return: True if connected, False otherwise.
        '''

    def set_listener(self, listener: ITransportListener) -> None:
        '''
            Updates the transport event listener.

            :param listener: ITransportListener instance.
        '''

    def connect(self, port: str, baudrate: int) -> bool:
        '''
            Opens transport connection and starts background reader thread.

            :param port: Serial port identifier path.
            :param baudrate: Transmission baud rate.
            :return: True if connected successfully, False otherwise.
        '''

    def disconnect(self) -> None:
        '''
            Terminates reader thread and closes transport connection.
        '''

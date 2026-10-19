# -*- coding: UTF-8 -*-

'''
Module
    irouter.py
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
    Interface protocol defining binary wire frame routing operations.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from scaracom.flow.router.iframe import IRoutedFrame
from scaracom.flow.router.ihandler import IFrameHandler

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IFrameRouter(Protocol):
    '''
        Protocol defining registration and routing of parsed binary frames.

        It defines:

            :methods:
                | register_handler - Registers protocol handler for specific message ID.
                | unregister_handler - Unregisters protocol handler for specific message ID.
                | route - Routes binary frame payload to registered handlers.
                | get_version - Returns router protocol version string.
    '''

    def register_handler(self, message_id: int, handler: IFrameHandler) -> None:
        '''
            Registers protocol handler for specific message ID.

            :param message_id: Numerical message opcode identifier.
            :param handler: Injected IFrameHandler handler instance.
        '''

    def unregister_handler(self, message_id: int, handler: IFrameHandler) -> None:
        '''
            Unregisters protocol handler for specific message ID.

            :param message_id: Numerical message opcode identifier.
            :param handler: Injected IFrameHandler handler instance to remove.
        '''

    def route(self, frame: IRoutedFrame) -> bool:
        '''
            Routes binary frame payload to registered handlers.

            :param frame: Parsed IRoutedFrame object.
            :return: True if frame was routed, False otherwise.
        '''

    def get_version(self) -> str:
        '''
            Returns router protocol version string.

            :return: Semantic version string.
        '''

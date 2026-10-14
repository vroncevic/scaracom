# -*- coding: UTF-8 -*-

'''
Module
    null_listener.py
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
    Null-object implementation of transport event listener discarding events silently.
'''

from __future__ import annotations

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class NullTransportListener:
    '''
        Null-object transport event listener discarding events silently.

        It defines:

            :methods:
                | on_line_received - Discards text response line.
                | on_bytes_received - Discards raw byte chunk.
                | on_log_emitted - Discards generated transport log.
                | get_version - Returns component version string.
    '''

    def on_line_received(self, line: str) -> None:
        '''
            Discards received text response line.

            :param line: Inbound line payload string.
        '''
        del line

    def on_bytes_received(self, data: bytes) -> None:
        '''
            Discards received raw byte chunk.

            :param data: Inbound bytes payload.
        '''
        del data

    def on_log_emitted(self, message: str, is_tx: bool) -> None:
        '''
            Discards generated transport log entry.

            :param message: Log message string.
            :param is_tx: Transmission flag.
        '''
        del message, is_tx

    def get_version(self) -> str:
        '''
            Returns component version string.

            :return: Semantic version string.
        '''
        return __version__

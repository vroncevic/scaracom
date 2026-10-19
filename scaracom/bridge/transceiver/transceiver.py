# -*- coding: UTF-8 -*-

'''
Module
    transceiver.py
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
    Transceiver managing raw byte payload transmission over transport.
'''

from __future__ import annotations

from typing import Final

from scaracom.bridge.listener.itransport_listener import ITransportListener
from scaracom.bridge.transceiver.dependencies import TransceiverDependencies
from scaracom.transport.itransport import ITransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class RawTransceiver:
    '''
        Transceiver managing raw byte payload transmission.

        It defines:

            :attributes:
                | _transport - Injected ITransport communication transport instance.
                | _listener - Injected ITransportListener event sink instance.
            :methods:
                | __init__ - Initializes RawTransceiver with dependency bundle.
                | is_connected - Checks whether transport connection is currently open.
                | send_raw_bytes - Transmits raw byte payload over active transport.
                | get_version - Returns transceiver component version.
    '''

    _transport: ITransport
    _listener: ITransportListener

    def __init__(self, dependencies: TransceiverDependencies) -> None:
        '''
            Initializes RawTransceiver with dependencies bundle.

            :param dependencies: Injected TransceiverDependencies parameter bundle.
            :exceptions: None.
        '''
        self._transport: Final[ITransport] = dependencies.transport
        self._listener: Final[ITransportListener] = dependencies.listener

    def is_connected(self) -> bool:
        '''
            Checks whether transport connection is currently open.

            :return: True if transport is connected, False otherwise.
            :exceptions: None.
        '''
        return self._transport.is_connected()

    def send_raw_bytes(self, payload: bytes) -> bool:
        '''
            Transmits raw byte payload over active transport.

            :param payload: Raw byte payload.
            :return: True if transmission succeeded, False otherwise.
            :exceptions: None.
        '''
        if not self._transport.is_connected():
            return False

        self._listener.on_log_emitted(f'[TX]: (HEX) {payload.hex()}', True)
        try:
            return self._transport.write_bytes(payload)
        except Exception as exc:
            self._listener.on_log_emitted(
                f'[ERR]: Binary send error: {exc}', False
            )
            return False

    def get_version(self) -> str:
        '''
            Returns transceiver component version.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

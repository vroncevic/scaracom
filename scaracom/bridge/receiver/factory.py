# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory instantiating transport receiver components.
'''

from __future__ import annotations

from typing import Type

from scaracom.bridge.receiver.dependencies import ReceiverDependencies
from scaracom.bridge.receiver.ireceiver import ITransportReceiver
from scaracom.bridge.receiver.receiver import TransportReceiver

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReceiverFactory:
    '''
        Factory providing creation of transport receiver components.

        It defines:

            :methods:
                | create - Instantiates and returns an ITransportReceiver.
                | get_version - Returns factory component version.
    '''

    @classmethod
    def create(
        cls: Type[ReceiverFactory],
        dependencies: ReceiverDependencies,
    ) -> ITransportReceiver:
        '''
            Instantiates and returns an ITransportReceiver.

            :param dependencies: Injected ReceiverDependencies parameter bundle.
            :return: Configured ITransportReceiver instance.
            :exceptions: None.
        '''
        return TransportReceiver(dependencies)

    @classmethod
    def get_version(cls: Type[ReceiverFactory]) -> str:
        '''
            Returns factory component version.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

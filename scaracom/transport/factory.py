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
    Factory component constructing communication transport instances.
'''

from __future__ import annotations

from scaracom.transport.driver.factory import SerialDriverFactory
from scaracom.transport.driver.idriver import ISerialDriver
from scaracom.transport.itransport import ITransport
from scaracom.transport.transport import SerialTransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportFactory:
    '''
        Factory component constructing physical communication transport instances.

        It defines:

            :methods:
                | create - Constructs and returns ITransport instance.
                | get_version - Returns factory version string.
    '''

    @classmethod
    def create(cls) -> ITransport:
        '''
            Constructs and returns ITransport instance with default serial driver.

            :return: Fully wired ITransport implementation.
            :exceptions: None.
        '''
        driver: ISerialDriver = SerialDriverFactory.create()

        return SerialTransport(driver=driver)

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns factory version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return __version__

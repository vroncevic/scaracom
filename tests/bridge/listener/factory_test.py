# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Unit tests for ListenerHolderFactory.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main
from unittest.mock import Mock

from scaracom.bridge.listener.factory import ListenerHolderFactory
from scaracom.bridge.listener.iholder import ITransportListenerHolder
from scaracom.bridge.listener.itransport_listener import ITransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ListenerHolderFactoryTestCase(TestCase):
    '''
        Verifies ListenerHolderFactory behaviors.

        It defines:

            :methods:
                | test_create_returns_holder - Verifies factory creates holder with injected listener.
                | test_get_version - Verifies factory version returns valid string.
    '''

    def test_create_returns_holder(self) -> None:
        '''
            Verifies factory creates ITransportListenerHolder with injected listener.

            :exceptions: None.
        '''
        listener = Mock(spec=ITransportListener)
        holder = ListenerHolderFactory.create(listener)
        self.assertTrue(isinstance(holder, ITransportListenerHolder))

    def test_get_version(self) -> None:
        '''
            Verifies factory version returns valid string.

            :exceptions: None.
        '''
        self.assertEqual(ListenerHolderFactory.get_version(), '1.0.0')


if __name__ == '__main__':
    main()

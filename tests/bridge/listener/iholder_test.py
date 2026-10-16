# -*- coding: UTF-8 -*-

'''
Module
    iholder_test.py
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
    Unit tests for ITransportListenerHolder protocol.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main
from unittest.mock import Mock

from scaracom.bridge.listener.holder import TransportListenerHolder
from scaracom.bridge.listener.iholder import ITransportListenerHolder
from scaracom.bridge.listener.itransport_listener import ITransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportListenerHolderProtocolTestCase(TestCase):
    '''
        Verifies ITransportListenerHolder runtime checkable protocol.
    '''

    def test_holder_implements_protocol(self) -> None:
        '''
            Verifies TransportListenerHolder satisfies ITransportListenerHolder.

            :exceptions: None.
        '''
        holder = TransportListenerHolder(Mock(spec=ITransportListener))
        self.assertTrue(isinstance(holder, ITransportListenerHolder))

    def test_non_holder_fails_protocol(self) -> None:
        '''
            Verifies non-conforming object fails ITransportListenerHolder check.

            :exceptions: None.
        '''
        self.assertFalse(isinstance(object(), ITransportListenerHolder))


if __name__ == '__main__':
    main()

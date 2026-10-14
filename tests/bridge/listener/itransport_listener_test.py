# -*- coding: UTF-8 -*-

'''
Module
    itransport_listener_test.py
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
    Unit tests for ITransportListener protocol.
'''

from __future__ import annotations

from unittest import TestCase

from scaracom.bridge.listener.itransport_listener import ITransportListener
from scaracom.bridge.listener.null_listener import NullTransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportListenerProtocolTestCase(TestCase):
    '''
        Verifies ITransportListener runtime checkable protocol.
    '''

    def test_null_listener_implements_protocol(self) -> None:
        '''
            Verifies NullTransportListener satisfies ITransportListener.
        '''
        listener = NullTransportListener()
        self.assertTrue(isinstance(listener, ITransportListener))

    def test_non_listener_fails_protocol(self) -> None:
        '''
            Verifies non-conforming object fails ITransportListener check.
        '''
        self.assertFalse(isinstance(object(), ITransportListener))

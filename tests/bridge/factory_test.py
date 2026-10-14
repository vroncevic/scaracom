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
    Unit tests for BridgeFactory.
'''

from __future__ import annotations

from unittest import TestCase
from unittest.mock import Mock

from scaracom.bridge.coordinator.icoordinator import IConnectionCoordinator
from scaracom.bridge.dependencies import BridgeDependencies
from scaracom.bridge.factory import BridgeFactory
from scaracom.bridge.listener.iholder import ITransportListenerHolder
from scaracom.bridge.provides import BridgeProvides
from scaracom.bridge.transceiver.ichannel import IRawChannel
from scaracom.transport.itransport import ITransport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BridgeFactoryTestCase(TestCase):
    '''
        Verifies BridgeFactory behaviors.
    '''

    def test_create_returns_bridge_provides(self) -> None:
        '''
            Verifies factory creates configured BridgeProvides container.
        '''
        mock_transport = Mock(spec=ITransport)
        deps = BridgeDependencies(transport=mock_transport)
        provides = BridgeFactory.create(deps)

        self.assertTrue(isinstance(provides, BridgeProvides))
        self.assertTrue(isinstance(provides.coordinator, IConnectionCoordinator))
        self.assertTrue(isinstance(provides.transceiver, IRawChannel))
        self.assertTrue(isinstance(provides.listener_holder, ITransportListenerHolder))
        self.assertEqual(provides.transport, mock_transport)

    def test_get_version(self) -> None:
        '''
            Verifies factory version returns valid string.
        '''
        self.assertEqual(BridgeFactory.get_version(), '0.1.0')

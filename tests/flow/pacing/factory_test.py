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
    Unit tests for WindowFactory flow control window subsystem creation.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.pacing.dependencies import WindowDependencies
from scaracom.flow.pacing.factory import WindowFactory
from scaracom.flow.pacing.iwindow import IFlowWindow
from scaracom.flow.pacing.provides import WindowProvides
from scaracom.flow.pacing.window import FlowWindow

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestWindowFactory(TestCase):
    '''
        Unit test cases verifying WindowFactory creation and structural typing.

        It defines:

            :methods:
                | test_create - Verifies WindowProvides creation with default config.
                | test_structural_typing - Verifies created window satisfies IFlowWindow.
                | test_get_version - Verifies factory version string.
    '''

    def test_create(self) -> None:
        '''
            Verifies creation with valid dependency configuration.

            :exceptions: None.
        '''
        dependencies = WindowDependencies(max_in_flight=8)
        provides: WindowProvides = WindowFactory.create(dependencies)
        self.assertIsInstance(provides, WindowProvides)
        self.assertIsInstance(provides.window, FlowWindow)

    def test_structural_typing(self) -> None:
        '''
            Verifies created window satisfies IFlowWindow protocol.

            :exceptions: None.
        '''
        provides = WindowFactory.create(WindowDependencies())
        self.assertTrue(isinstance(provides.window, IFlowWindow))

    def test_get_version(self) -> None:
        '''
            Verifies factory version returns valid semantic string.

            :exceptions: None.
        '''
        self.assertEqual(WindowFactory.get_version(), '1.0.0')


if __name__ == '__main__':
    main()

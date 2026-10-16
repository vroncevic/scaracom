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
    Unit tests for RouterFactory component.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.router.factory import RouterFactory
from scaracom.flow.router.irouter import IFrameRouter
from scaracom.flow.router.provides import RouterProvides
from scaracom.flow.router.router import FrameRouter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestRouterFactory(TestCase):
    '''
        Test suite verifying RouterFactory component instantiation and wiring.

        It defines:

            :methods:
                | test_create - Verifies RouterProvides creation.
                | test_structural_typing - Verifies router satisfies IFrameRouter.
                | test_get_version - Verifies factory semantic version string.
    '''

    def test_create(self) -> None:
        '''
            Verifies factory creates a valid RouterProvides instance.
        '''
        provides: RouterProvides = RouterFactory.create()
        self.assertIsInstance(provides, RouterProvides)
        self.assertIsInstance(provides.router, FrameRouter)

    def test_structural_typing(self) -> None:
        '''
            Verifies created router satisfies IFrameRouter protocol.
        '''
        provides: RouterProvides = RouterFactory.create()
        self.assertTrue(isinstance(provides.router, IFrameRouter))

    def test_get_version(self) -> None:
        '''
            Verifies factory returns a valid semantic version string.
        '''
        version: str = RouterFactory.get_version()
        self.assertIsInstance(version, str)
        self.assertEqual(version, '1.0.1')


if __name__ == '__main__':
    main()

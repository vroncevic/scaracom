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
    Unit tests for SequenceFactory component.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.sequence.coordinator import SequenceCoordinator
from scaracom.flow.sequence.factory import SequenceFactory
from scaracom.flow.sequence.icoordinator import ISequenceCoordinator
from scaracom.flow.sequence.provides import SequenceProvides

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSequenceFactory(TestCase):
    '''
        Test suite verifying SequenceFactory component instantiation and wiring.

        It defines:

            :methods:
                | test_create - Verifies SequenceProvides creation.
                | test_structural_typing - Verifies coordinator satisfies ISequenceCoordinator.
                | test_get_version - Verifies factory semantic version string.
    '''

    def test_create(self) -> None:
        '''
            Verifies factory creates a valid SequenceProvides instance.
        '''
        provides: SequenceProvides = SequenceFactory.create()
        self.assertIsInstance(provides, SequenceProvides)
        self.assertIsInstance(provides.coordinator, SequenceCoordinator)

    def test_structural_typing(self) -> None:
        '''
            Verifies created coordinator satisfies ISequenceCoordinator protocol.
        '''
        provides: SequenceProvides = SequenceFactory.create()
        self.assertTrue(isinstance(provides.coordinator, ISequenceCoordinator))

    def test_get_version(self) -> None:
        '''
            Verifies factory returns a valid semantic version string.
        '''
        version: str = SequenceFactory.get_version()
        self.assertIsInstance(version, str)
        self.assertEqual(version, '1.0.1')


if __name__ == '__main__':
    main()

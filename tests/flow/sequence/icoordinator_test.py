# -*- coding: UTF-8 -*-

'''
Module
    icoordinator_test.py
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
    Unit tests for ISequenceCoordinator protocol.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.sequence.coordinator import SequenceCoordinator
from scaracom.flow.sequence.icoordinator import ISequenceCoordinator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestISequenceCoordinator(TestCase):
    '''
        Verifies ISequenceCoordinator runtime checkable protocol contract.

        It defines:

            :methods:
                | test_structural_typing - Verifies SequenceCoordinator satisfies protocol.
                | test_non_conforming - Verifies non-conforming object fails check.
    '''

    def test_structural_typing(self) -> None:
        '''
            Verifies SequenceCoordinator satisfies ISequenceCoordinator structurally.
        '''
        coordinator = SequenceCoordinator()
        self.assertTrue(isinstance(coordinator, ISequenceCoordinator))

    def test_non_conforming(self) -> None:
        '''
            Verifies non-conforming object fails ISequenceCoordinator check.
        '''
        self.assertFalse(isinstance(object(), ISequenceCoordinator))


if __name__ == '__main__':
    main()

# -*- coding: UTF-8 -*-

'''
Module
    coordinator_test.py
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
    Unit tests for SequenceCoordinator component.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.sequence.coordinator import SequenceCoordinator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSequenceCoordinator(TestCase):
    '''
        Unit test cases verifying SequenceCoordinator cyclic arithmetic and reset.

        It defines:

            :methods:
                | setUp - Initializes SequenceCoordinator test instance.
                | test_initial_state - Verifies initial sequence counter value.
                | test_advance_and_wraparound - Verifies 8-bit cyclic incrementing.
                | test_reset - Verifies sequence reset back to zero.
                | test_custom_initial_value - Verifies custom initial sequence parameter.
                | test_get_version - Verifies version string retrieval.
    '''

    _coordinator: SequenceCoordinator

    def setUp(self) -> None:
        '''
            Sets up test fixture with SequenceCoordinator instance.
        '''
        self._coordinator = SequenceCoordinator()

    def test_initial_state(self) -> None:
        '''
            Verifies initial sequence is zero.
        '''
        self.assertEqual(self._coordinator.current_sequence_id(), 0)

    def test_advance_and_wraparound(self) -> None:
        '''
            Verifies sequential advance and modulo 256 wraparound.
        '''
        coord = SequenceCoordinator(initial_seq=254)
        self.assertEqual(coord.next_sequence_id(), 254)
        self.assertEqual(coord.next_sequence_id(), 255)
        self.assertEqual(coord.next_sequence_id(), 0)
        self.assertEqual(coord.current_sequence_id(), 1)

    def test_reset(self) -> None:
        '''
            Verifies reset sets sequence counter back to zero.
        '''
        self._coordinator.next_sequence_id()
        self._coordinator.next_sequence_id()
        self.assertGreater(self._coordinator.current_sequence_id(), 0)
        self._coordinator.reset()
        self.assertEqual(self._coordinator.current_sequence_id(), 0)

    def test_custom_initial_value(self) -> None:
        '''
            Verifies custom initial sequence value masking.
        '''
        coord = SequenceCoordinator(initial_seq=42)
        self.assertEqual(coord.current_sequence_id(), 42)

    def test_get_version(self) -> None:
        '''
            Verifies get_version returns valid semantic version string.
        '''
        version: str = self._coordinator.get_version()
        self.assertIsInstance(version, str)
        self.assertEqual(version, '1.0.1')


if __name__ == '__main__':
    main()

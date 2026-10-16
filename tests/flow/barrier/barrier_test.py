# -*- coding: UTF-8 -*-

'''
Module
    barrier_test.py
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
    Unit tests for FlowBarrier component.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.barrier.barrier import FlowBarrier

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestFlowBarrier(TestCase):
    '''
        Unit test cases verifying FlowBarrier synchronization states.

        It defines:

            :methods:
                | setUp - Initializes FlowBarrier test instance.
                | test_initial_state - Verifies barrier initializes in cleared state.
                | test_set_barrier - Verifies locking barrier sets state to uncleared.
                | test_clear_barrier - Verifies clearing barrier unlocks state.
                | test_wait_clear_success - Verifies wait_clear returns True when clear.
                | test_wait_clear_timeout - Verifies wait_clear returns False on timeout.
                | test_get_version - Verifies version string retrieval.
    '''

    _barrier: FlowBarrier

    def setUp(self) -> None:
        '''
            Sets up test fixture with FlowBarrier instance.
        '''
        self._barrier = FlowBarrier()

    def test_initial_state(self) -> None:
        '''
            Verifies barrier initializes in unlocked (clear) state.
        '''
        self.assertTrue(self._barrier.is_barrier_clear())

    def test_set_barrier(self) -> None:
        '''
            Verifies set_barrier locks the barrier.
        '''
        self._barrier.set_barrier()
        self.assertFalse(self._barrier.is_barrier_clear())

    def test_clear_barrier(self) -> None:
        '''
            Verifies clear_barrier transitions barrier back to unlocked state.
        '''
        self._barrier.set_barrier()
        self.assertFalse(self._barrier.is_barrier_clear())
        self._barrier.clear_barrier()
        self.assertTrue(self._barrier.is_barrier_clear())

    def test_wait_clear_success(self) -> None:
        '''
            Verifies wait_clear succeeds when barrier is clear.
        '''
        self.assertTrue(self._barrier.wait_clear(timeout_sec=0.1))

    def test_wait_clear_timeout(self) -> None:
        '''
            Verifies wait_clear returns False when barrier remains locked.
        '''
        self._barrier.set_barrier()
        self.assertFalse(self._barrier.wait_clear(timeout_sec=0.02))

    def test_get_version(self) -> None:
        '''
            Verifies get_version returns valid semantic version string.
        '''
        version: str = self._barrier.get_version()
        self.assertIsInstance(version, str)
        self.assertEqual(version, '1.0.0')


if __name__ == '__main__':
    main()

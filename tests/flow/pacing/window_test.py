# -*- coding: UTF-8 -*-

'''
Module
    window_test.py
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
    Unit tests for FlowWindow sliding-window flow control in scaracom.flow.pacing.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.pacing.iwindow import IFlowWindow
from scaracom.flow.pacing.window import FlowWindow

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestFlowWindow(TestCase):
    '''
        Unit test cases verifying FlowWindow capacity limiting and replenishment.

        It defines:

            :methods:
                | setUp - Initializes FlowWindow with test capacity.
                | test_acquire_slot_limit - Verifies slot acquisition up to capacity limit.
                | test_update_from_slots - Verifies slot replenishment on ACK feedback.
                | test_reset - Verifies resetting window baseline state.
                | test_structural_typing - Verifies instance satisfies IFlowWindow.
                | test_get_version - Verifies version string retrieval.
    '''

    _window: FlowWindow

    def setUp(self) -> None:
        '''
            Sets up test fixture with capacity 3.

            :exceptions: None.
        '''
        self._window = FlowWindow(max_in_flight=3)

    def test_acquire_slot_limit(self) -> None:
        '''
            Verifies slots can be acquired up to max capacity.

            :exceptions: None.
        '''
        self.assertTrue(self._window.acquire_slot())
        self.assertTrue(self._window.acquire_slot())
        self.assertTrue(self._window.acquire_slot())
        self.assertFalse(self._window.acquire_slot())

    def test_update_from_slots(self) -> None:
        '''
            Verifies unacknowledged count decrements on ACK feedback.

            :exceptions: None.
        '''
        self.assertTrue(self._window.acquire_slot())
        self.assertTrue(self._window.acquire_slot())
        self._window.update_from_slots(free_slots=3)
        self.assertTrue(self._window.acquire_slot())

    def test_reset(self) -> None:
        '''
            Verifies reset restores slot acquisition ability.

            :exceptions: None.
        '''
        self._window.acquire_slot()
        self._window.acquire_slot()
        self._window.acquire_slot()
        self.assertFalse(self._window.acquire_slot())
        self._window.reset()
        self.assertTrue(self._window.acquire_slot())

    def test_structural_typing(self) -> None:
        '''
            Verifies FlowWindow satisfies IFlowWindow protocol structurally.

            :exceptions: None.
        '''
        self.assertTrue(isinstance(self._window, IFlowWindow))

    def test_get_version(self) -> None:
        '''
            Verifies version string returned.

            :exceptions: None.
        '''
        self.assertEqual(self._window.get_version(), '1.0.0')


if __name__ == '__main__':
    main()

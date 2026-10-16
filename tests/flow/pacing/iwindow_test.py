# -*- coding: UTF-8 -*-

'''
Module
    iwindow_test.py
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
    Unit tests for IFlowWindow structural protocol.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.pacing.iwindow import IFlowWindow

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DummyWindow:
    '''
        Structural stub implementing IFlowWindow contract.

        It defines:

            :methods:
                | acquire_slot - Attempts to acquire packet transmission slot.
                | update_from_slots - Updates window state from available queue slots.
                | reset - Resets window metrics to empty baseline.
                | get_version - Returns flow window protocol version.
    '''

    def acquire_slot(self) -> bool:
        '''
            Attempts to acquire packet transmission slot.

            :return: Always True for test stub.
            :exceptions: None.
        '''
        return True

    def update_from_slots(self, free_slots: int) -> None:
        '''
            Updates window state from available queue slots.

            :param free_slots: Count of free buffer slots.
            :exceptions: None.
        '''
        _ = free_slots

    def reset(self) -> None:
        '''
            Resets window metrics to empty baseline.

            :exceptions: None.
        '''

    def get_version(self) -> str:
        '''
            Returns flow window protocol version.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return '1.0.0'


class IncompleteWindow:
    '''
        Incomplete class missing required protocol methods.

        It defines:

            :methods:
                | acquire_slot - Attempts to acquire packet transmission slot.
                | extra_action - Secondary action not matching protocol.
    '''

    def acquire_slot(self) -> bool:
        '''
            Attempts to acquire packet transmission slot.

            :return: Always True for test stub.
            :exceptions: None.
        '''
        return True

    def extra_action(self) -> bool:
        '''
            Secondary action not matching protocol.

            :return: Always True for test stub.
            :exceptions: None.
        '''
        return True


class TestIFlowWindow(TestCase):
    '''
        Unit test cases verifying IFlowWindow runtime typing.

        It defines:

            :methods:
                | test_structural_typing - Verifies dummy satisfies protocol.
                | test_incomplete_class - Verifies incomplete class fails protocol check.
    '''

    def test_structural_typing(self) -> None:
        '''
            Verifies DummyWindow satisfies IFlowWindow protocol.

            :exceptions: None.
        '''
        window = DummyWindow()
        self.assertIsInstance(window, IFlowWindow)

    def test_incomplete_class(self) -> None:
        '''
            Verifies incomplete class does not satisfy IFlowWindow.

            :exceptions: None.
        '''
        incomplete = IncompleteWindow()
        self.assertNotIsInstance(incomplete, IFlowWindow)


if __name__ == '__main__':
    main()

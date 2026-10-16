# -*- coding: UTF-8 -*-

'''
Module
    ibarrier_test.py
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
    Unit tests for IFlowBarrier protocol.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.barrier.barrier import FlowBarrier
from scaracom.flow.barrier.ibarrier import IFlowBarrier

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestIFlowBarrier(TestCase):
    '''
        Verifies IFlowBarrier runtime checkable protocol contract.

        It defines:

            :methods:
                | test_structural_typing - Verifies FlowBarrier satisfies protocol.
                | test_non_conforming - Verifies non-conforming object fails check.
    '''

    def test_structural_typing(self) -> None:
        '''
            Verifies FlowBarrier satisfies IFlowBarrier structurally.
        '''
        barrier = FlowBarrier()
        self.assertTrue(isinstance(barrier, IFlowBarrier))

    def test_non_conforming(self) -> None:
        '''
            Verifies non-conforming object fails IFlowBarrier check.
        '''
        self.assertFalse(isinstance(object(), IFlowBarrier))


if __name__ == '__main__':
    main()

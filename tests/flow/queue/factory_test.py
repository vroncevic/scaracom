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
    Unit tests for QueueFactory component.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.flow.queue.factory import QueueFactory
from scaracom.flow.queue.iqueue import IFrameQueue
from scaracom.flow.queue.provides import QueueProvides
from scaracom.flow.queue.queue import FrameQueue

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestQueueFactory(TestCase):
    '''
        Test suite verifying QueueFactory component instantiation and wiring.

        It defines:

            :methods:
                | test_create - Verifies QueueProvides creation.
                | test_structural_typing - Verifies queue satisfies IFrameQueue.
                | test_get_version - Verifies factory semantic version string.
    '''

    def test_create(self) -> None:
        '''
            Verifies factory creates a valid QueueProvides instance.
        '''
        provides: QueueProvides = QueueFactory.create()
        self.assertIsInstance(provides, QueueProvides)
        self.assertIsInstance(provides.queue, FrameQueue)

    def test_structural_typing(self) -> None:
        '''
            Verifies created queue satisfies IFrameQueue protocol.
        '''
        provides: QueueProvides = QueueFactory.create()
        self.assertTrue(isinstance(provides.queue, IFrameQueue))

    def test_get_version(self) -> None:
        '''
            Verifies factory returns a valid semantic version string.
        '''
        version: str = QueueFactory.get_version()
        self.assertIsInstance(version, str)
        self.assertEqual(version, '1.0.0')


if __name__ == '__main__':
    main()

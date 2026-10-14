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
    Unit tests for ReaderWorkerFactory.
'''

from __future__ import annotations

from threading import Event
from unittest import TestCase
from unittest.mock import Mock

from scaracom.bridge.worker.dependencies import WorkerDependencies
from scaracom.bridge.worker.factory import ReaderWorkerFactory
from scaracom.bridge.worker.iworker import ITransportReaderWorker

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReaderWorkerFactoryTestCase(TestCase):
    '''
        Verifies ReaderWorkerFactory behaviors.
    '''

    def test_create_returns_worker(self) -> None:
        '''
            Verifies factory creates ITransportReaderWorker instance.
        '''
        deps = WorkerDependencies(
            transport=Mock(),
            listener=Mock(),
            stop_event=Event(),
        )
        worker = ReaderWorkerFactory.create(deps)
        self.assertTrue(isinstance(worker, ITransportReaderWorker))

    def test_get_version(self) -> None:
        '''
            Verifies factory version returns valid string.
        '''
        self.assertEqual(ReaderWorkerFactory.get_version(), '0.1.0')

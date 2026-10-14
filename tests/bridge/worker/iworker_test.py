# -*- coding: UTF-8 -*-

'''
Module
    iworker_test.py
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
    Unit tests for ITransportReaderWorker protocol.
'''

from __future__ import annotations

from threading import Event
from unittest import TestCase
from unittest.mock import Mock

from scaracom.bridge.worker.dependencies import WorkerDependencies
from scaracom.bridge.worker.iworker import ITransportReaderWorker
from scaracom.bridge.worker.worker import TransportReaderWorker

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TransportReaderWorkerProtocolTestCase(TestCase):
    '''
        Verifies ITransportReaderWorker runtime checkable protocol.
    '''

    def test_worker_implements_protocol(self) -> None:
        '''
            Verifies TransportReaderWorker satisfies ITransportReaderWorker.
        '''
        deps = WorkerDependencies(
            transport=Mock(),
            listener=Mock(),
            stop_event=Event(),
        )
        worker = TransportReaderWorker(deps)
        self.assertTrue(isinstance(worker, ITransportReaderWorker))

    def test_non_worker_fails_protocol(self) -> None:
        '''
            Verifies non-conforming object fails ITransportReaderWorker check.
        '''
        self.assertFalse(isinstance(object(), ITransportReaderWorker))

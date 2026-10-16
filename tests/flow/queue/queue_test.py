# -*- coding: UTF-8 -*-

'''
Module
    queue_test.py
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
    Unit tests for FrameQueue component.
'''

from __future__ import annotations

from queue import Empty
from unittest import TestCase
from unittest import main
from unittest.mock import MagicMock, patch

from scaracom.flow.queue.queue import FrameQueue

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestFrameQueue(TestCase):
    '''
        Unit test cases verifying FrameQueue buffering and timeout behaviors.

        It defines:

            :methods:
                | setUp - Initializes FrameQueue test instance.
                | test_put_and_get - Verifies enqueue and dequeue operations.
                | test_get_timeout - Verifies timeout on empty buffer returns failure tuple.
                | test_size - Verifies queue item count tracking.
                | test_clear - Verifies clearing queued frames.
                | test_bounded_overflow - Verifies overflow behavior on saturated buffer.
                | test_get_version - Verifies version string retrieval.
    '''

    _queue: FrameQueue

    def setUp(self) -> None:
        '''
            Sets up test fixture with FrameQueue instance.
        '''
        self._queue = FrameQueue()

    def test_put_and_get(self) -> None:
        '''
            Verifies successful enqueue and dequeue of frame data.
        '''
        success: bool = self._queue.put_frame(b'\x01\x02\x03')
        self.assertTrue(success)
        self.assertEqual(self._queue.size(), 1)

        ok, data = self._queue.get_frame(timeout_sec=0.1)
        self.assertTrue(ok)
        self.assertEqual(data, b'\x01\x02\x03')
        self.assertEqual(self._queue.size(), 0)

    def test_get_timeout(self) -> None:
        '''
            Verifies get_frame returns (False, b'') on timeout.
        '''
        ok, data = self._queue.get_frame(timeout_sec=0.02)
        self.assertFalse(ok)
        self.assertEqual(data, b'')

    def test_size(self) -> None:
        '''
            Verifies size reflects number of queued items.
        '''
        self.assertEqual(self._queue.size(), 0)
        self._queue.put_frame(b'frame1')
        self._queue.put_frame(b'frame2')
        self.assertEqual(self._queue.size(), 2)

    def test_clear(self) -> None:
        '''
            Verifies clear removes all pending frames and handles race condition.
        '''
        self._queue.put_frame(b'frame1')
        self._queue.put_frame(b'frame2')
        self._queue.clear()
        self.assertEqual(self._queue.size(), 0)

        mock_raw_queue = MagicMock()
        mock_raw_queue.empty.side_effect = [False, True]
        mock_raw_queue.get_nowait.side_effect = Empty
        with patch('scaracom.flow.queue.queue.Queue', return_value=mock_raw_queue):
            race_queue = FrameQueue()
            race_queue.clear()

    def test_bounded_overflow(self) -> None:
        '''
            Verifies bounded queue rejects items when capacity is reached.
        '''
        bounded = FrameQueue(maxsize=1)
        self.assertTrue(bounded.put_frame(b'item1'))
        self.assertFalse(bounded.put_frame(b'item2'))

    def test_get_version(self) -> None:
        '''
            Verifies get_version returns valid semantic version string.
        '''
        version: str = self._queue.get_version()
        self.assertIsInstance(version, str)
        self.assertEqual(version, '1.0.1')


if __name__ == '__main__':
    main()

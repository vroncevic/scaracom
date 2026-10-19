# -*- coding: UTF-8 -*-

'''
Module
    router_test.py
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
    Unit tests for FrameRouter component.
'''

from __future__ import annotations

from dataclasses import dataclass
from unittest import TestCase
from unittest import main
from unittest.mock import Mock

from scaracom.flow.router.ihandler import IFrameHandler
from scaracom.flow.router.router import FrameRouter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass(frozen=True, slots=True)
class SampleFrame:
    '''
        Sample frame implementing IRoutedFrame structurally for tests.
    '''

    msg_id: int
    seq_num: int = 0
    payload: bytes = b''
    crc16: int = 0


class TestFrameRouter(TestCase):
    '''
        Unit test cases verifying FrameRouter registration and dispatch.

        It defines:

            :methods:
                | setUp - Initializes FrameRouter and mock handler.
                | test_register_and_route - Verifies frame routing to registered handler.
                | test_route_unregistered - Verifies routing with no registered handler.
                | test_unregister_handler - Verifies handler unregistration stops dispatch.
                | test_exception_safety - Verifies handler exceptions are swallowed.
                | test_invalid_frame - Verifies routing object without msg_id returns False.
                | test_get_version - Verifies version string retrieval.
    '''

    _router: FrameRouter
    _handler: Mock

    def setUp(self) -> None:
        '''
            Sets up test fixture with FrameRouter and mock handler.

            :exceptions: None.
        '''
        self._router = FrameRouter()
        self._handler = Mock(spec=IFrameHandler)

    def test_register_and_route(self) -> None:
        '''
            Verifies frame dispatch to registered handler.

            :exceptions: None.
        '''
        frame = SampleFrame(msg_id=1, seq_num=0, payload=b'', crc16=0)
        self._router.register_handler(1, self._handler)
        result: bool = self._router.route(frame)
        self.assertTrue(result)
        self._handler.handle_frame.assert_called_once_with(frame)

    def test_route_unregistered(self) -> None:
        '''
            Verifies routing frame without registered handler returns False.

            :exceptions: None.
        '''
        frame = SampleFrame(msg_id=99, seq_num=0, payload=b'', crc16=0)
        result: bool = self._router.route(frame)
        self.assertFalse(result)
        self._handler.handle_frame.assert_not_called()

    def test_unregister_handler(self) -> None:
        '''
            Verifies unregistered handler no longer receives dispatched frames.

            :exceptions: None.
        '''
        frame = SampleFrame(msg_id=3, seq_num=0, payload=b'', crc16=0)
        self._router.register_handler(3, self._handler)
        self._router.unregister_handler(3, self._handler)
        result: bool = self._router.route(frame)
        self.assertFalse(result)
        self._handler.handle_frame.assert_not_called()

    def test_exception_safety(self) -> None:
        '''
            Verifies handler exceptions do not propagate.

            :exceptions: None.
        '''
        frame = SampleFrame(msg_id=4, seq_num=0, payload=b'', crc16=0)
        self._handler.handle_frame.side_effect = RuntimeError('Handler failed')
        self._router.register_handler(4, self._handler)
        result: bool = self._router.route(frame)
        self.assertTrue(result)

    def test_invalid_frame(self) -> None:
        '''
            Verifies routing object without msg_id attribute returns False.

            :exceptions: None.
        '''
        result: bool = self._router.route(object())  # type: ignore[arg-type]
        self.assertFalse(result)

    def test_get_version(self) -> None:
        '''
            Verifies get_version returns valid semantic version string.

            :exceptions: None.
        '''
        version: str = self._router.get_version()
        self.assertEqual(version, '1.0.2')


if __name__ == '__main__':
    main()

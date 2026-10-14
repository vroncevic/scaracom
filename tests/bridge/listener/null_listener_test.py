# -*- coding: UTF-8 -*-

'''
Module
    null_listener_test.py
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
    Unit tests for NullTransportListener.
'''

from __future__ import annotations

from unittest import TestCase

from scaracom.bridge.listener.null_listener import NullTransportListener

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '0.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class NullTransportListenerTestCase(TestCase):
    '''
        Verifies NullTransportListener behaviors.
    '''

    def test_callbacks_execute_silently(self) -> None:
        '''
            Verifies all callbacks can be called without side effects or exceptions.
        '''
        listener = NullTransportListener()
        listener.on_line_received('G0 X10')
        listener.on_bytes_received(b'\xaa\x55')
        listener.on_log_emitted('Log message', True)
        listener.on_log_emitted('Log message', False)

    def test_get_version(self) -> None:
        '''
            Verifies version method returns valid string.
        '''
        listener = NullTransportListener()
        self.assertEqual(listener.get_version(), '0.1.0')

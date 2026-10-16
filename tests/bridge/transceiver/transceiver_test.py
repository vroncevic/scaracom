# -*- coding: UTF-8 -*-

'''
Module
    transceiver_test.py
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
    Unit tests for RawTransceiver.
'''

from __future__ import annotations

from unittest import TestCase
from unittest.mock import Mock

from scaracom.bridge.transceiver.dependencies import TransceiverDependencies
from scaracom.bridge.transceiver.transceiver import RawTransceiver

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class RawTransceiverTestCase(TestCase):
    '''
        Verifies RawTransceiver behaviors.
    '''

    def test_is_connected(self) -> None:
        '''
            Verifies is_connected delegates to transport.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        deps = TransceiverDependencies(transport=mock_transport, listener=Mock())
        transceiver = RawTransceiver(deps)
        self.assertTrue(transceiver.is_connected())

        mock_transport.is_connected.return_value = False
        self.assertFalse(transceiver.is_connected())

    def test_send_raw_command_not_connected(self) -> None:
        '''
            Verifies send_raw_command returns False when disconnected.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = False
        deps = TransceiverDependencies(transport=mock_transport, listener=Mock())
        transceiver = RawTransceiver(deps)
        self.assertFalse(transceiver.send_raw_command('G0 X0 Y0'))

    def test_send_raw_command_success(self) -> None:
        '''
            Verifies send_raw_command logs TX and writes newline terminated bytes.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        mock_transport.write_bytes.return_value = True
        mock_listener = Mock()
        deps = TransceiverDependencies(transport=mock_transport, listener=mock_listener)
        transceiver = RawTransceiver(deps)

        result = transceiver.send_raw_command('  G0 X10 Y20  ')
        self.assertTrue(result)
        mock_listener.on_log_emitted.assert_called_with('[TX]: G0 X10 Y20', True)
        mock_transport.write_bytes.assert_called_with(b'G0 X10 Y20\n')

    def test_send_raw_command_exception_handled(self) -> None:
        '''
            Verifies send_raw_command logs error and returns False on exception.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        mock_transport.write_bytes.side_effect = IOError('Write error')
        mock_listener = Mock()
        deps = TransceiverDependencies(transport=mock_transport, listener=mock_listener)
        transceiver = RawTransceiver(deps)

        result = transceiver.send_raw_command('CMD')
        self.assertFalse(result)
        mock_listener.on_log_emitted.assert_called_with('[ERR]: Send error: Write error', False)

    def test_send_raw_bytes_not_connected(self) -> None:
        '''
            Verifies send_raw_bytes returns False when disconnected.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = False
        deps = TransceiverDependencies(transport=mock_transport, listener=Mock())
        transceiver = RawTransceiver(deps)
        self.assertFalse(transceiver.send_raw_bytes(b'\xaa\x55'))

    def test_send_raw_bytes_success(self) -> None:
        '''
            Verifies send_raw_bytes logs hex and writes bytes.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        mock_transport.write_bytes.return_value = True
        mock_listener = Mock()
        deps = TransceiverDependencies(transport=mock_transport, listener=mock_listener)
        transceiver = RawTransceiver(deps)

        result = transceiver.send_raw_bytes(b'\xaa\x55\x01')
        self.assertTrue(result)
        mock_listener.on_log_emitted.assert_called_with('[TX]: (HEX) aa5501', True)
        mock_transport.write_bytes.assert_called_with(b'\xaa\x55\x01')

    def test_send_raw_bytes_exception_handled(self) -> None:
        '''
            Verifies send_raw_bytes logs error and returns False on exception.
        '''
        mock_transport = Mock()
        mock_transport.is_connected.return_value = True
        mock_transport.write_bytes.side_effect = IOError('Binary error')
        mock_listener = Mock()
        deps = TransceiverDependencies(transport=mock_transport, listener=mock_listener)
        transceiver = RawTransceiver(deps)

        result = transceiver.send_raw_bytes(b'\xaa')
        self.assertFalse(result)
        mock_listener.on_log_emitted.assert_called_with('[ERR]: Binary send error: Binary error', False)

    def test_get_version(self) -> None:
        '''
            Verifies version returns valid semantic string.
        '''
        deps = TransceiverDependencies(transport=Mock(), listener=Mock())
        transceiver = RawTransceiver(deps)
        self.assertEqual(transceiver.get_version(), '1.0.1')

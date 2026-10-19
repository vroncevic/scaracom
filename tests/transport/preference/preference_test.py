# -*- coding: UTF-8 -*-

'''
Module
    preference_test.py
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
    Unit tests for SerialPreference model in scaracom.transport.preference.
'''

from __future__ import annotations

from dataclasses import FrozenInstanceError
from unittest import TestCase
from unittest import main

from scaracom.transport.preference.preference import SerialPreference

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSerialPreference(TestCase):
    '''
        Unit test cases verifying SerialPreference value object attributes and immutability.

        It defines:

            :methods:
                | test_initialization - Verifies attribute initialization.
                | test_immutability - Verifies FrozenInstanceError on attribute mutation.
                | test_equality - Verifies value-based equality comparison.
    '''

    def test_initialization(self) -> None:
        '''
            Verifies creation with valid port and baud attributes.

            :exceptions: None.
        '''
        pref = SerialPreference(port='/dev/ttyUSB0', baud=115200)
        self.assertEqual(pref.port, '/dev/ttyUSB0')
        self.assertEqual(pref.baud, 115200)

    def test_immutability(self) -> None:
        '''
            Verifies preference cannot be modified after instantiation.

            :exceptions: None.
        '''
        pref = SerialPreference(port='/dev/ttyACM0', baud=9600)
        with self.assertRaises(FrozenInstanceError):
            pref.port = '/dev/ttyACM1'  # type: ignore[misc]

    def test_equality(self) -> None:
        '''
            Verifies value equality across identical instances.

            :exceptions: None.
        '''
        pref1 = SerialPreference(port='/dev/ttyACM0', baud=115200)
        pref2 = SerialPreference(port='/dev/ttyACM0', baud=115200)
        pref3 = SerialPreference(port='/dev/ttyUSB0', baud=115200)
        self.assertEqual(pref1, pref2)
        self.assertNotEqual(pref1, pref3)


if __name__ == '__main__':
    main()

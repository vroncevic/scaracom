# -*- coding: UTF-8 -*-

'''
Module
    irepository_test.py
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
    Unit tests for ISerialPreferenceRepository structural protocol in scaracom.transport.preference.
'''

from __future__ import annotations

from unittest import TestCase
from unittest import main

from scaracom.transport.preference.irepository import ISerialPreferenceRepository
from scaracom.transport.preference.preference import SerialPreference

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DummyRepository:
    '''
        Structural stub implementing ISerialPreferenceRepository contract.

        It defines:

            :methods:
                | has_preference - Checks preference availability.
                | load_preference - Loads dummy preference.
                | save_preference - Saves preference.
                | get_version - Returns version string.
    '''

    def has_preference(self) -> bool:
        '''
            Checks preference availability.

            :return: Always True for test stub.
            :exceptions: None.
        '''
        return True

    def load_preference(self) -> SerialPreference:
        '''
            Loads dummy preference.

            :return: Dummy SerialPreference instance.
            :exceptions: None.
        '''
        return SerialPreference(port='/dev/ttyACM0', baud=115200)

    def save_preference(self, preference: SerialPreference) -> bool:
        '''
            Saves preference.

            :param preference: Preference to save.
            :return: Always True for test stub.
            :exceptions: None.
        '''
        _ = preference
        return True

    def get_version(self) -> str:
        '''
            Returns version string.

            :return: Semantic version string.
            :exceptions: None.
        '''
        return '1.0.1'


class IncompleteRepository:
    '''
        Incomplete class missing save_preference.

        It defines:

            :methods:
                | has_preference - Checks preference availability.
                | extra_action - Secondary action not matching protocol.
    '''

    def has_preference(self) -> bool:
        '''
            Checks preference availability.

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


class TestISerialPreferenceRepository(TestCase):
    '''
        Unit test cases verifying ISerialPreferenceRepository runtime typing.

        It defines:

            :methods:
                | test_structural_typing - Verifies dummy satisfies protocol.
                | test_incomplete_class - Verifies incomplete class fails protocol check.
    '''

    def test_structural_typing(self) -> None:
        '''
            Verifies DummyRepository satisfies ISerialPreferenceRepository.

            :exceptions: None.
        '''
        repo = DummyRepository()
        self.assertIsInstance(repo, ISerialPreferenceRepository)

    def test_incomplete_class(self) -> None:
        '''
            Verifies incomplete class does not satisfy protocol.

            :exceptions: None.
        '''
        incomplete = IncompleteRepository()
        self.assertNotIsInstance(incomplete, ISerialPreferenceRepository)


if __name__ == '__main__':
    main()

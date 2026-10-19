# -*- coding: UTF-8 -*-

'''
Module
    irepository.py
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
    Defines ISerialPreferenceRepository structural protocol for serial preference persistence.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from scaracom.transport.preference.preference import SerialPreference

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ISerialPreferenceRepository(Protocol):
    '''
        Structural protocol defining serial device preference persistence operations.

        It defines:

            :methods:
                | has_preference - Checks if saved preference configuration exists.
                | load_preference - Reads stored serial connection preference.
                | save_preference - Persists active serial connection preference.
                | get_version - Returns repository semantic version string.
    '''

    def has_preference(self) -> bool:
        '''
            Checks if saved preference configuration exists.

            :return: True if preference exists, False otherwise.
        '''

    def load_preference(self) -> SerialPreference:
        '''
            Reads stored serial connection preference.

            :return: Loaded SerialPreference instance.
        '''

    def save_preference(self, preference: SerialPreference) -> bool:
        '''
            Persists active serial connection preference.

            :param preference: SerialPreference instance to persist.
            :return: True if persisted successfully, False otherwise.
        '''

    def get_version(self) -> str:
        '''
            Returns repository semantic version string.

            :return: Semantic version string.
        '''

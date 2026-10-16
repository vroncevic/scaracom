# -*- coding: UTF-8 -*-

'''
Module
    ireceiver.py
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
    Interface protocol for background transport receiver threads.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/scaracom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/scaracom/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ITransportReceiver(Protocol):
    '''
        Structural protocol defining background polling transport receivers.

        It defines:

            :methods:
                | is_running - Checks if receiver loop termination event is not set.
                | run - Executes background read loop until stopped or disconnect detected.
                | get_version - Returns receiver component version string.
    '''

    def is_running(self) -> bool:
        '''
            Checks if receiver loop termination event is not set.

            :return: True if running, False otherwise.
        '''

    def run(self) -> None:
        '''
            Executes background read loop until stopped or disconnect detected.
        '''

    def get_version(self) -> str:
        '''
            Returns receiver component version string.

            :return: Semantic version string.
        '''

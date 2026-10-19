#!/bin/bash
#
# @brief   scaracom
# @version 1.0.2
# @date    Wed Oct 14 09:50:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py scaracom
pylint scaracom > scaracom.report
echo "Done"

#!/bin/bash
#
# @brief   scaracom
# @version 1.0.1
# @date    Wed Oct 14 09:50:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py scaracom
python3 gates/gates/isp_checker.py scaracom
python3 gates/gates/limits_checker.py scaracom
python3 gates/gates/srp_checker.py scaracom

echo "Done"

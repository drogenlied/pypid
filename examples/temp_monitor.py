#!/usr/bin/env python
# Copyright (C) 2011 W. Trevor King <wking@drexel.edu>
#
# This file is part of tempcontrol.
#
# tempcontrol is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# tempcontrol is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with tempcontrol.  If not, see
# <http://www.gnu.org/licenses/>.

"""Log control and ambient temperature every 10 seconds.

usage: python temp_monitor.py
"""

import time

from tempcontrol.backend import get_backend


b = get_backend('melcor')()
period = 10

with open('temp_monitor.log', 'a') as f:
    last = time.time()
    last -= last % period
    next_time = last + period
    while True:
        time.sleep(next_time - time.time())
        tstr = time.strftime('%Y-%m-%d %H:%M:%S')
        temp = str(b.get_temp())
        ambient = str(b.get_ambient_temp())
        f.write('\t'.join([tstr, temp, ambient]) + '\n')
        f.flush()
        print('\t'.join([tstr, temp, ambient]))
        next_time += period
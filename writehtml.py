#!/usr/bin/env python3

import datetime

dt = datetime.datetime.now()
with open('index.html', 'w') as f:
    f.write('<h1>Hello world</h1>')
    f.write('<b>Deploy time</b>')
    f.write(str(dt))


# singlebar
[![Build Status](https://travis-ci.org/ericedem/singlebar.svg?branch=master)](https://travis-ci.org/ericedem/singlebar)

Progressbar that increments one item at a time.

To use, put this in your requirements.txt `git+ssh://github.com/ericedem/singlebar#egg=singlebar`

Example Code:

```
import singlebar as bar
from time import sleep

n = 100
bar.start(n)

for i in range(n):
    bar.update()
    sleep(.1)

bar.finish()
```

Output:

```
$ ../env/bin/python example.py 
[===================================                              ]  55% ETA:  0:00:04
```

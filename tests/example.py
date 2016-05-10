from context import singlebar
from time import sleep

n = 100
singlebar.start(n)

for i in range(n):
    singlebar.update()
    sleep(.1)

singlebar.finish()

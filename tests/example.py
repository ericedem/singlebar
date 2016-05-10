from context import bar
from time import sleep

n = 100
bar.start(n)

for i in range(n):
    bar.update()
    sleep(.1)

bar.finish()

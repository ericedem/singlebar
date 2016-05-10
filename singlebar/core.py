
# singleton for managing this silly progress bar
import progressbar

bar = None
count = 0


def start(total):
    if total == 0:
        return
    global bar, count
    bar = progressbar.ProgressBar(maxval=total,
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage(), ' ', progressbar.ETA()])
    count = 0
    bar.start()


def update():
    global bar, count
    count += 1
    bar.update(count)


def finish():
    bar.finish()

__author__ = 'ericedem'

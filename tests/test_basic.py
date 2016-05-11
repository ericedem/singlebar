from .context import singlebar as bar


def test_import():
    bar.start(1)
    bar.finish()

#!/bin/sh
python setup.py sdist
curl -F file=@dist/singlebar* $GEMFURY_REPO

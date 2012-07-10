#!/usr/bin/env python

from __future__ import print_function
from distutils.core import setup, Command
from glob import glob
import os

scripts = glob(os.path.join('scripts', '*'))

setup(name='zoonibot',
      version='0.1.0',
      packages=['zoonibot'],
      scripts=scripts
)
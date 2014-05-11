import os
from os.path import join as ospj
import subprocess
import sys

from distutils.core import setup, Extension

setup(
    name="unicodetest",
    version="1.0",
    py_modules=['unicodetest'],
    ext_modules=[
        Extension(
            "_unicodetest",
            [
                "unicodetest_wrap.c",
                "unicodetest.c",
            ],
        ),
    ],
)

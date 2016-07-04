from distutils.core import setup
from pkgutil import walk_packages

import glob
import sys
import os


data_files = []


for x in os.walk('modules'):
    data_files.append(
            (sys.prefix + '/ipmicons/' + '/'.join(os.path.split(x[0])),
            glob.glob(os.path.join(x[0], '*.py')) + \
            glob.glob(os.path.join(x[0], 'LICENSE')) + \
            glob.glob(os.path.join(x[0], 'Makefile')) + \
            glob.glob(os.path.join(x[0], '*.cfg')) + \
            glob.glob(os.path.join(x[0], '*.rst')) + \
            glob.glob(os.path.join(x[0], '*.bat')) + \
            glob.glob(os.path.join(x[0], 'README*'))
            )
    )


setup(
        name = "ipmicons",
        version = "0.1",
        author = "helloarys",
        author_email = "helloarys@email.com",
        url = "https://github.com/InfraSIM/ipmi_console.git",
        packages = ["ipmicons"],
        platforms = "Linux",
        classifiers = [
            "Intended Audience :: Developers",
            "Operating System :: Linux",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
        ],
        scripts = ["ipmi_sim.py"],
        data_files = data_files,
)

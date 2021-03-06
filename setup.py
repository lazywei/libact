#!/usr/bin/env python

from distutils.core import setup, Extension
import numpy.distutils
import sys

if sys.platform == 'darwin':
    print("Platform Detection: Mac OS X. Link to openblas...")
    extra_link_args = ['-L/usr/local/opt/openblas/lib -lopenblas']
    include_dirs = (numpy.distutils.misc_util.get_numpy_include_dirs() +
                    ['/usr/local/opt/openblas/include'])
else:
    # assume linux otherwise, unless we support Windows in the future...
    print("Platform Detection: Linux. Link to liblapacke...")
    extra_link_args = ['-llapacke -llapack -lblas']
    include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs()

setup(
    name='libact',
    version='0.1',
    description='Pool-based active learning in Python',
    long_description='Pool-based active learning in Python',
    author='Y.-A. Chung, S.-C. Lee, T.-E. Wu, Y.-Y. Yang, H.-T. Lin',
    author_email='lsc36x@gmail.com',
    url='https://github.com/ntucllab/libact',
    packages=[
        'libact.base',
        'libact.models',
        'libact.labelers',
        'libact.query_strategies',
        ],
    package_dir={
        'libact.base': 'libact/base',
        'libact.models': 'libact/models',
        'libact.labelers': 'libact/labelers',
        'libact.query_strategies': 'libact/query_strategies',
        },
    ext_modules=[
        Extension(
            "libact.query_strategies._variance_reduction",
            ["libact/query_strategies/variance_reduction.c"],
            extra_link_args=extra_link_args,
            extra_compile_args=['-std=c11'],
            include_dirs=include_dirs,
            ),
        ],
    )

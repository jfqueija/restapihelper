#! usr/bin/python
# -*- coding: utf-8 *-* 

__author__='pepekiko@gmail.com'

from distutils.core import setup
setup(
    name = 'restapihelper',
    packages = ['restapihelper'],
    version = '0.1.2',
    description = 'Rest API Helper',
    author = 'José Fº Queija',
    author_email = 'pepekiko@gmail.com',
    url = 'https://github.com/jfqueija/restapihelper',
    download_url = 'https://github.com/jfqueija/restapihelper/tarball/0.1.1',
    keywords = ['restapihelper','Rest','API','Caller','Helper'],    
    classifiers = [  
        # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['requests','urllib3']
)
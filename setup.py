import sys, requests
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
long_description += '\n\n'

setup(
    name='pippkg-api',
    version='0.0.2',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='UnOfficial PyPi API Wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/M4cs/PipPKG-API',
    packages=['pippkgapi'],
    install_requires=['requests'],
    project_urls={
        'Wiki': 'https://github.com/M4cs/PipPKG-API/blob/master/README.md',
        'Discord Server': 'https://discordapp.com/invite/7VN9VZe'
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
    )

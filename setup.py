from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'CHANGELOG.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='knockpy',
    version='4.1.1',

    description='Knock is a python tool designed to enumerate subdomains on a target domain through a wordlist.',
    long_description=long_description,
    url='https://github.com/devAgam/KnockPy-Python3',

    author='Gianni \'guelfoweb\' Amato',
    author_email='guelfoweb@gmail.com',

    license='GNU',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License (GPL)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.*',
        "I'll try to keep this working I'm Still testing this im not sure how well this works"
    ],

    keywords='knock sudbomain scan',

    packages=["knockpy", "knockpy.modules"],
    package_data={
        'knockpy': ['wordlist/*.txt', '*.json'],
    },

    install_requires=['dnspython>=1.3.5'],

    entry_points={
        'console_scripts': [
            'knockpy=knockpy.knockpy:main',
        ],
    },

)

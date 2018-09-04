"""
Python setup file for the yuriko app.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.

If all looks good, you can make your first release:

    python setup.py sdist upload

For new releases, you need to bump the version number in
tornado_botocore/__init__.py and re-run the above command.

For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html
"""

from setuptools import find_packages, setup


setup(
    name="yuriko",
    version='0.0.1',
    description="Encrypted notes",
    long_description="Encrypted notes",
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='encrypted, notes',
    author='Oleksandr Polieno',
    author_email='polyenoom@gmail.com',
    url="https://github.com/nanvel/yuriko",
    packages=find_packages(),
    install_requires=[
        'pycrypto'
    ],
    entry_points={
        'console_scripts': [
            'yuriko = yuriko.main:main'
        ]
    }
)

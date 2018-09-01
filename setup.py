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

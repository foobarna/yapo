from setuptools import setup

import yapo

requires = [
]

with open('README.rst', 'r') as file:
    long_description = file.read()

setup(
    name=yapo.__title__,
    version=yapo.__version__,
    author=yapo.__author__,
    author_email=yapo.__author_email__,
    url=yapo.__url__,
    description=yapo.__description__,
    long_description=long_description,
    license=yapo.__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Text Processing :: Markup :: XML',
    ],
    keywords='xml parser objectify painless',
    packages=['yapo'],
    install_requires=requires
)

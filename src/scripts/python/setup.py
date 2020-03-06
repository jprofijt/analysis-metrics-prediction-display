#! /usr/bin/env python2.7

from distutils.core import setup

setup(
    name='QualityParser',
    version='1.0',
    description='Quality metrics parser applications',
    author='Jouke Profijt',
    author_email='jouke.profijt@gmail.com',
    packages=['QualityParser', 'QualityParser.DataTypes', 'QualityParser.DataBase', 'QualityParser.Parsers'],
)
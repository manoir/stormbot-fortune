#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='stormbot-fortune',
      version='1.2',
      description='fortune plugin for stormbot',
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://git.paulfariello.fr/Stormbot/stormbot-fortune',
      packages=find_packages(),
      package_data={'stormbot_fortune': ['data/*.dic']},
      install_requires=['Stormbot'],
      entry_points={'stormbot.plugins': ['fortune = stormbot_fortune:Fortune']},
      classifiers=['Environment :: Console',
                   'Intended Audience :: System Administrators',
                   'Operating System :: POSIX',
                   'Programming Language :: Python'])

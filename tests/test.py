import sys
from stormbot import storage, bot
from stormbot_fortune import Fortune
from unittest.mock import patch
from nose.tools import *
import logging

@bot.mock(['fortune', '-h'])
@storage.mock({'fortunes': {'author': ['fortune']}})
def test_help(stdout):
    # When
    bot.main(Fortune)

    # Then
    eq_("\n".join(stdout.getvalue().splitlines()[:-1]), """usage: fortune [-h] [--fortune-dict FORTUNE_DICT] [_ [_ ...]]

positional arguments:
  _

optional arguments:
  -h, --help            show this help message and exit
  --fortune-dict FORTUNE_DICT
                        Dictionnary to use for fortune (default: kaamelott)""")


if __name__ == '__main__':
    import nose
    nose.runmodule()

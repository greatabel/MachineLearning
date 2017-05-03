import os
try:
    import ujson as json  # UltraJSON if available
except:
    import json
import sys
from collections import defaultdict

try:
    # http://stackoverflow.com/questions/3683181/cannot-install-pyenchant-on-osx
    # 安装步骤如下：
    # brew install enchant
    # pip3.5 install PyEnchant
    import enchant
    speller = enchant.Dict("en_US")

except:
    print("""\
Enchant is not installed, which is not a problem since spell correction features
will not be used in the chapter. If, however, you want to experiment with them
(highly encouraged!), you can get the library from http://packages.python.org/pyenchant/.
""")

class EnchantMock:

    def __init__(self):
        pass

    def check(self, word):
        return True

speller = EnchantMock()


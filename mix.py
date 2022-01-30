import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from mix import __start__
    __start__()
elif bit == '32bit':
    from mix import __start__
    __start__()

import sys, os

from crawler.settings import path
if path not in sys.path:
    sys.path.append(path)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crz6.settings")
django.setup()

from front.models  import Coser

import time

class DBCRM(object):

    def Coser_Save(self, item):
        coser = Coser()
        try:
            coser.title = item["title"]
            coser.Rurl  = item["Rurl"]
            coser.url   = item["url"]
            coser.save()
        except Exception as e:

            print(e)
            time.sleep(60)
            pass

    pass
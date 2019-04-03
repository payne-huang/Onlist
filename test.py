import os

from operator import itemgetter, attrgetter
def cmpx(x, y):

    return x[0]-y[0]
s = [{'a':u'2019-01-31T02:53:32Z'},{'a':u'2019-01-30T02:53:32Z'}]
print sorted(s,  key=lambda x:x["a"], reverse=True)


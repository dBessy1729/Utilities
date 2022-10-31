#! /usr/bin/python
'''
  Usage: python dtg.py or import as dtg.

  Output: Returns a DTG string that can be used in filenames,
          log timestamps etc. If ran as script, will print 
          the DTG string.
'''
import datetime

def pad(myInt):
    if myInt < 10:
        myInt = '0' + str(myInt)
    return myInt

def dtg():
    basedate = datetime.datetime.now()
    y = basedate.year
    m = pad(basedate.month)
    d = basedate.day
    H = pad(basedate.hour)
    M = pad(basedate.minute)
    S = pad(basedate.second)
    return '%s%s%s-%s%s%s' % (y, m, d, H, M, S)

if __name__ == '__main__':
    print dtg()

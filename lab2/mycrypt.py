import codecs
import string
import time
import threading

class ConstantTime():
    def __init__(self, length):
        self.length = length

    def __enter__(self):
        self.timer = threading.Thread(target=time.sleep, args=[self.length])
        self.timer.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.timer.join()
        
def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    if origlen > 1000:
        raise ValueError
    "{:<999}".format(s) 
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    with ConstantTime(0.1):
        for c in s:
            if c in ['+', 'å', 'ä','ö']:
                raise ValueError
            elif c.isalpha():
                c = c.upper()
                crypted += codecs.encode(c, 'rot13')
            else:
                crypted += digitmapping[c]

    return crypted[:origlen]
   
def decode(s):
    return encode(s).lower()

import codecs
import string

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    "{:<999}".format(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
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


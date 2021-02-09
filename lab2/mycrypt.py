import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    s = s.ljust(1000, 'a')
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if isalpha(c):
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            else:
            	c=c.lower()
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError

    return crypted[:origlen]

def decode(s):
    return encode(s)
    
def isalpha(c):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z']
    if c in alphabet:
        return True
    else:
        return False

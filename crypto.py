#coding utf-8

import js2py
import sys

rsa =''' 
var rsaKey = new RSAKey();
rsaKey.setPublic(b64tohex("%s"), b64tohex("%s"));
var enPassword = hex2b64(rsaKey.encrypt("%s"));
'''
with open('./rsa2.js') as fp:
    js = fp.read()
    context = js2py.EvalJs()
    rsa = rsa % (sys.argv[1], sys.argv[2], sys.argv[3])
    context.execute(js + rsa)
print(context.enPassword)

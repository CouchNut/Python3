#!/usr/local/bin python3

# -*- coding: utf-8 -*-

print('---------- BytesIO ----------')

from io import BytesIO

f = BytesIO()
s =  f.write('中文'.encode('utf-8'))
print(s)
print(f.getvalue())

print('--------------------')
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())





































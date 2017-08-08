#!/usr/local/bin python3

# -*- coding: utf-8 -*-

print('---------- 序列化 ----------')

import pickle
d = dict(name='Bob', age=20, score=98)
print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)













































































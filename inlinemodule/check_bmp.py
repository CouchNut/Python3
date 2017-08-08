#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 要把一个32位无符号整数变成字节，也就是4个长度的bytes，
# 你得配合位运算符这么写：

n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

import struct
# struct 的 pack 函数把任意数据类型变成 bytes
print(struct.pack('>I', 10240099))
'''
pack的第一个参数是处理指令，'>I'的意思是：

>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

后面的参数个数要和处理指令一致。
'''
# struct 的 unpack 把 bytes 变成相应的数据类型
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。





































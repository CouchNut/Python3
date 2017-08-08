#!/usr/local/bin python3

# -*- coding: utf-8 -*-

import hashlib

print('----- MD5 -----')
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

print('----- SHA1 -----')
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


def get_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

# 加盐
def calc_md5(password, salt):
	return get_md5(password + salt)

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }

# def login(user, password):
#     return calc_md5(password) == db[user]

# print(login('michael', '123456'))

database = {
	
}

def register(username, password):
	database[username] = calc_md5(password, username)
	print(database)

def login(user, password):
    return calc_md5(password, user) == database[user]

register('copper', 'awef')
register('Bob', 'bob')

print(login('copper', 'awef'))




















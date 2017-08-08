#!/usr/local/bin python3

# -*- coding: utf-8 -*-

print('---------- JSON ----------')

import json
# d = dict(name='Bob', age=20, score=88)

# print(json.dumps(d))

# json_str = '{"name": "Bob", "age": 20, "score": 88}'
# print(json.loads(json_str))



class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return {
		'name' 	: std.name,
		'age'	: std.age,
		'score' : std.score
	}

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

print('---------- student2json ----------')
s = Student('Bon', 20, 88)
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))


print('---------- json2student ----------')
student_json = '{"name": "Bon", "age": 20, "score": 88}'
print(json.loads(student_json, object_hook=dict2student))











#!/usr/bin/python

import sys
import os

os.system('clear')

num = int(open('count', 'r').readline())

pyth = 'python3'

def check_c(name):
	global num
	os.system('rm a.out')
	os.system('g++ -std=c++0x -Wextra -march=atom -O2 -Wall -DHOME ' + name)
	for i in range(num):
		print('\n')
		print('=' * 10)
		print('Test # ' + str(i + 1) + '/' + str(num))
		ti = 'in' + str(i + 1)
		to = 'out' + str(i + 1)
		IN = open(ti, 'r').readlines()
		OUT = open(to, 'r').readlines()
		os.system('./a.out < ' + ti + ' > tmp')
		S_in = ''
		S_out = ''
		S_yout = ''
		print('=' * 10)
		print('INPUT')
		for i in IN:
			S_in += i
		print(S_in.rstrip())
		print('=' * 10)
		print('OUTPUT')
		for i in OUT:
			S_out += i
		print(S_out.rstrip())
		YOUT = open('tmp', 'r').readlines()
		print('=' * 10)
		print ('YOUR OUTPUT')
		for i in YOUT:
			S_yout += i
		print(S_yout.rstrip())
    
def check_p(name):
	global num, pyth
	for i in range(num):
		print('\n')
		print('=' * 10)
		print('Test # ' + str(i + 1) + '/' + str(num))
		ti = 'in' + str(i + 1)
		to = 'out' + str(i + 1)
		IN = open(ti, 'r').readlines()
		OUT = open(to, 'r').readlines()
		os.system(pyth + ' ' + name + ' < ' + ti + ' > tmp')
		S_in = ''
		S_out = ''
		S_yout = ''
		print('=' * 10)
		print('INPUT')
		for i in IN:
			S_in += i
		print(S_in.rstrip())
		print('=' * 10)
		print('OUTPUT')
		for i in OUT:
			S_out += i
		print(S_out.rstrip())
		YOUT = open('tmp', 'r').readlines()
		print('=' * 10)
		print ('YOUR OUTPUT')
		for i in YOUT:
			S_yout += i
		print(S_yout.rstrip())

def show():
	global num
	for i in range(num):
		print('\n')
		print('=' * 10)
		print('Test # ' + str(i + 1) + '/' + str(num))
		ti = 'in' + str(i + 1)
		to = 'out' + str(i + 1)
		IN = open(ti, 'r').readlines()
		OUT = open(to, 'r').readlines()
		S_in = ''
		S_out = ''
		print('=' * 10)
		print('INPUT')
		for i in IN:
			S_in += i
		print(S_in.rstrip())
		print('=' * 10)
		print('OUTPUT')
		for i in OUT:
			S_out += i
		print(S_out.rstrip())
		
if (len(sys.argv) > 2):
	print('Wrong arguments')

if (len(sys.argv) == 1):
	show()
	print('\n\n')
	exit(0)

L = str(sys.argv)
L = list(L.split(','))
a = L[1]
name = 'main'

a = a.replace(' ', '').replace('[', '').replace(']', '').replace("'", "")
name = name.replace(' ', '').replace('[', '').replace(']', '').replace("'", "")

if (a == 'c'):
	name += '.cpp'
	check_c(name)
elif (a == 'p'):
	name += '.py'
	check_p(name)
else:
	print('Wrong arguments')
print('\n\n')
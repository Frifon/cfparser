#!/usr/bin/python

##############################
############GLOBAL############
##############################
my_home_name = 'artem' # /home/???/
##############################

import urllib2
import sys
import os

def get_page(link):
	req = urllib2.Request(link + '?locale=en')
	response = urllib2.urlopen(req)
	page = response.read()
	return page

def get_tests(page):
	global my_home_name
	f = -1
	A = []
	t = page.count('<pre>')
	t = t % 2
	while (1):
		L = []
		f = page.find('<pre>', f + 1)
		if (t == 1):
			t = 0
			f = page.find('<pre>', f + 1)
		if (f == -1):
			break
		f2 = page.find('</pre>', f)
		L.append(page[f + 5:f2])
		f = page.find('<pre>', f + 1)
		f2 = page.find('</pre>', f)
		L.append(page[f + 5:f2])
		L[0] = L[0].replace('<br />', '\n').replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
		L[1] = L[1].replace('<br />', '\n').replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
		A.append(L)
	return A


def parse(ID, link):
	global my_home_name
	page = get_page(link)
	S = '<div class="title">'
	f1 = page.find(S)
	name = page[f1 + len(S):page.find('</div>', f1)]
	name = name.replace(' ', '_')
	tmp = ''
	for i in range(len(name)):
		if ('a' <= name[i] <= 'z' or 'A' <= name[i] <= 'Z' or name[i] == '_' or '0' <= name[i] <= '9'):
			tmp += name[i]
	name = tmp
	os.system('mkdir ~/CF/' + ID + '/' + name + '/')
	Tests = get_tests(page)
	print name
	os.system('cp main.* ~/CF/' + ID + '/' + name)
	os.system('cp tester.py ~/CF/' + ID + '/' + name)
	open('/home/' + my_home_name + '/CF/' + ID + '/' + name + '/count', 'w').write(str(len(Tests)) + '\n')
	k = 1
	for i in Tests:
		open('/home/' + my_home_name + '/CF/' + ID + '/' + name + '/in' + str(k), 'w').write(i[0] + '\n')
		open('/home/' + my_home_name + '/CF/' + ID + '/' + name + '/out' + str(k), 'w').write(i[1] + '\n')
		k += 1

ID = str(input('ID:'))
os.system('mkdir ~/CF/' + ID)
page = get_page('http://codeforces.ru/contest/' + ID)
f = 0
L = []
last = 10 ** 20
LTRS = []
while (1):
	fnd = page.rfind('option value="', 0, last)
	last = fnd - 1
	t = fnd + 14
	tmp = ""
	while (page[t] != '"'):
		tmp += page[t]
		t += 1
	if (len(tmp) == 0 or len(tmp) > 3):
		break
	else:
		LTRS.append(tmp)
LTRS = LTRS[::-1]
for let in LTRS:
	f = page.find('/contest/' + ID + '/problem/' + let)
	if (f == -1):
		break
	L.append('http://codeforces.ru/contest/' + ID + '/problem/' + let)
	
for i in L:
	parse(ID, i)
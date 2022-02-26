from random import choice
from time import sleep
from os import name as osname, system
try: from urllib.request import urlopen
except: from urllib2 import urlopen

def random_chars(amount, english_chars=True, russian_chars=False, numbers=True, spec_chars=False, big_chars=True, litte_chars=True):
	text=''
	chars=[]
	if english_chars==True:
		if big_chars==True:
			chars+=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		if litte_chars==True:
			chars+=list('abcdefghijklmnopqrstuvwxyz')
	if russian_chars==True:
		if big_chars==True:
			chars+=list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
		if litte_chars==True:
			chars+=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
	if numbers==True:
		chars+=list('1234567890')
	if spec_chars==True:
		chars+=list('~`!@#$%^&*()-_+={}[]|\/:;"\'<>,.?')
	for i in range(amount):
		text+=choice(chars)
	return text
inputtt=input
def type(text, speed=0.1, input=False):
	for i in text:
		print(i, end='', flush=True)
		sleep(speed)
	if input:
		return inputtt()
	print()
def clear():
	if osname in ['nt', 'dos']:
		system('cls')
		return
	system('clear')
def download(url, name):
	response=urlopen(url)
	with open(name, 'wb') as f:
		f.write(response.read())

import random

from bottle import *

stafir = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_-abcdefghijklmnopqrstuvwxyz0123456789"

def randomStrengur(lengd = 6):
	strengur = ""
	for x in range(lengd):
		strengur += stafir[random.randint(0, len(stafir))-1]
	return strengur

def writePaint(name, data):
	file = open('draw_data/' + name, 'w', encoding='utf-8')
	file.write(data)
	file.close()

def allCharsMatch(str1):
	for x in str1:
		if stafir.count(x) == 0:
			return False
	return True

def replaceAll(strengur):
	strengur2 = strengur
	for x in range(len(strengur)):
		if stafir.count(strengur[x]) == 0:
			strengur2 += "_"
		else:
			strengur2 += strengur2[x]
	return strengur2

@route('/')
def index():
	redirect(randomStrengur())

@route('/<name>')
def paint(name):
	if not allCharsMatch(name):
		redirect(replaceAll(name))
	return static_file("html/root.html", root='.')

@error(404)
def error(error):
	return "404 Not found"

@route('/static/<res>')
def getstatic(res):
	if res == "jquery":
		return static_file("html/jquery.js", root='.')
	elif res == "socket.io":
		return static_file("html/socket.io.js", root='.')
	elif res == "mouse":
		return static_file("html/mousewheel.js", root='.')
	elif res == "brush_paint":
		return static_file("html/brush.png", root='.')
	else:
		abort(404, "404 Not found")

@post('/<paint>/action/<action>')
def post(paint, action):
	if action == "update":
		data = request.forms.get('data')
		writePaint(paint, data)
		return "Hey that's pretty goooooooooooood!"
	else:
		return "";

@route('/<paint>/action/<action>')
def get(paint, action):
	if action == 'getdata':
		response.content_type = "text/plain"
		return static_file("draw_data/" + paint, root=".")

run(host='localhost', port=8080)
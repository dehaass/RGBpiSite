#!/usr/bin/python3

# Possibly a daemon to run a webserver and arduino
# Created March 4, 2016
# Author: Stuart de Haas

import web
import RGBpi

ser = RGBpi.connectPi()

render = web.template.render('templates/')

urls = (
# URL '/' i.e. front page to be handled by the class 'index'
        '/', 'index',
        '/changeColour', 'changeColour',
        '/defineCol', 'defineCol',
        '/changeSeq', 'changeSeq',
        '/sleep', 'sleep',
        '/blank', 'blank'
        )
backgroundCol = 'white'

class index:
    def GET(self):
        return render.index(backgroundCol)

class blank:
    def GET(self):
        return render.blank()

class changeColour:
    def GET(self):
        raise web.seeother('/')
    def POST(self):
        form = web.input()
        colour = form.colour
        if RGBpi.isAlive(ser):
            RGBpi.changeCol(ser, colour)
            global backgroundCol
            backgroundCol = colour
        raise web.seeother('/')

class defineCol:
    def GET(self):
        raise web.seeother('/')
    def POST(self):
        form = web.input()
        red   = form.red
        green = form.green
        blue  = form.blue
        if RGBpi.isAlive(ser):
            RGBpi.changeCol(ser, colour)
            global backgroundCol
            backgroundCol = colour
        raise web.seeother('/')

class changeSeq:
    def GET(self):
        raise web.seeother('/')
    def POST(self):
        form = web.input()
        seq = form.seq
        if RGBpi.isAlive(ser):
            RGBpi.changeSeq(ser, seq)
            global backgroundCol
            backgroundCol = "white"
        raise web.seeother('/')

class sleep:
    def GET(self):
        raise web.seeother('/')
    def POST(self):
        if RGBpi.isAlive(ser):
            RGBpi.sleepArd(ser)
            global backgroundCol
            backgroundCol = 'white'
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

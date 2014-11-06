import gevent.monkey ; gevent.monkey.patch_all()
import os, sys, traceback as tb, bottle, json
from bottle import route, run, template
from uuid import uuid4
from cors import add_headers

from auth import *

@route('/')
def index():
    return 'xxx'

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@bottle.error(404)
def error404(error):
    add_headers(bottle.response)
    return 'Nothing here, sorry'

@route('/auth/login',method=['HEAD','OPTIONS'])
def login():
    add_headers(bottle.response)
    return ''

@route('/auth/login',method=['POST'])
def login():
    add_headers(bottle.response)
    #print "AUTH LOGIN", dict(bottle.request.params)
    #print "AUTH LOGIN", (bottle.request.body)
    d = bottle.request.body.read()
    #print "AUTH LOGIN", repr(d)
    j = json.loads(d)
    print "AUTH LOGIN", repr(j)

    inp = dict( data=j )
    print "AUTH LOGIN INPUT", repr(inp)

    ret = login_user( j['u'], j['p'] )
    print "AUTH LOGIN -RET-", repr(ret)

    return dict(result=ret)

#test()
if __name__=='__main__':run(host='localhost', port=sys.argv[1],server='gevent')

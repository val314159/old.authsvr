import gevent.monkey ; gevent.monkey.patch_all()
import os, sys, traceback as tb, bottle, json
from uuid import uuid4
from cors import add_headers

def DB(_=[]):
    if not _:
        import sqlite3
        conn = sqlite3.connect('.auth.db')
        _.append(conn)
        pass
    return _[0]

def create_db():
    DB().execute('''CREATE TABLE auth (
 uuid text,   email text, password text, digest text,
 secret text, state text, level integer
)''')
    pass

def create_user(email, password, level=1):
    uuid = str(uuid4())
    #secret = str(uuid4())
    secret = 'SECRET'
    state = 'initial'
    DB().execute('''INSERT INTO auth (uuid,email,password,secret,state,level)
 VALUES (?,?,?,?,?,?)''', (uuid,email,password,secret,state,level))
    DB().commit()
    return uuid

def login_user(email, password):
    for rs in DB().execute('''SELECT uuid,secret,state FROM auth WHERE email==? AND password==?''', (email,password)):
        return list(rs)
    return None,None,None

def resecret_user(uuid):
    secret = str(uuid4())
    DB().execute('''UPDATE secret=? WHERE uuid=?''', (secret,uuid))
    DB().commit()
    return secret

def verify_user(uuid, secret):
    for rs in DB().execute('''SELECT 1 FROM auth WHERE uuid==? AND secret==?''', (uuid,secret)):
        return True
    return False

def recreate_db():
    DB().execute('''DROP TABLE IF EXISTS auth''')
    create_db()
    create_user('a','a')
    create_user('v','pass')
    print '-'*80
    z = login_user('vxx','pass')
    print "Z", z
    print '-'*80
    z = login_user('v','pass')
    print "Z", z
    print '='*80

    uuid,secret,state = z

    q = verify_user(uuid,secret)
    print "Q", q
    print '-'*80
    q = verify_user(uuid+"Q",secret+"X")
    print "Q", q
    print '-'*80

    pass


def test():
    print "TEST"
    recreate_db()
    print "TEST2"
    for x in DB().execute('SELECT * FROM auth'):
        print '**', x
        pass
    pass

#test()
#if __name__=='__main__':run(host='localhost', port=sys.argv[1],server='gevent')

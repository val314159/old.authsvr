
run_authsvr () {
  python ws.py 9998
}

run_htmlsvr () {
  python -mSimpleHTTPServer 9999
}

. venv/bin/activate

$*

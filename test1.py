from bottle import route, run

@route('/')
def hello():
    return "<b>Started building the api"

run(host='localhost', port=8080, debug=True)


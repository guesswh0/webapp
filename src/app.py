def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    user = env.get('USER', "World")
    return [f"Hello, {user}!".encode('ascii')]
